#!/usr/bin/env python

from multiprocessing import JoinableQueue, Process, cpu_count
from subprocess import check_call
import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


class Runner():
    def __init__(self, queue):
        self.queue = queue
        self.proc = Process(target=self.go)
        self.proc.start()

    def go(self):
        while not self.queue.empty():
            command = self.queue.get()
            print(command)
            check_call(command, shell=True)
            self.queue.task_done()


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('command_file', type=click.File('rb'))
@click.option('-n', '--nproc', type=int, default=cpu_count(),
              help='Number of processes to use.')
def queue_work(command_file, nproc):
    """Queue up commands to run in parallel."""
    print("Queuing work using %d processes...\n" % nproc)
    queue = JoinableQueue()

    for command in command_file:
        queue.put(command.decode('utf8').rstrip('\n'))

    for ii in range(nproc):
        Runner(queue)

    queue.join()
    print("\n...done!")


if __name__ == "__main__":
    queue_work()
