"""
============================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
CMSC 315
============================================================

OVERVIEW:
This program demonstrates two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

The program includes:
- Stack implementation
- Queue implementation
- LIFO and FIFO demonstrations
- Empty structure edge cases
- Single-item edge cases
- A custom real-world application
============================================================
"""

from collections import deque


# ============================================================
# STACK IMPLEMENTATION - LIFO
# Last In, First Out
# ============================================================

class ConfigurationStack:

    def __init__(self):
        """
        Create an empty stack.
        """
        # TODO (Student): Create the internal data structure for the stack.
        # A Python list is appropriate because it supports efficient
        # append() and pop() operations at the end of the list.
        self.stack = []

    def push_command(self, command: str):
        """
        Add a configuration command to the top of the stack.
        """
        # TODO (Student): Add a value to the stack.
        # Adding items to the end of the list supports LIFO behavior.
        print(f"[STACK PUSH] Staging configuration: {command}")
        self.stack.append(command)

    def pop_command(self) -> str:
        """
        Remove and return the most recently added command.
        """
        # TODO (Student): Remove and return the most recently added value.
        # If the stack is empty, return None instead of causing an error.
        if self.is_empty():
            print("[STACK EMPTY] Warning: No active configurations available.")
            return None

        command = self.stack.pop()
        print(f"[STACK POP] Undoing configuration: {command}")
        return command

    def peek_command(self) -> str:
        """
        Return the top command without removing it.
        """
        # TODO (Student): Return the top value without removing it.
        # The last list item is the top of the stack.
        if self.is_empty():
            print("[STACK EMPTY] Warning: No active configurations available.")
            return None

        command = self.stack[-1]
        print(f"[STACK PEEK] Current configuration: {command}")
        return command

    def is_empty(self) -> bool:
        """
        Return True when the stack contains no commands.
        """
        # TODO (Student): Return True if the stack has no values.
        return len(self.stack) == 0


# ============================================================
# QUEUE IMPLEMENTATION - FIFO
# First In, First Out
# ============================================================

class ProvisioningQueue:

    def __init__(self):
        """
        Create an empty queue.
        """
        # TODO (Student): Create the internal data structure for the queue.
        # collections.deque supports efficient additions and removals
        # from both ends of the queue.
        self.queue = deque()

    def enqueue_task(self, task: str):
        """
        Add a task to the back of the queue.
        """
        # TODO (Student): Add a value to the queue.
        # Adding to the back of the queue supports FIFO behavior.
        print(f"[QUEUE ENQUEUE] Staging provisioning task: {task}")
        self.queue.append(task)

    def dequeue_task(self) -> str:
        """
        Remove and return the task at the front of the queue.
        """
        # TODO (Student): Remove and return the value from the front
        # of the queue. Handle an empty queue safely.
        if self.is_empty():
            print("[QUEUE EMPTY] Warning: No tasks in the pipeline.")
            return None

        task = self.queue.popleft()
        print(f"[QUEUE DEQUEUE] Executing server task: {task}")
        return task

    def front(self) -> str:
        """
        Return the front task without removing it.
        """
        # TODO (Student): Return the front value without removing it.
        # The first item in the deque is the front of the queue.
        if self.is_empty():
            print("[QUEUE EMPTY] Warning: No tasks in the pipeline.")
            return None

        task = self.queue[0]
        print(f"[QUEUE FRONT] Next task: {task}")
        return task

    def is_empty(self) -> bool:
        """
        Return True when the queue contains no tasks.
        """
        # TODO (Student): Return True if the queue has no values.
        return len(self.queue) == 0


# ============================================================
# MAIN DEMONSTRATION
# ============================================================

