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

   # returns generator object
   >>> iterutils.get_chunks([1, 2, 3, 4, 5, 6], 2)
   <generator object <genexpr> at 0x1018fab40>

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
    >>> func_list = [
    ...     (foo, [0], {'y': 5}),
    ...     (foo, [8, 9], {}),
    ...     (foo, [], {'x': 77, 'y': 4})]

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


swap_dict
---------
**swap_dict(dict_obj, multivalued=True)**: Swaps the *(key, value)* pair of ``dict`` to the *(value, key)* pair. If
``multivalued`` is set as ``True``, returns the *value* of dict as ``list`` of *key* in original dict. If ``multivalued`` is
set as ``False``, returns the single *key* as *value* discarding the duplicates. Default value of ``multivalued=True``.
For example:

.. code-block:: python

    >>> from utilspie import collectionsutils

    # multivalued `True`
    >>> collectionsutils.swap_dict({1: 2, 3: 2})
    {2: [1, 3]}

    # multivalued `False`
    >>> collectionsutils.swap_dict({1: 2, 3: 2},
    ...                     multivalued=False)
    {2: 3}


utilspie.importutils
====================
Utilities related to importing the modules.


lazy_load_modules
-----------------
**lazy_load_modules(*modules)**: is a decorator which could be used over functions to use modules within function
which you do not want to reside in *sys.modules*. Ideal for using modules that uses too much system's memory and are
not frequently used. For example:

.. code-block:: python

    >>> from utilspie import importutils

    >>> @importutils.lazy_load_modules('idna', 'some_other_module')
    ... def foo(x, y):
    ...     import idna, some_other_module
    ...     # Do somethings return
    ...

    >>> foo(1, 2)
    # 'idna' and 'some_other_module' won't be
    # available outside the function


**Note**: The module you are passing to ``lazy_load_modules`` should not contain any reference outside the decorated function.
In case any reference exist, *garbage-collector* will fail to free the memory.

reload_module
-------------
**reload_module(module)**: It reloads a previously imported module. It is based on `reload <https://docs.python.org/2/library/functions.html#reload>`_
in Python2.x, `imp.reload <https://docs.python.org/3/library/imp.html#imp.reload>`_ in <= Python 3.3 and `importlib.reload <https://docs.python.org/3/library/importlib.html#importlib.reload>`_
in Python >= 3.3. But this *reload_module()* is compatible with all Python verisons.

.. code-block:: python

    >>> from utilspie import importutils

    >>> importutils.reload('my.module')


delete_module
-------------
**delete_module(modname)**: It deletes the entry of ``modname`` module from  ``sys.modules`` dict. The memory will be later freed
by *garbage-collector* only if there do not exists any reference to that module.

.. code-block:: python

    >>> from utilspie import importutils

    >>> importutils.delete_module('my.module')


--------------------------
Didn't find what you want?
--------------------------
Are you looking for something which you think should be the part of *utilspie* but is not currently present? Feel free to mention it by
opening a `issue <https://github.com/moin18/utilspie/issues>`_. We will take a look at it, and will implement it if it's a good fit.
