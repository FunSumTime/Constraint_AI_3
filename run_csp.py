from cs4300_csp_parser import parse_cs4300
from cs4300_csp import solve_backtracking, solve_backtrackingMRV
import time


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python run_csp.py <problem.csp>")
        sys.exit(1)
    csp = parse_cs4300(sys.argv[1])
    any_sol = False
    start_time = time.perf_counter()
    for i, sol in enumerate(solve_backtracking(csp), 1):
        any_sol = True
        print(f"Solution #{i}: {sol}")
        end_time = time.perf_counter()
        Time_all = end_time - start_time
        print(Time_all)
    if not any_sol:
        print("No solutions.")

    print()
    start_time = time.perf_counter()
    print("mine")
    for i, sol in enumerate(solve_backtrackingMRV(csp), 1):
        any_sol = True
        print(f"Solution #{i}: {sol}")
        end_time = time.perf_counter()
        Time_all = end_time - start_time
        print(Time_all)
    if not any_sol:
        print("No solutions.")