def main():

    print("====================================================")
    print("       UNIT 2: STACKS AND QUEUES DEMONSTRATION")
    print("====================================================")

    # ========================================================
    # 1. STACK DEMO - LIFO
    # ========================================================

    # TODO (Student): STACK DEMO
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain
    #    what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify that the stack is empty afterward.

    print("\n--- STACK DEMO: LIFO ---")

    config_manager = ConfigurationStack()

    print("\nAdding configurations to the stack:")

    config_manager.push_command("Configure terminal")
    config_manager.push_command("Interface gigabitethernet0/1")
    config_manager.push_command("IP address 192.168.1.10")
    config_manager.push_command("Enable security settings")

    print("\nChecking the top configuration without removing it:")
    config_manager.peek_command()

    print("\nRemoving configurations from the stack:")
    config_manager.pop_command()
    config_manager.pop_command()
    config_manager.pop_command()
    config_manager.pop_command()

    print("\nThe stack should now be empty:")
    config_manager.pop_command()

    # ========================================================
    # 2. QUEUE DEMO - FIFO
    # ========================================================

    # TODO (Student): QUEUE DEMO
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain
    #    what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify that the queue is empty afterward.

    print("\n--- QUEUE DEMO: FIFO ---")

    pipeline = ProvisioningQueue()

    print("\nAdding tasks to the queue:")

    pipeline.enqueue_task("Task #1: Run OS Kernel Security Patch Update")
    pipeline.enqueue_task("Task #2: Reconfigure Firewall Access Control Lists")
    pipeline.enqueue_task("Task #3: Restart Database Service")
    pipeline.enqueue_task("Task #4: Verify Server Connectivity")

    print("\nChecking the front task without removing it:")
    pipeline.front()

    print("\nRemoving tasks from the queue:")
    pipeline.dequeue_task()
    pipeline.dequeue_task()
    pipeline.dequeue_task()
    pipeline.dequeue_task()

    print("\nThe queue should now be empty:")
    pipeline.dequeue_task()

    # ========================================================
    # 3. EDGE CASE TESTS
    # ========================================================

    # TODO (Student): EDGE CASE TESTS
    # Test empty stack operations, empty queue operations,
    # single-item structures, and verify they become empty
    # after the item is removed.

    print("\n--- EDGE CASE TESTS ---")

    print("\nTesting pop on an empty stack:")
    empty_stack = ConfigurationStack()
    empty_stack.pop_command()

    print("\nTesting peek on an empty stack:")
    empty_stack.peek_command()

    print("\nTesting a stack with one item:")
    single_stack = ConfigurationStack()
    single_stack.push_command("Single configuration")
    single_stack.pop_command()
    print(f"Stack empty after removal: {single_stack.is_empty()}")

    print("\nTesting dequeue on an empty queue:")
    empty_queue = ProvisioningQueue()
    empty_queue.dequeue_task()

    print("\nTesting front on an empty queue:")
    empty_queue.front()

    print("\nTesting a queue with one item:")
    single_queue = ProvisioningQueue()
    single_queue.enqueue_task("Single provisioning task")
    single_queue.dequeue_task()
    print(f"Queue empty after removal: {single_queue.is_empty()}")

    # ========================================================
    # 4. CUSTOM REAL-WORLD APPLICATION
    # ========================================================

    # TODO (Student): CUSTOM REAL-WORLD APPLICATION
    # Create a meaningful application using both data structures.
    # Explain how the stack and queue behavior applies to the
    # selected real-world scenario.

    print("\n--- CUSTOM REAL-WORLD APPLICATION ---")
    print("Data center configuration and server provisioning")

    # STACK APPLICATION
    # A network administrator may need to undo the most recent
    # configuration change first. This is a LIFO situation.

    print("\nStack example - undoing network configurations:")

    network_stack = ConfigurationStack()

    network_stack.push_command("Enable security settings")
    network_stack.push_command("Configure firewall")
    network_stack.push_command("Update router interface")

    print("\nThe most recent configuration is undone first:")
    network_stack.pop_command()

    # QUEUE APPLICATION
    # Server provisioning tasks should normally be processed
    # in the same order they were received. This is FIFO.

    print("\nQueue example - processing server tasks:")

    server_queue = ProvisioningQueue()

    server_queue.enqueue_task("Install security updates")
    server_queue.enqueue_task("Configure firewall rules")
    server_queue.enqueue_task("Restart server")

    print("\nTasks are processed in the order they were received:")

    server_queue.dequeue_task()
    server_queue.dequeue_task()
    server_queue.dequeue_task()

    print("\n====================================================")
    print("              PROGRAM COMPLETE")
    print("====================================================")


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()
