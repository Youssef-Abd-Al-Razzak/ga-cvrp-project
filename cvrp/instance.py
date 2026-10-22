"""CVRP instance data + file reader."""
import os
import re
from dataclasses import dataclass


@dataclass
class CVRPInstance:
    name: str
    capacity: int
    coords: list        # coords[i] = (x, y); index 0 = depot
    demands: list       # demands[i]; demands[0] = 0

    @property
    def num_customers(self) -> int:
        return len(self.coords) - 1


def load_instance(path: str) -> CVRPInstance:
    """Read a CVRP instance file.

    Supported formats (auto-detected):
      1. TSPLIB / CVRPLIB (.vrp): NAME, CAPACITY, NODE_COORD_SECTION,
         DEMAND_SECTION, DEPOT_SECTION.
      2. Plain numeric: first line "<num_nodes> <capacity>", then one line per
         node "<id> <x> <y> <demand>" (first node = depot).
    """
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    name = os.path.splitext(os.path.basename(path))[0]
    if re.search(r"NODE_COORD_SECTION", text, re.IGNORECASE):
        return _parse_tsplib(text, name)
    return _parse_plain(text, name)


def _parse_tsplib(text: str, default_name: str) -> CVRPInstance:
    name, capacity = default_name, None
    coords, demands = {}, {}
    depot_id = None
    section = None
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.upper() == "EOF":
            continue
        upper = line.upper()
        if upper.startswith("NODE_COORD_SECTION"):
            section = "coord"
            continue
        if upper.startswith("DEMAND_SECTION"):
            section = "demand"
            continue
        if upper.startswith("DEPOT_SECTION"):
            section = "depot"
            continue
        if ":" in line and section is None or (":" in line and re.match(r"^[A-Za-z_]+\s*:", line)):
            key, _, value = line.partition(":")
            key, value = key.strip().upper(), value.strip()
            if key == "NAME":
                name = value
            elif key == "CAPACITY":
                capacity = int(float(value))
            section = None
            continue
        parts = line.split()
        if section == "coord":
            coords[int(parts[0])] = (float(parts[1]), float(parts[2]))
        elif section == "demand":
            demands[int(parts[0])] = int(float(parts[1]))
        elif section == "depot":
            if int(parts[0]) != -1 and depot_id is None:
                depot_id = int(parts[0])
    if capacity is None or not coords:
        raise ValueError("invalid instance file: missing CAPACITY or coordinates")
    if depot_id is None:
        depot_id = min(coords)
    # depot first, then customers in id order
    order = [depot_id] + sorted(i for i in coords if i != depot_id)
    return CVRPInstance(
        name=name,
        capacity=capacity,
        coords=[coords[i] for i in order],
        demands=[0] + [demands.get(i, 0) for i in order[1:]],
    )


def _parse_plain(text: str, default_name: str) -> CVRPInstance:
    rows = [ln.split() for ln in text.splitlines() if ln.strip()]
    if len(rows) < 2:
        raise ValueError("invalid instance file")
    capacity = int(float(rows[0][1]))
    coords, demands = [], []
    for r in rows[1:]:
        if len(r) < 4:
            continue
        coords.append((float(r[1]), float(r[2])))
        demands.append(int(float(r[3])))
    demands[0] = 0
    return CVRPInstance(default_name, capacity, coords, demands)
