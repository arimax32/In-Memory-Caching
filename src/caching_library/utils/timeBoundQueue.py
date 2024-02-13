import time
import heapq

class TimeBoundTask:
    def __init__(self, delay, task):
        self.delay = delay
        self.task = task
        self.execution_time = time.time() + delay

    def __lt__(self, other):
        return self.execution_time < other.execution_time

class TimeBoundQueue:
    def __init__(self, ):
        self.queue = []

    def push(self, delay, task):
        delayed_task = TimeBoundTask(delay, task)
        heapq.heappush(self.queue, delayed_task)

    def pop(self):
        while self.queue:
            current_time = time.time()
            next_task = self.queue[0]

            if current_time >= next_task.execution_time:
                return heapq.heappop(self.queue).task
            else:
                time_unit = next_task.execution_time - current_time
                time.sleep(time_unit)