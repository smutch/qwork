# Qwork

> Queue up commands to run in parallel.

Sometimes you just want to run a series of independent shell commands as quickly
as possible. **Qwork** allows you do do just that as simply as possible.

*There probably exists many other (more complete) options for this task.
However, this simple code meets my needs 99% of the time.*

## Usage

    queue-work [OPTIONS] COMMAND_FILE
    
    Options:
      -n, --nproc INTEGER  Number of processes to use.
      -h, --help           Show this message and exit.


## Examples

### Reading commands from file

``` sh
for p in {1..10}; do echo 'echo do this' $p >>! temp.txt; done
queue-work -n 2 temp.txt
```

### Reading commands from stdin

``` sh
for p in {1..10}; do echo 'echo do this' $p; done | queue-work -n 2 -
```
