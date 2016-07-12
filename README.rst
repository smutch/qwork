Qwork
=====


    Queue up commands to run in parallel.

Sometimes you just want to run a series of independent shell commands as quickly
as possible. **Qwork** allows you do do just that as simply as possible.

*There probably exists many other (more complete) options for this task.
However, this simple code meets my needs 99% of the time.*

* Free software: MIT license


Usage
-----

.. code-block:: sh

    qwork [OPTIONS] COMMAND_FILE
    
    Options:
      -n, --nproc INTEGER  Number of processes to use.
      -h, --help           Show this message and exit.


Examples
--------

Reading commands from file
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: sh

    for p in {1..10}; do echo 'echo do this' $p >>! temp.txt; done
    qwork -n 2 temp.txt


Reading commands from stdin
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: sh

    for p in {1..10}; do echo 'echo do this' $p; done | qwork -n 2 -


Credits
-------

Code written by Simon Mutch (smutch).

This package was created with Cookiecutter_ and the 
`audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
