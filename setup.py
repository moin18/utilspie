#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

required = [
]

packages = [
    'utilspie',
    'utilspie.asyncutils',
    'utilspie.importutils',
    'utilspie.fileutils'
]

setup(
    name='utilspie',
    version='0.0.4',
    description='Python Utilities',
    long_description=long_description,
    url='https://github.com/moin18/utilspie',
    author='Moinuddin Quadri',
    author_email='moin18@gmail.com',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='utils asyncutils importutils fileutils import file async',
    packages=packages,
    install_requires=required,
)
