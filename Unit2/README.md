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

I implemented the `ConfigurationStack` class using a Python list. The list stored the values in the stack, and the `append()` method added new values to the top of the stack. The `pop()` method removed the most recently added value, which demonstrated LIFO behavior.

I implemented the `ProvisioningQueue` class using Python's `collections.deque`. The `append()` method added values to the back of the queue, while `popleft()` removed values from the front. This demonstrated FIFO behavior.

I also implemented methods for checking whether each structure was empty. The stack included `push_command()`, `pop_command()`, `peek_command()`, and `is_empty()`. The queue included `enqueue_task()`, `dequeue_task()`, `front()`, and `is_empty()`.

## Stack: LIFO

A stack follows the LIFO rule, which means Last In, First Out. The last value added to the stack is the first value removed.

I demonstrated this behavior using network configuration commands. Each configuration command was added to the stack. When an undo operation occurred, the most recently added configuration was removed first.

For example, if the configurations were added in this order:

1. Enable security settings
2. Configure firewall
3. Update router interface

The first configuration removed was `Update router interface` because it was the most recently added item.

This behavior is useful for situations such as undo operations, browser history, and reversing recent configuration changes.

## Queue: FIFO

A queue follows the FIFO rule, which means First In, First Out. The first value added to the queue is the first value removed.

I demonstrated this behavior using server provisioning tasks. Tasks were added to the back of the queue, and the task at the front was processed first.

For example, if the tasks entered the queue in this order:

1. Install security updates
2. Configure firewall rules
3. Restart server

`Install security updates` was processed first because it entered the queue first.

This behavior is useful for server processing, print jobs, customer service lines, and other systems where tasks should be processed in the order they arrive.

## Edge Cases

I tested several edge cases in the program.

For the stack, I tested:

- Calling `pop_command()` when the stack was empty.
- Calling `peek_command()` when the stack was empty.
- Creating a stack with one item.
- Removing the only item from the stack.
- Verifying that the stack became empty afterward.

For the queue, I tested:

- Calling `dequeue_task()` when the queue was empty.
- Calling `front()` when the queue was empty.
- Creating a queue with one item.
- Removing the only item from the queue.
- Verifying that the queue became empty afterward.

When an empty stack or queue was accessed, the program returned `None` instead of causing the program to crash.

## LIFO and FIFO Verification

I verified the behavior of both structures using three test values.

The stack removed the values in reverse order:

1. Third
2. Second
3. First

This confirmed LIFO behavior.

The queue removed the values in the same order they were added:

1. First
2. Second
3. Third

This confirmed FIFO behavior.

## Memory Usage

Both data structures used memory based on the number of elements stored.

If a stack or queue contained `n` elements, the space required for the stored elements was O(n). As more elements were added, more memory was required to store those elements.

When elements were removed, the number of stored elements decreased.

The queue used `collections.deque`, which was appropriate because it supported efficient additions and removals from the ends of the queue.

## Custom Real-World Application

My custom application focused on data center configuration and server provisioning.

The stack represented network configuration changes. Because a stack uses LIFO behavior, the most recent configuration change could be undone first.

The queue represented server provisioning tasks. Because a queue uses FIFO behavior, server tasks could be processed in the same order that they were received.

This showed how stacks and queues can be used in practical computing environments.

## Results

I completed the required stack and queue implementations and demonstrated their LIFO and FIFO behavior.

I also tested empty structures and single-item structures to verify that the program handled edge cases correctly.

The program included a custom real-world application involving network configurations and server provisioning tasks.

The tests confirmed that the stack removed the most recently added item first, while the queue removed the oldest item first.

## Conclusion

This assignment helped me understand the differences between stacks and queues and how their ordering rules affect their use in applications.

I learned that a stack is useful when the most recent item needs to be accessed first, while a queue is useful when items need to be processed in the order they arrived.

The real-world examples made the concepts easier to understand because they showed how LIFO and FIFO behavior can be applied to network configuration, server provisioning, and other software systems.

## GitHub Repository

My GitHub repository contains the Python implementation and documentation for this assignment:

https://github.com/robemaru/cmsc315-oop-fundamentals
