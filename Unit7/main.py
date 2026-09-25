"""
UNIT 7: DISCUSSION: SORTING ALGORITHMS
CMSC 315 - Data Structures and Analysis

This program implements and compares Bubble Sort and Merge Sort.
It tests both algorithms using multiple datasets, edge cases,
and a real-world sorting example.
"""

import time


def bubble_sort(lst):
    """Return a sorted copy of lst using Bubble Sort."""
    arr = lst.copy()

    for i in range(len(arr)):
        swapped = False

        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


def merge_sort(lst):
    """Return a sorted copy of lst using Merge Sort."""
    if len(lst) <= 1:
        return lst.copy()

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)


def merge(left, right):
    """Merge two sorted lists into one sorted list."""
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


def test_algorithm(algorithm, data):
    """Run an algorithm and return its result and execution time."""
    start_time = time.perf_counter()
    sorted_data = algorithm(data)
    elapsed_time = time.perf_counter() - start_time
    return sorted_data, elapsed_time


def run_dataset_test(dataset_name, data):
    """Test both sorting algorithms on the same dataset."""
    print("\n" + "=" * 60)
    print(f"DATASET: {dataset_name}")
    print("=" * 60)
    print(f"Original data: {data}")

    bubble_result, bubble_time = test_algorithm(bubble_sort, data)
    merge_result, merge_time = test_algorithm(merge_sort, data)

    print("\nBubble Sort result:")
    print(bubble_result)
    print(f"Bubble Sort time: {bubble_time:.8f} seconds")

    print("\nMerge Sort result:")
    print(merge_result)
    print(f"Merge Sort time: {merge_time:.8f} seconds")

    print("\nResults match:", bubble_result == merge_result)
    print("Bubble Sort correctly sorted:", bubble_result == sorted(data))
    print("Merge Sort correctly sorted:", merge_result == sorted(data))


def test_datasets():
    """Test multiple datasets."""
    datasets = {
        "Random Data": [64, 34, 25, 12, 22, 11, 90, 5],
        "Already Sorted Data": [1, 2, 3, 4, 5, 6, 7, 8],
        "Reverse-Sorted Data": [8, 7, 6, 5, 4, 3, 2, 1],
        "Data With Duplicates": [5, 3, 8, 3, 9, 5, 1, 3],
    }

    for name, data in datasets.items():
        run_dataset_test(name, data)


def real_world_example():
    """Demonstrate a real-world sorting example."""
    ratings = [4.5, 2.0, 5.0, 3.5, 4.0, 1.5, 3.0]

    print("\n" + "=" * 60)
    print("REAL-WORLD SORTING EXAMPLE")
    print("=" * 60)
    print("Movie ratings:")
    print(ratings)

    print("\nRatings sorted using Bubble Sort:")
    print(bubble_sort(ratings))

    print("\nRatings sorted using Merge Sort:")
    print(merge_sort(ratings))

    print(
        "\nExample: A streaming platform could use sorting algorithms "
        "to organize customer ratings, viewing history, or search results."
    )


def test_edge_cases():
    """Test boundary and unusual input cases."""
    edge_cases = {
        "Empty list": [],
        "Single-element list": [42],
        "Two elements": [2, 1],
        "All duplicate values": [7, 7, 7, 7],
        "Negative values": [-5, -1, -10, 3, 0],
        "Already sorted": [1, 2, 3, 4, 5],
    }

    print("\n" + "=" * 60)
    print("EDGE CASE TESTING")
    print("=" * 60)

    for case_name, data in edge_cases.items():
        bubble_result = bubble_sort(data)
        merge_result = merge_sort(data)

        print(f"\n{case_name}")
        print(f"Input:        {data}")
        print(f"Bubble Sort:  {bubble_result}")
        print(f"Merge Sort:   {merge_result}")

        status = bubble_result == merge_result == sorted(data)
        print("Status:", "PASS" if status else "FAIL")


def performance_comparison():
    """Compare performance on larger reverse-sorted datasets."""
    print("\n" + "=" * 60)
    print("PERFORMANCE COMPARISON")
    print("=" * 60)

    for size in [100, 500, 1000]:
        data = list(range(size, 0, -1))

        _, bubble_time = test_algorithm(bubble_sort, data)
        _, merge_time = test_algorithm(merge_sort, data)

        print(f"\nDataset size: {size}")
        print(f"Bubble Sort: {bubble_time:.8f} seconds")
        print(f"Merge Sort:  {merge_time:.8f} seconds")

        if bubble_time > merge_time:
            print("Faster algorithm: Merge Sort")
        elif merge_time > bubble_time:
            print("Faster algorithm: Bubble Sort")
        else:
            print("Both algorithms had similar execution times.")


def main():
    print("=" * 60)
    print("UNIT 7: SORTING ALGORITHMS")
    print("=" * 60)
    print("This program compares Bubble Sort and Merge Sort.")

    test_datasets()
    real_world_example()
    test_edge_cases()
    performance_comparison()

    print("\n" + "=" * 60)
    print("PROGRAM COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
