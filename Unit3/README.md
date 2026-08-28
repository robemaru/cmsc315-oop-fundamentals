# Unit 3 Discussion: List Operations

## Overview

For this Unit 3 discussion, I implemented and tested list operations in Python. The program demonstrated how values could be inserted, deleted, and searched within a Python list. I also tested several edge cases to make sure the program handled invalid operations safely.

## Design Approach

I used a Python list to represent a student's course task list. The list contained tasks such as reading a chapter, completing a quiz, and submitting an assignment.

The program used three functions:

- `insert_at()` inserted a value at a specific position.
- `delete_at()` removed and returned a value from a specific position.
- `search_value()` searched the list for a specific value and returned its index.

The `main()` function tested each operation and displayed the results.

## Insertion

The `insert_at()` function used Python's `insert()` list operation. I tested inserting an item at the beginning, middle, and end of the list.

When an item was inserted near the beginning or middle, existing elements had to shift to the right to make room for the new item. Therefore, insertion can require more work as the number of list elements increases.

## Deletion

The `delete_at()` function first checked whether the requested index was valid. If the index was invalid, the function returned `None`. If the index was valid, the selected item was removed and returned.

Deleting an element from the beginning or middle of a list can cause later elements to shift to the left. This can make deletion more expensive than deleting an item from the end.

## Searching

The `search_value()` function performed a linear search. It checked the list elements sequentially until it found the requested value.

If the value was found, the function returned its index. If the value was not found, it returned `-1`.

## Edge Cases

I tested several edge cases:

1. I attempted to delete an item using an invalid index.
2. I searched for a value that was not in the list.
3. I inserted a value into an empty list.

These tests demonstrated that the program could handle situations that could otherwise cause unexpected behavior.

## Real-World Application

The real-world scenario used in this program was a student managing course tasks. A list was useful because tasks could be added, removed, or searched as the student's workload changed.

For example, a new task could be inserted into the list, a completed task could be deleted, and a specific assignment could be searched for.

## Memory Usage

A Python list stores references to its elements. As more items were added to the list, the amount of memory required also increased.

Therefore, the memory usage of the list grew approximately linearly with the number of elements, or **O(n)**.

Python lists also maintain extra capacity internally so that they can grow efficiently when additional elements are added.

## Testing

I tested the following operations:

- Insertion at the beginning
- Insertion in the middle
- Insertion at the end
- Deletion at the beginning
- Deletion in the middle
- Deletion at the end
- Searching for an existing value
- Searching for a missing value
- Deleting with an invalid index
- Searching for a missing value as an edge case
- Inserting into an empty list

The program was run in IntelliJ IDEA to verify that the operations produced the expected results.

## Linked List vs. Array-Based List Performance
An array-based list stores elements in a contiguous block of memory, allowing for fast O(1) random access but making insertions or deletions near the head a costly O(n) operation due to element shifting. Conversely, a linked list would easily outperform an array-based list during frequent insertions or deletions at the beginning of the collection. Because linked list nodes are dynamically allocated and connected via pointers, elements can be added or removed at the front in absolute O(1) constant time simply by updating reference addresses without shifting any underlying data blocks.

## Conclusion

The implementation demonstrated how Python lists could be used to manage changing collections of data. The testing showed that insertion and deletion can require elements to shift, while searching may require checking elements sequentially. The edge-case tests also demonstrated the importance of validating operations before modifying a list.

## GitHub Repository

[Unit 3 - List Operations](https://github.com/robemaru/cmsc315-oop-fundamentals/tree/main/Unit3)
