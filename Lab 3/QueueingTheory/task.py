from random import randint

TIME_UNIT = 10

class Task:
    def __init__(self, max_runtime):
        self.done = False
        self.arrival = randint(0, TIME_UNIT - 1)
        self.runtime = randint(1, max_runtime)

    def __str__(self):
        done = self.done
        arrival = self.arrival
        runtime = self.runtime
        return f'{{ arrival: {arrival}, runtime: {runtime}, done: {done} }}'
