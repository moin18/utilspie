#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import codecs

from setuptools import setup

try:
    # Python 3
    from os import dirname
except ImportError:
    # Python 2
    from os.path import dirname

here = os.path.abspath(dirname(__file__))

def read(*parts):
    return codecs.open(os.path.join(here, *parts), 'r').read()

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel upload")
    sys.exit()

# List of required libraries
required = [
]

setup(
    name='utilspie',
    version='0.0.1',
    description='Utilities for Python Developers',
    long_description= '\n' + read('README.rst'),
    author='Moinuddin Quadri',
    author_email='moin18@gmail.com',
    url='https://github.com/moin18/utilspie',
    py_modules=['utilspie'],
    install_requires=required,
    license='MIT',
    classifiers=(

    ),
)
