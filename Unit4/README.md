# Unit 4 Discussion: Binary Search Trees

## Overview
This assignment introduced Binary Search Trees (BSTs) and recursive tree operations. The program demonstrates how a tree structures numerical keys hierarchically and searches for records efficiently.

## Learning Objectives
I completed the following learning objectives:
* **Built a BST:** Developed structural rules to organize incoming data dynamically.
* **Recursive Operations:** Implemented recursive patterns for clean node insertion and value searching.
* **In-Order Traversal:** Traversed the tree paths to display sorted data sequences.
* **Efficiency Analysis:** Analyzed how tree balancing impacts algorithmic runtime constraints.

## Design Approach
I created a Node class to store each unique value alongside pointers to its left and right children. The core tree structures utilize three primary functions:
* `insert()` — inserts a value recursively into its correct logical subtree location.
* `search()` — searches the tree for a specific key, eliminating half the paths at each step.
* `in_order_traversal()` — visits the left subtree, current node, and right tree to output keys in ascending order.

## Implementation Details

### Node Insertion
During insertion, values smaller than the current node are placed into the left subtree, while larger values are placed in the right subtree. Duplicate employee IDs are explicitly ignored because employee keys must remain unique.

### Value Search
The search operation uses the same tree-ordering logic. Each comparison allows the program to skip half of the remaining nodes. A balanced BST provides an average search performance of `O(log n)`, while a highly unbalanced tree can degrade to `O(n)`.

### Real-World Example
I used employee records organized by employee ID as the real-world scenario. Employee IDs serve as numeric keys. When searching for a record, the program compares the target ID with the current node ID, choosing the left or right path to instantly bypass irrelevant records.

## Testing and Edge Cases
I verified the stability of the implementation using the following edge cases:
* Multiple employee IDs in both left and right subtrees.
* Searching for existing and non-existent employee IDs.
* Traversing an completely empty tree environment.
* Attempting to insert a duplicate employee ID.
* Verifying tree operations on a single-node configuration.

## Discussion Board Reflection
Completing this assignment helped me understand how a Binary Search Tree organizes values efficiently. A major challenge was tracking how recursion updates root node references when a new element is added. I overcame this by drawing out the execution stacks step by step. 

A BST makes searching significantly faster than a linear search because each comparison eliminates a massive chunk of the data pool. In a balanced state, its `O(log n)` performance scales beautifully for massive enterprise database deployments.

---

## GitHub Repository
* [My OOP Fundamentals Repository](https://github.com)
