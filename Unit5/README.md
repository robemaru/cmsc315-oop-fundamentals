# Unit 5 Discussion: Search Algorithms

## Overview
This assignment compares linear search and binary search. The program demonstrates how different search strategies perform when searching through small and large datasets and how edge cases can affect the search process.

## Learning Objectives
I completed the following learning objectives:
* **Linear Search:** Implemented a sequential search algorithm that checks each item until the target is found.
* **Binary Search:** Implemented an efficient search algorithm that repeatedly divides a sorted dataset in half.
* **Performance Comparison:** Tested both algorithms on small and large datasets to compare their performance.
* **Algorithm Efficiency:** Analyzed the time complexity and trade-offs between linear and binary search.
* **Edge-Case Testing:** Tested empty lists, single-item lists, values at the beginning and end, and values that are not present.

## Design Approach
I created two search functions, `linear_search()` and `binary_search()`, to demonstrate different approaches to finding a target value in a list. The core script utilizes four primary functions:
* `linear_search()` --- checks each element from the beginning of the list until the target is found or the list ends.
* `binary_search()` --- searches a sorted list by repeatedly comparing the target with the middle element and eliminating half of the remaining search space.
* `run_search_test()` --- runs both algorithms and records their results and execution times.
* `main()` --- organizes the required datasets, edge cases, performance analysis, and real-world scenario.

## Implementation Details

### Linear Search
The linear search implementation examines each element sequentially. If the target matches an element, the function returns its index. If the target is not found after checking the entire list, the function returns `-1`. The worst-case time complexity of linear search is `O(n)` because the algorithm may need to examine every element in the dataset.

### Binary Search
The binary search implementation works with a sorted dataset. It compares the target with the middle element and then eliminates either the left or right half of the remaining search area. The worst-case time complexity of binary search is `O(log n)` because the search space is cut approximately in half after each comparison.

### Performance Analysis
Linear search has a worst-case time complexity of `O(n)`, so its running time can increase directly as the dataset grows. Binary search has a worst-case time complexity of `O(log n)`, making it significantly more efficient for large sorted datasets. The main trade-off is that binary search requires the data to be sorted. Linear search does not require sorting and can therefore be a better choice for small or unsorted datasets.

### Real-World Example
A real-world example is searching for a student ID in a university database. If student IDs are stored in a small or unsorted collection, linear search can be simple and practical because it can search the data without requiring it to be sorted. For a large collection of student IDs that is already sorted, binary search is more appropriate. It can quickly eliminate large portions of the dataset and locate the requested student ID efficiently. The trade-off is that maintaining sorted data may require additional processing when records are added, removed, or changed.

## Testing and Edge Cases
I verified the stability of the implementation using the following edge cases:
* A small sorted dataset containing 10 values.
* A large sorted dataset containing 100,000 values.
* Searching for a value that exists in the dataset.
* Searching for a value that does not exist.
* Searching an empty list.
* Searching a single-item list.
* Searching for the first value in a list.
* Searching for the last value in a list.

These tests helped verify that both algorithms return the correct index when a value is found and `-1` when the target is not present.

## Discussion Board Reflection
Completing this assignment helped me better understand how search algorithms affect program efficiency. I learned how to implement both linear search and binary search in Python and how their performance changes as the size of a dataset increases. I also learned that binary search requires the data to be sorted before it can be used correctly. 

One challenge I encountered was understanding how binary search changes the search range after each comparison. I overcame this by breaking the algorithm into smaller steps and using variables for the left, middle, and right positions. Testing edge cases such as an empty list, a single-item list, and values that were not found also helped me make the algorithms more reliable.

Linear search is useful when a dataset is small or unsorted because it is simple and does not require preprocessing. Binary search is a better choice when working with a large, sorted dataset because it eliminates half of the remaining search area with each comparison. The main trade-off is that the data must remain sorted, which can require additional work when data changes frequently.
