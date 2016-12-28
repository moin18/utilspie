utilspie : Utilities for Python
===============================

.. image:: https://img.shields.io/pypi/v/utilspie.svg
   :target: https://pypi.python.org/pypi/utilspie
   :alt: downloads

.. image:: https://travis-ci.org/moin18/utilspie.svg?branch=master
   :alt: build status
   :target: https://travis-ci.org/moin18/utilspie

.. image:: https://codecov.io/github/moin18/utilspie/coverage.svg?branch=master
   :target: https://codecov.io/github/moin18/utilspie
   :alt: codecov

.. image:: https://img.shields.io/badge/contributions-welcome-brightgreen.svg
   :target: https://github.com/moin18/utilspie/issues
   :alt: contributor-friendly

.. image:: https://img.shields.io/badge/docs-latest-brightgreen.svg
   :target: http://utilspie.readthedocs.io/en/latest
   :alt: documentation

Documentation: `utilspie.readthedocs.org <http://utilspie.readthedocs.io/en/latest/>`_
--------------------------------------------------------------------------------------

---------------------
What is **utilspie**?
---------------------
Utilspie is a Python library that offers a sensible, human-friendly utilities which do not come along with Python installation. Utilspie is categorized into 5 modules:

- asyncutils : utilities for asynchronous call/threads
- fileutils : utilities related to file operations/manipulations
- iterutils : utilities for iterators. Inspired by `itertools <https://docs.python.org/2/library/itertools.html>`_ package
- collectionsutils : provides data objects not present in `collections <https://docs.python.org/2/library/collections.html>`_ package
- importutils : utilities related to importing the modules

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

    from utilspie import iterutils
    # OR, from utilspie.iterutils import get_chunks

    iterutils.get_chunks([1, 2, 3, 4, 5, 6], 2)
    <generator object <genexpr> at 0x1018fab40>
    # returns generator object

    list(iterutils.get_chunks([1, 2, 3, 4, 5, 6], 2))
    [[1, 2], [3, 4], [5, 6]]


How to Contribute
-----------------

#. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
#. Fork `the repository`_ on GitHub to start making your changes to the **master** branch (or branch off of it).
#. Write a test which shows that the bug was fixed or that the feature works as expected.
#. Send a pull request and bug the maintainer until it gets merged and published. :) Make sure to add yourself to AUTHORS_.

.. _`the repository`: http://github.com/moin18/utilspie
.. _AUTHORS: https://github.com/moin18/utilspie/blob/master/AUTHORS.rst
