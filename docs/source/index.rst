===============================
Utilspie:  Utilities for Python
===============================

-----------------
What is utilspie?
-----------------
Utilspie is a Python library that offers a sensible, human-friendly utilities which do not come along with Python installation. Utilspie is categorized into 5 modules:

- `asyncutils <http://utilspie.readthedocs.io/en/latest/#utilspie-asyncutils>`_: utilities for asynchronous call/threads
- `fileutils <http://utilspie.readthedocs.io/en/latest/#utilspie-fileutils>`_: utilities related to file operations/manipulations
- `iterutils <http://utilspie.readthedocs.io/en/latest/#utilspie-iterutils>`_: utilities for iterators. Inspired by `itertools <https://docs.python.org/2/library/itertools.html>`_ package
- `collectionsutils <http://utilspie.readthedocs.io/en/latest/#utilspie-collectionsutils>`_: provides data objects not present in `collections <https://docs.python.org/2/library/collections.html>`_ package
- `importutils <http://utilspie.readthedocs.io/en/latest/#utilspie-importutils>`_: utilities related to importing the modules

------------
Installation
------------
**utilspie** is available on `pypi <https://pypi.python.org/pypi/utilspie>`_. To install, run:

.. code-block:: bash

    $ pip install utilspie

Source code for utilspie is available on `github <https://github.com/moin18/utilspie>`_

-----------
Quick Start
-----------
For using the utilspie, you have to import the package utilspie and call it's function as:

.. code-block:: python

   >>> from utilspie import iterutils
   # OR, from utilspie.iterutils import get_chunks

   >>> iterutils.get_chunks([1, 2, 3, 4, 5, 6], 2)
   <generator object <genexpr> at 0x1018fab40>
   # returns generator object

   >>> list(iterutils.get_chunks([1, 2, 3, 4, 5, 6], 2))
   [[1, 2], [3, 4], [5, 6]]


---------
API Guide
---------

utilspie.asyncutils
===================
Contains utility functions for asynchronous calls.

ordered_async_call
------------------
**ordered_async_call(function_list)**: Asynchronously executes the list of passed functions, and return the ``['list', 'of', 'values']`` returned by each function.
Values returned are in the order in which functions are passed through ``function_list``. ``function_list`` should be of the format:
``[(function_1, args_1, kwargs_1), (function_2, args_2, kwargs_2), ...]``. For example:

.. code-block:: python

    >>> from utilspie import asyncutils
    >>> def foo(x, y):
    ...     return x + y
    ...
    >>> func_list = [(foo, [0], {'y': 5}), (foo, [8, 9], {}), (foo, [], {'x': 77, 'y': 4})]

    >>> asyncutils.ordered_async_call(func_list)
    [5, 17, 81]


utilspie.fileutils
==================
Contains utility functions for files related operations.

copy_file
---------
**copy_file(source, destination, unique=False, sort=False, case_sensitive=True, create_path=False)**: Copy file from ``source`` path to ``destination`` path.
It has 4 optional params:

- **unique**: Copy unique lines of file. Default: ``False``
- **sort**: Copy sorted content of the file. Default: ``False``
- **case_sensitive**: Do *unique*/*sort* on case-sensitive content. Default: ``True``
- **create_path**: Create directory to destination file, in case not exists. Default: ``False``

Sample example:

.. code-block:: python

    >>> from utilspie import fileutils

    >>> fileutils.copy_file(
    ...     source='/tmp/path/to/source.txt',
    ...     destination='/tmp/path/to/destination.txt',
    ...     unique=True,
    ...     sort=True,
    ...     case_sensitive=False,
    ...     create_path=True)

utilspie.iterutils
==================
Contains utility functions for iterables. It is inspired by **itertools** package.

get_chunks
----------
**get_chunks(iterable_obj, chunk_size=1)**: Receives the iterable object ``iterable_obj`` and divides the object in evenly
sized chunks of size ``chunk_size``. Default value of ``chunk_size=1``. For example:

.. code-block:: python

   >>> from utilspie import iterutils

   >>> iterutils.get_chunks([1, 2, 3, 4, 5, 6], 2)
   <generator object <genexpr> at 0x1018fab40>
   # returns generator object

   >>> list(iterutils.get_chunks([1, 2, 3, 4, 5, 6], 2))
   [[1, 2], [3, 4], [5, 6]]


utilspie.collectionsutils
=========================
Contains additional data objects not available as in-built in Python. This is inspired by **collections** module.

frozendict
----------
**frozendict(dict_obj)**: Accepts obj of ``dict`` type and returns a hashable and immutable ``dict``. For example:

.. code-block:: python

    >>> from utilspie import collectionsutils

    >>> my_dict = collectionsutils.frozendict({1: 2, 3: 4})
    >>> my_dict   # 'frozendict' type object
    frozendict({1: 2, 3: 4})

    >>> {my_dict: 3}   # could be used as a 'key' to dict
    {frozendict({1: 2, 3: 4}): 3}

utilspie.importutils
====================

.. currentmodule:: import_utils
.. autofunction:: delete_module


.. currentmodule:: import_utils
.. autofunction:: reload_module

