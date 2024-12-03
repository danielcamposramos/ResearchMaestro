
# ResearchMaestro Module with Enhanced Logging and Fixed `get_log` Method
class ResearchMaestro:
    def __init__(self):
        self.task_queue = []
        self.log = []

    def add_task(self, task, priority=1):
        self.task_queue.append((priority, task))
        self.task_queue.sort()  # Sort by priority

    def process_tasks(self):
        while self.task_queue:
            priority, task = self.task_queue.pop(0)
            try:
                # Log task initiation
                self.log.append(f"Starting task: {task} (Priority: {priority})")
                print(f"Processing task: {task} (Priority: {priority})")
                self.log.append(f"Task completed: {task}")
            except Exception as e:
                self.log.append(f"Task failed: {task} - {str(e)}")
                print(f"Task failed: {task} - {str(e)}")

    def get_log(self):
        return self.log
