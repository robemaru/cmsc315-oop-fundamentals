Unit 4 Discussion: Binary Search Trees
Overview
This assignment introduced Binary Search Trees (BSTs) and recursive tree operations.

Learning Objectives
I completed the following learning objectives:

Built a BST.
Inserted values recursively.
Searched for values recursively.
Performed an in-order traversal.
Explained how BST organization affects efficiency.
Implementation
I created a Node class to store each value and references to its left and right children. I created a BST class with a root reference and implemented recursive insertion, recursive searching, and in-order traversal.

During insertion, values smaller than the current node were placed in the left subtree, while larger values were placed in the right subtree. Duplicate employee IDs were ignored because employee IDs should be unique.

The search operation used the same ordering. Each comparison allowed the program to continue only into the subtree where the requested value could exist. A balanced BST can provide average O(log n) search and insertion performance, while a highly unbalanced BST can become O(n).

In-Order Traversal
I used in-order traversal by visiting the left subtree, the current node, and then the right subtree. Because of the BST ordering rule, this produced the employee IDs in ascending order.

Real-World Example
I used employee records organized by employee ID as the real-world scenario. Employee IDs can be used as numeric keys in a BST. When searching for an employee, the program compares the requested ID with the current ID and chooses the left or right subtree. This reduces the number of records that need to be considered when the tree is reasonably balanced.

Testing and Edge Cases
I tested:

Multiple employee IDs in both left and right subtrees.
Two existing employee IDs.
Two missing employee IDs.
An empty tree traversal.
Searching an empty tree.
A duplicate employee ID.
A single-node tree.
The tests showed that the BST handled normal operations and edge cases without errors.

Discussion Board Reflection
Completing this assignment helped me understand how a Binary Search Tree organizes values by placing smaller values on the left and larger values on the right. I practiced recursive insertion, recursive searching, and in-order traversal. I also learned why an in-order traversal of a BST produces values in sorted order. One challenge was understanding how recursion returns an updated node reference when a new value is inserted. I overcame this by following each comparison from the root and tracing whether the value belonged in the left or right subtree. I also tested edge cases, including an empty tree, a duplicate employee ID, and a single-node tree. For my real-world example, I used employee records organized by employee ID. A BST can make searching efficient because each comparison can eliminate part of the tree. In a balanced BST, search and insertion are typically O(log n), which is more efficient than a linear search that may require O(n) comparisons. However, if the BST becomes highly unbalanced, its performance can become O(n).

GitHub Repository
https://github.com/robemaru/cmsc315-oop-fundamentals
