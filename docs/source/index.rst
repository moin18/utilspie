===============================
Utilspie:  Utilities for Python
===============================

-----
What?
-----
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



utilspie.fileutils
==================



utilspie.iterutils
==================


utilspie.collectionsutils
=========================


utilspie.importutils
====================

