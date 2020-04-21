import sys
from queue import *
from graph import *


help = """Commands:
            - exit: exit CLI
            - <number of graph>: select plot to build

Available graphs:
            1. plot of probability of interval's between task processing versus interval
            2. plot of tasks amount versus awaiting time
            3. plot of average awaiting time versus arrival rate
            4. plot of percent of downtime versus arrival rate
            5. plot of tasks per unit probability versus tasks_amount
"""

def emulation_params():
    tasks_amount = input('Enter tasks amount: ')
    arrival_rate = input('Enter arrival rate: ')
    max_runtime = input('Enter max task runtime: ')
    return tasks_amount, arrival_rate, max_runtime

def cli():
    print(help)

    while True:
        command = input('Enter command: ')

        if command == 'exit':
            return

        elif command == '1':
            graph = Graph()
            graph.title("Probability of interval's between task processing versus interval")
            graph.y_label('Probability p(t)')
            graph.x_label('Interval t')

            tasks_amount, arrival_rate, max_runtime = emulation_params()
            queue = Queue(int(tasks_amount), int(arrival_rate), int(max_runtime))

            queue.init_timeline()
            queue.start()

            for i in range(len(queue.x_interval_probability)):
                graph.set_values(
                    queue.x_interval_probability[i],
                    queue.y_interval_probability[i]
                )

            graph.show()

        elif command == '2':
            graph = Graph()
            graph.title("Tasks amount versus awaiting time")
            graph.y_label('Tasks amount')
            graph.x_label('Awaiting time')

            tasks_amount, arrival_rate, max_runtime = emulation_params()
            queue = Queue(int(tasks_amount), int(arrival_rate), int(max_runtime))

            queue.init_timeline()
            queue.start()

            for i in range(len(queue.x_await_time)):
                graph.set_values(queue.x_await_time[i], queue.y_tasks_amount[i])

            graph.show(True)
#             graph.show_hist(queue.x_await_time)

        elif command == '3':
            graph = Graph()
            graph.title("Average awaiting time versus arrival rate")
            graph.y_label('Average awaiting time')
            graph.x_label('Arrival rate (tasks per 10 beats)')

            tasks_amount = input('Enter tasks amount: ')
            min_rate = input('Enter min arrival rate: ')
            max_rate = input('Enter max arrival rate: ')
            max_runtime = input('Enter max task runtime: ')

            for rate in range(int(min_rate), int(max_rate) + 1):
                queue = Queue(int(tasks_amount), rate, int(max_runtime))

                queue.init_timeline()
                queue.start()
                graph.set_values(rate, queue.avg_await_time)

            graph.show()

        elif command == '4':
            graph = Graph()
            graph.title("Percent of downtime versus arrival rate")
            graph.y_label('Percent of downtime')
            graph.x_label('Arrival rate')

            tasks_amount = input('Enter tasks amount: ')
            min_rate = input('Enter min arrival rate: ')
            max_rate = input('Enter max arrival rate: ')
            max_runtime = input('Enter max task runtime: ')

            for rate in range(int(min_rate), int(max_rate) + 1):
                queue = Queue(int(tasks_amount), rate, int(max_runtime))

                queue.init_timeline()
                queue.start()
                graph.set_values(rate, queue.downtime_percent)

            graph.show()

        elif command == '5':
            graph = Graph()
            graph.title("Tasks per unit probability versus tasks amount")
            graph.y_label('Tasks per unit probability')
            graph.x_label('Tasks amount')

            tasks_amount, arrival_rate, max_runtime = emulation_params()
            queue = Queue(int(tasks_amount), int(arrival_rate), int(max_runtime))

            queue.init_timeline()
            queue.start()

            for i in range(len(queue.x_tasks_unit_probability)):
                graph.set_values(
                    queue.x_tasks_unit_probability[i],
                    queue.y_tasks_unit_probability[i]
                )

            graph.show(True)

cli()
