from math import ceil, factorial, exp
from random import randrange
from task import *

TIME_UNIT = 10

class Queue:
    def __init__(self, tasks_amount, arrival_rate, max_runtime):
        timeline_stock = max_runtime * tasks_amount

        self.sum_await_time = 0
        self.downtime = 0
        self.intervals = set()
        self.x_await_time = []
        self.y_tasks_amount = []
        self.x_interval_probability = []
        self.y_interval_probability = []
        self.x_tasks_unit_probability = []
        self.y_tasks_unit_probability = []

        self.busy = 0
        self.max_runtime = max_runtime
        self.tasks_amount = tasks_amount
        self.arrival_rate = arrival_rate
        self.arrival_density = arrival_rate / TIME_UNIT
        self.units = ceil(tasks_amount / arrival_rate)
        self.beats = self.units * TIME_UNIT + timeline_stock
        self.timeline = [[] for i in range(self.beats)]
        self.last_active_beat = self.beats - 1

    def __str__(self):
        beat_tasks = lambda bt: ', '.join(map(lambda t: str(t), bt))
        beat_to_string = lambda bt: '\t[{}]'.format(beat_tasks(bt))
        timeline = ',\n'.join(map(beat_to_string, self.timeline))
        return f'[\n{timeline}\n]'

    def init_timeline(self):
        for unit in range(self.units):
            remainder = self.tasks_amount - unit * self.arrival_rate
            tasks_unit_amount = self.arrival_rate \
                if remainder > self.arrival_rate \
                else remainder

            for i in range(tasks_unit_amount):
                task = Task(self.max_runtime)
                beat_index = task.arrival + unit * TIME_UNIT
                beat_tasks = self.timeline[beat_index]
                task.abs_arrival = beat_index
                beat_tasks.append(task)

    def execute(self, task):
        task.done = True
        self.busy = task.runtime - 1

    def pick_task(self, beat):
        timeline = self.timeline[0:beat]
        tasks = [task for beat in timeline for task in beat if not task.done]

        if len(tasks):
            random_task = tasks[randrange(0, len(tasks))]
            await_time = beat - random_task.arrival
            abs_await_time = beat - random_task.abs_arrival

            self.sum_await_time += abs_await_time
            self.execute(random_task)
            self.x_await_time.append(await_time)
            self.y_tasks_amount.append(len(tasks) - 1)
            self.intervals.add(random_task.runtime)
        else:
            timeline = self.timeline[beat:len(self.timeline)]
            upcoming_tasks = [task for beat in timeline for task in beat]
            if len(upcoming_tasks):
                self.downtime += 1
            else:
                self.last_active_beat = beat


    def calculate_interval_probability(self):
        for interval in self.intervals:
            p = self.arrival_density * exp(-self.arrival_density * interval)
            self.y_interval_probability.append(p)
            self.x_interval_probability.append(interval)

    def calculate_tasks_per_unit_probability(self):
        for task in range(self.tasks_amount):
            p = (
                    ((self.arrival_density * TIME_UNIT) ** task) /
                    factorial(task)
                ) * exp(-self.arrival_density * TIME_UNIT)
            self.x_tasks_unit_probability.append(task)
            self.y_tasks_unit_probability.append(p)

    def start(self):
        for beat in range(1, self.beats + 1):
            if self.busy:
              self.busy -= 1
              continue
            else:
              self.pick_task(beat)

        self.calculate_interval_probability()
#         self.calculate_tasks_per_unit_probability()

        self.avg_await_time = self.sum_await_time / self.tasks_amount
        self.downtime_percent = (self.downtime / self.last_active_beat) * 100
