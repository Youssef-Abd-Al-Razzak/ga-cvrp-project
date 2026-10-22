"""Print the solution in the format required by the assignment.

Format:
    Route #1: 21 31 19 17 13 7 26
    Route #2: 12 1 16 30
    ...
    Cost: 784.00
"""


def print_solution(problem, chromosome):
    routes = problem.decode(chromosome)
    for k, route in enumerate(routes, start=1):
        print(f"Route #{k}: " + " ".join(str(c) for c in route))
    print(f"Cost: {problem.total_distance(routes):.2f}")
