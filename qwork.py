#!/usr/bin/env python

from __future__ import print_function

from multiprocessing import JoinableQueue, Process, cpu_count, current_process
from subprocess import check_call
import click

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


class Runner():
    def __init__(self, queue):
        self.queue = queue
        self.proc = Process(target=self.go)
        self.proc.start()

    def go(self):
        name = current_process().name
        while not self.queue.empty():
            command = self.queue.get()
            print("{} :: {}".format(name, command))
            check_call(command, shell=True)
            self.queue.task_done()


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('command_file', type=click.File('rb'))
@click.option('-n', '--nproc', type=int, default=cpu_count(),
              help='Number of processes to use.')
def qwork(command_file, nproc):
    """Queue up commands to run in parallel."""

    print("Queuing work using %d processes...\n" % nproc)
    queue = JoinableQueue()

    for command in command_file:
        queue.put(command.decode('utf8').rstrip('\n'))

    for ii in range(nproc):
        Runner(queue)

    queue.join()
    queue.close()

    print("\n...done!")


if __name__ == "__main__":
    qwork()
