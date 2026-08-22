# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explored two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

The assignment focused on implementing the basic operations for stacks and queues, demonstrating their behavior, testing edge cases, and connecting each structure to a real-world application.

## Learning Objectives

The assignment helped me:

- Implement stack operations.
- Implement queue operations.
- Understand LIFO behavior.
- Understand FIFO behavior.
- Create and test edge cases.
- Connect data structures to real-world applications.
- Understand how memory usage grows as items are added.

## Implementation Approach

I implemented the `Stack` class using a Python list. The list stored the values in the stack, and the `append()` method added new values to the top of the stack. The `pop()` method removed the most recently added value, which demonstrated LIFO behavior.

I implemented the `Queue` class using Python's `collections.deque`. The `append()` method added values to the back of the queue, while `popleft()` removed values from the front. This demonstrated FIFO behavior.

I also implemented methods for checking whether each structure was empty. The stack included `push()`, `pop()`, `peek()`, and `is_empty()`. The queue included `enqueue()`, `dequeue()`, `front()`, and `is_empty()`.

## Stack: LIFO

A stack follows the LIFO rule, which means Last In, First Out. The last value added to the stack is the first value removed.

I demonstrated this behavior using a text editor undo-history scenario. Each new editing action was added to the stack. When an undo operation occurred, the most recent action was removed first.

For example, if the actions were added in this order:

1. Type assignment title
2. Write paragraph
3. Add code
4. Save document

The first action removed from the stack was `Save document`, because it was the most recently added item.

## Queue: FIFO

A queue follows the FIFO rule, which means First In, First Out. The first value added to the queue is the first value removed.

I demonstrated this behavior using a coffee shop line. Customers were added to the back of the queue, and the customer at the front was served first.

For example, if four customers entered the queue in this order:

1. Customer 1
2. Customer 2
3. Customer 3
4. Customer 4

`Customer 1` was served first because that customer entered the queue first.

## Edge Cases

I tested several edge cases in the program.

For the stack, I tested:

- Calling `pop()` when the stack was empty.
- Calling `peek()` when the stack was empty.
- Creating a stack with one item.
- Removing the only item from the stack.
- Verifying that the stack became empty afterward.

For the queue, I tested:

- Calling `dequeue()` when the queue was empty.
- Calling `front()` when the queue was empty.
- Creating a queue with one item.
- Removing the only item from the queue.
- Verifying that the queue became empty afterward.

When an empty stack or queue was accessed, the operation returned `None` instead of causing the program to crash.

## Memory Usage

Both data structures used memory based on the number of elements stored.

If a stack or queue contained `n` elements, the space required for the stored elements was O(n). As more elements were added, more memory was required to store those elements.

When elements were removed, the number of stored elements decreased.

The queue used `collections.deque`, which was appropriate because it supported efficient additions and removals from the ends of the queue.

## Results

I completed the required TODO sections in the Python starter file while keeping the TODO prompts in place.

I demonstrated both LIFO and FIFO behavior and tested the required edge cases. The program also included real-world examples showing how stacks and queues can be used outside of a classroom setting.

## Conclusion

This assignment helped me understand the differences between stacks and queues and how their ordering rules affect their use in applications. I learned that a stack is useful when the most recent item needs to be accessed first, while a queue is useful when items need to be processed in the order they arrived.

The real-world examples made the concepts easier to understand because they showed how LIFO and FIFO behavior can be applied to common software and everyday situations.

## GitHub Repository

https://github.com/robemaru/cmsc315-oop-fundamentals
