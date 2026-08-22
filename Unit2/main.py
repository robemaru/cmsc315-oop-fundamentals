import collections


# ============================================================
# UNIT 2 DISCUSSION: STACKS AND QUEUES
# CMSC 315
# ============================================================


# ============================================================
# STACK IMPLEMENTATION - LIFO
# Last In, First Out
# ============================================================

class ConfigurationStack:
    def __init__(self):
        """Create an empty stack."""
        self.stack = []

    def push_command(self, command: str):
        """Add a configuration command to the top of the stack."""
        print(f"[STACK PUSH] Staging configuration: {command}")
        self.stack.append(command)

    def pop_command(self) -> str:
        """Remove and return the most recently added command."""
        if self.is_empty():
            print("[STACK EMPTY] Warning: No active configurations available.")
            return None

        command = self.stack.pop()
        print(f"[STACK POP] Undoing configuration: {command}")
        return command

    def peek_command(self) -> str:
        """Return the top command without removing it."""
        if self.is_empty():
            print("[STACK EMPTY] Warning: No active configurations available.")
            return None

        command = self.stack[-1]
        print(f"[STACK PEEK] Current configuration: {command}")
        return command

    def is_empty(self) -> bool:
        """Return True when the stack contains no commands."""
        return len(self.stack) == 0


# ============================================================
# QUEUE IMPLEMENTATION - FIFO
# First In, First Out
# ============================================================

class ProvisioningQueue:
    def __init__(self):
        """Create an empty queue."""
        self.queue = collections.deque()

    def enqueue_task(self, task: str):
        """Add a task to the back of the queue."""
        print(f"[QUEUE ENQUEUE] Staging provisioning task: {task}")
        self.queue.append(task)

    def dequeue_task(self) -> str:
        """Remove and return the task at the front of the queue."""
        if self.is_empty():
            print("[QUEUE EMPTY] Warning: No tasks in the pipeline.")
            return None

        task = self.queue.popleft()
        print(f"[QUEUE DEQUEUE] Executing server task: {task}")
        return task

    def front(self) -> str:
        """Return the front task without removing it."""
        if self.is_empty():
            print("[QUEUE EMPTY] Warning: No tasks in the pipeline.")
            return None

        task = self.queue[0]
        print(f"[QUEUE FRONT] Next task: {task}")
        return task

    def is_empty(self) -> bool:
        """Return True when the queue contains no tasks."""
        return len(self.queue) == 0


# ============================================================
# MAIN DEMONSTRATION
# ============================================================

def main():
    print("==============================================")
    print("   UNIT 2: STACKS AND QUEUES DEMONSTRATION")
    print("==============================================")

    # ========================================================
    # 1. STACK DEMO - LIFO
    # ========================================================

    print("\n--- STACK DEMO: LIFO ---")

    config_manager = ConfigurationStack()

    print("\nAdding configurations to the stack:")
    config_manager.push_command("configure terminal")
    config_manager.push_command("interface gigabitethernet0/1")
    config_manager.push_command("ip address 192.168.1.10")

    print("\nChecking the top configuration without removing it:")
    config_manager.peek_command()

    print("\nRemoving configurations from the stack:")
    config_manager.pop_command()
    config_manager.pop_command()
    config_manager.pop_command()

    print("\nThe stack should now be empty:")
    config_manager.pop_command()


    # ========================================================
    # 2. QUEUE DEMO - FIFO
    # ========================================================

    print("\n--- QUEUE DEMO: FIFO ---")

    pipeline = ProvisioningQueue()

    print("\nAdding tasks to the queue:")
    pipeline.enqueue_task("Task #1: Run OS Kernel Security Patch Update")
    pipeline.enqueue_task("Task #2: Reconfigure Firewall Access Control Lists")
    pipeline.enqueue_task("Task #3: Restart Database Service")

    print("\nChecking the front task without removing it:")
    pipeline.front()

    print("\nRemoving tasks from the queue:")
    pipeline.dequeue_task()
    pipeline.dequeue_task()
    pipeline.dequeue_task()

    print("\nThe queue should now be empty:")
    pipeline.dequeue_task()


    # ========================================================
    # 3. EDGE CASE TESTS
    # ========================================================

    print("\n--- EDGE CASE TESTS ---")

    print("\nTesting pop on an empty stack:")
    empty_stack = ConfigurationStack()
    empty_stack.pop_command()

    print("\nTesting peek on an empty stack:")
    empty_stack.peek_command()

    print("\nTesting dequeue on an empty queue:")
    empty_queue = ProvisioningQueue()
    empty_queue.dequeue_task()

    print("\nTesting front on an empty queue:")
    empty_queue.front()


    # ========================================================
    # 4. CUSTOM REAL-WORLD APPLICATION
    # ========================================================

    print("\n--- CUSTOM REAL-WORLD APPLICATION ---")
    print("Data center configuration and server provisioning")

    print("\nStack example - undoing network configurations:")
    network_stack = ConfigurationStack()

    network_stack.push_command("Enable security settings")
    network_stack.push_command("Configure firewall")
    network_stack.push_command("Update router interface")

    print("\nThe most recent configuration is undone first:")
    network_stack.pop_command()

    print("\nQueue example - processing server tasks:")
    server_queue = ProvisioningQueue()

    server_queue.enqueue_task("Install security updates")
    server_queue.enqueue_task("Configure firewall rules")
    server_queue.enqueue_task("Restart server")

    print("\nTasks are processed in the order they were received:")
    server_queue.dequeue_task()
    server_queue.dequeue_task()
    server_queue.dequeue_task()


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()
