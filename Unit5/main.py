"""
=========================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS
Linear Search vs. Binary Search
=========================================================

This program demonstrates and compares two searching
algorithms:

1. Linear Search
2. Binary Search

The program tests both algorithms using:
- A small dataset
- A large dataset
- Edge cases
- Performance timing
- A real-world search scenario
"""

import time


def linear_search(lst, target):
    """
    Perform a linear search.

    Linear search checks each element from the beginning
    of the list until the target is found.

    Parameters:
        lst: List of values to search
        target: Value being searched for

    Returns:
        The index of the target if found.
        -1 if the target is not found.

    Time Complexity:
        Best case: O(1)
        Worst case: O(n)
    """

    for i in range(len(lst)):
        if lst[i] == target:
            return i

    return -1


def binary_search(lst, target):
    """
    Perform a binary search.

    Binary search repeatedly divides a SORTED list in half
    to locate the target.

    Parameters:
        lst: Sorted list of values to search
        target: Value being searched for

    Returns:
        The index of the target if found.
        -1 if the target is not found.

    Time Complexity:
        Best case: O(1)
        Worst case: O(log n)
    """

    left = 0
    right = len(lst) - 1

    while left <= right:
        middle = (left + right) // 2

        if lst[middle] == target:
            return middle

        elif lst[middle] < target:
            left = middle + 1

        else:
            right = middle - 1

    return -1


def run_search_test(data, target):
    """
    Run both search algorithms and display their results
    and execution times.
    """

    # Linear search timing
    start_time = time.perf_counter()
    linear_result = linear_search(data, target)
    linear_time = time.perf_counter() - start_time

    # Binary search timing
    start_time = time.perf_counter()
    binary_result = binary_search(data, target)
    binary_time = time.perf_counter() - start_time

    print(f"Target: {target}")
    print(f"Linear Search Result: {linear_result}")
    print(f"Binary Search Result: {binary_result}")
    print(f"Linear Search Time: {linear_time:.10f} seconds")
    print(f"Binary Search Time: {binary_time:.10f} seconds")
    print()


def main():
    """
    Main function containing the required test cases.
    """

    print("=" * 60)
    print("UNIT 5: SEARCH ALGORITHM PERFORMANCE")
    print("=" * 60)

    # -----------------------------------------------------
    # TODO 1: SMALL DATASET
    # -----------------------------------------------------

    print("\n" + "-" * 60)
    print("SMALL DATASET TEST")
    print("-" * 60)

    small_data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # Test a value that exists in the dataset.
    print("Searching for a value that exists:")
    run_search_test(small_data, 70)

    # Test a value that does not exist.
    print("Searching for a value that does not exist:")
    run_search_test(small_data, 75)

    # -----------------------------------------------------
    # TODO 2: LARGE DATASET
    # -----------------------------------------------------

    print("\n" + "-" * 60)
    print("LARGE DATASET TEST")
    print("-" * 60)

    # range creates a sorted dataset from 1 through 100000.
    large_data = list(range(1, 100001))

    # Search for a value near the end of the dataset.
    print("Searching for a value near the end:")
    run_search_test(large_data, 99999)

    # Search for a value that does not exist.
    print("Searching for a value that does not exist:")
    run_search_test(large_data, 100001)

    # -----------------------------------------------------
    # TODO 3: EDGE CASE TESTS
    # -----------------------------------------------------

    print("\n" + "-" * 60)
    print("EDGE CASE TESTS")
    print("-" * 60)

    # Edge Case 1: Empty list
    empty_list = []

    print("Edge Case 1: Empty list")
    print("Linear Search:", linear_search(empty_list, 10))
    print("Binary Search:", binary_search(empty_list, 10))
    print()

    # Edge Case 2: Single-item list
    single_item = [42]

    print("Edge Case 2: Single-item list")
    print("Searching for 42:")
    print("Linear Search:", linear_search(single_item, 42))
    print("Binary Search:", binary_search(single_item, 42))
    print()

    # Edge Case 3: Value at the beginning
    print("Edge Case 3: Value at the beginning")
    edge_list = [10, 20, 30, 40, 50]
    print("Searching for 10:")
    print("Linear Search:", linear_search(edge_list, 10))
    print("Binary Search:", binary_search(edge_list, 10))
    print()

    # Edge Case 4: Value at the end
    print("Edge Case 4: Value at the end")
    print("Searching for 50:")
    print("Linear Search:", linear_search(edge_list, 50))
    print("Binary Search:", binary_search(edge_list, 50))
    print()

    # Edge Case 5: Value not present
    print("Edge Case 5: Value not present")
    print("Searching for 99:")
    print("Linear Search:", linear_search(edge_list, 99))
    print("Binary Search:", binary_search(edge_list, 99))
    print()

    # -----------------------------------------------------
    # TODO 4: PERFORMANCE ANALYSIS
    # -----------------------------------------------------

    print("\n" + "-" * 60)
    print("PERFORMANCE ANALYSIS")
    print("-" * 60)

    print("""
Linear search checks elements one at a time. Its worst-case
time complexity is O(n), meaning that the amount of work can
increase directly with the size of the dataset.

Binary search eliminates approximately half of the remaining
search space after every comparison. Its worst-case time
complexity is O(log n).

Binary search is therefore much more efficient for large
sorted datasets. However, binary search requires the data to
be sorted. If data is constantly changing and does not need
to be maintained in sorted order, linear search may be easier
and more practical.
""")

    # -----------------------------------------------------
    # TODO 5: REAL-WORLD SEARCH SCENARIO
    # -----------------------------------------------------

    print("\n" + "-" * 60)
    print("REAL-WORLD SEARCH SCENARIO")
    print("-" * 60)

    print("""
Example: Searching for a student ID in a university database.

If the student IDs are stored in an unsorted list and the
database is small, linear search can be a simple and effective
choice because it does not require the data to be sorted.

If thousands or millions of student IDs are stored in a
sorted list, binary search would be more appropriate because
it can locate an ID much faster by repeatedly dividing the
search area in half.

The trade-off is that binary search requires sorted data.
Maintaining sorted data can require additional processing
when records are added or changed.
""")

    # -----------------------------------------------------
    # FINAL COMPARISON
    # -----------------------------------------------------

    print("\n" + "-" * 60)
    print("FINAL COMPARISON")
    print("-" * 60)

    print("Linear Search: O(n)")
    print("Binary Search: O(log n)")
    print()
    print("Binary search is generally faster for large SORTED data.")
    print("Linear search is useful for smaller or UNSORTED data.")


if __name__ == "__main__":
    main()
