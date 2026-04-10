import math

def min_quantum_leaps(N: int) -> int:
    if N < 2:
        raise ValueError("N must be >= 2 per constraints.")
    if N == 2:
        return 2
    return math.floor(math.log2(N)) + 1

def run_tests():
    test_cases = [
        (2, 2, "Smallest N"),
        (4, 3, "Power of 2"),
        (6, 3, "Visible test 2"),
        (10, 4, "Visible test 1"),
        (15, 4, "Visible test 3"),
        (16, 5, "Power of 2"),
        (100, 7, "N=100"),
        (1000, 10, "N=1000"),
        (1000000, 20, "N=10^6"),
    ]

    print("=" * 60)
    print(f"{'N':>10}  {'Expected':>10}  {'Got':>6}  {'Pass?':>6}")
    print("=" * 60)

    all_passed = True
    for N, expected, desc in test_cases:
        result = min_quantum_leaps(N)
        status = "✅" if result == expected else "❌"
        if result != expected:
            all_passed = False
        print(f"{N:>10}  {expected:>10}  {result:>6}  {status}  {desc}")

    print("=" * 60)
    print("All tests passed!" if all_passed else "Some tests FAILED ")
    print()

def show_optimal_path(N: int):
    path = [1]
    cur = 1
    while cur * 2 < N:
        cur *= 2
        path.append(cur)
    if path[-1] != N:
        path.append(N)

    print(f"Optimal path for N={N}:")
    print("  " + " → ".join(str(g) for g in path))
    print(f"  Total leaps: {len(path) - 1}")
    print()

if __name__ == "__main__":
    N = int(input("Enter gate number N: "))
    print(min_quantum_leaps(N))