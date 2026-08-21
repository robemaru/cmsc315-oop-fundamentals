import collections

class ConfigurationStack:
    def __init__(self):
        self.stack = []

    def push_command(self, command: str):
        print(f"[STACK PUSH] Staging configuration: {command}")
        self.stack.append(command)

    def pop_command(self) -> str:
        if self.is_empty():
            print("[STACK EMPTY] Warning: No active configurations available.")
            return None
        command = self.stack.pop()
        print(f"[STACK POP] Undoing configuration: {command}")
        return command

    def is_empty(self) -> bool:
        return len(self.stack) == 0


class ProvisioningQueue:
    def __init__(self):
        self.queue = collections.deque()

    def enqueue_task(self, task: str):
        print(f"[QUEUE ENQUEUE] Staging provisioning task: {task}")
        self.queue.append(task)

    def dequeue_task(self) -> str:
        if self.is_empty():
            print("[QUEUE EMPTY] Warning: No tasks in the pipeline.")
            return None
        task = self.queue.popleft()
        print(f"[QUEUE DEQUEUE] Executing server task: {task}")
        return task

    def is_empty(self) -> bool:
        return len(self.queue) == 0


if __name__ == "__main__":
    print("=== Data Center Simulation: Stacks & Queues ===\n")
    
    config_manager = ConfigurationStack()
    config_manager.push_command("configure terminal")
    config_manager.push_command("interface gigabitethernet0/1")
    config_manager.pop_command()
    
    print("\n")
    pipeline = ProvisioningQueue()
    pipeline.enqueue_task("Task #1: Run OS Kernel Security Patch Update")
    pipeline.enqueue_task("Task #2: Reconfigure Firewall Access Control Lists")
    pipeline.dequeue_task()
