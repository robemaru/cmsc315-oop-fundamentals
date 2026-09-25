# CMSC 315 - Unit 7 Discussion: Sorting Algorithms

## Course Information
* **Course:** CMSC 315 - Data Structures and Analysis
* **Institution:** University of Maryland Global Campus (UMGC)

## Project Overview
This project implements, tests, and analyzes the performance of two fundamental sorting paradigms: **Bubble Sort** and **Merge Sort**. The implementation evaluates both algorithms using a benchmarking harness across various dataset configurations, extreme edge cases, and a real-world streaming data simulation.

## Learning Objectives
* Implement an optimized **Bubble Sort** utilizing early-exit logic.
* Implement a recursive **Merge Sort** utilizing a divide-and-conquer strategy.
* Analyze empirical execution runtimes using high-precision timers.
* Verify algorithmic stability using diverse data profiles and edge cases.
* Understand the performance trade-offs between O(n²) and \(O(n \log n)\) time complexities.

## Bubble Sort
Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. 
* **Best Case Complexity:** O(n) — Achieved when the input data is already sorted, terminating early via a swap-detection flag.
* **Average Case Complexity:** O(n²)
* **Worst Case Complexity:** O(n²)
* **Space Complexity:** O(1) auxiliary (In-place sorting).

## Merge Sort
Merge Sort is a classic divide-and-conquer algorithm. It recursively divides the unsorted list into n sub-lists until each sub-list contains exactly one element, then merges those sub-lists back together in a sorted manner.
* **Best Case Complexity:** \(O(n \log n)\)
* **Average Case Complexity:** \(O(n \log n)\)
* **Worst Case Complexity:** \(O(n \log n)\)
* **Space Complexity:** O(n) auxiliary space required to allocate temporary sub-arrays during the merge phase.

## Algorithm Comparison

| Feature | Bubble Sort | Merge Sort |
| :--- | :--- | :--- |
| **Algorithmic Approach** | Repeated adjacent comparisons | Divide-and-conquer recursion |
| **Best-Case Time** | O(n) (with optimized early-exit flag) | \(O(n \log n)\) |
| **Average-Case Time** | O(n²) | \(O(n \log n)\) |
| **Worst-Case Time** | O(n²) | \(O(n \log n)\) |
| **Space Complexity** | O(1) (In-place) | O(n) (Requires extra memory allocation) |
| **Implementation Complexity** | Low / Simple logic | Moderate / Recursive stack |
| **Suitability for Large Scale** | Poor / High performance degradation | Excellent / Highly predictable scaling |

## Testing Parameters & Edge Cases
To verify code correctness and defensive stability, the suite evaluates both algorithms against the following array configurations:
* **Standard Test Arrays:** Uniformly distributed random data, completely pre-sorted arrays, reverse-sorted chains, and arrays containing heavy duplicate clusters.
* **Boundary Edge Cases:** 
  * Empty lists (`[]`)
  * Single-element lists (`[x]`)
  * Two-element unsorted arrays (`[y, x]`)
  * Arrays containing exclusively uniform duplicate values
  * Arrays containing negative integer values
  * Arrays containing mixed floating-point metrics

## Performance Analysis
The benchmarking module tracks processing latency by wrapping execution blocks inside high-precision `time.perf_counter()` windows across input sizes of **100, 500, and 1,000 elements**.
* **Bubble Sort** demonstrates a steep, quadratic latency curve as the input array scales. The exponential rise in comparisons and swaps renders it unsuitable for high-throughput production tracks.
* **Merge Sort** maintains a flat, highly scalable runtime curve across expanding element groups. The recursive division strategy yields predictable performance even under worst-case data layout configurations.

## Real-World Scenario
In an enterprise video streaming application, sorting algorithms are used to organize user viewing histories, search outputs, and media ratings. While Bubble Sort may be acceptable for small, localized preferences on a user's client profile, sorting millions of database records requires Merge Sort's \(O(n \log n)\) runtime to prevent thread blockages and minimize server I/O latency.

## Challenges & Implementation Notes
The primary technical challenge involved managing call-stack pointer management during Merge Sort's split phase and ensuring temporary arrays were merged back cleanly without introducing indexing off-by-one errors. Comprehensive unit testing across empty and negative boundaries successfully proved the structural integrity of both sorting implementations.

## Conclusion
While both algorithms consistently converge on identical sorted structures, their execution paths scale completely differently. Bubble Sort functions as a highly visual introductory paradigm for educational settings, whereas Merge Sort remains a fundamental standard for production-grade engineering when dealing with enterprise-scale matrices.

## How to Run
Execute the testing and performance evaluation suite directly via your terminal:
```bash
python unit_7_discussion.py
```
## GitHub Repository: https://github.com/robemaru/cmsc315-oop-fundamentals/tree/main/Unit7
