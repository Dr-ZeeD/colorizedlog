#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup
import re
import ast

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

_version_re = re.compile(r'__version__\s+=\s+(.*)')
with open(os.path.join(root_dir, 'colorizedlog.py'), 'r') as f:
    version = str(ast.literal_eval(_version_re.search(f.read()).group(1)))

description = "Replacement for logging.StreamHandler with colors."

setup(
    name='colorizedlog',
    version=version,
    description=description,
    long_description=long_description,
    author='Dominik Steinberger',
    url='https://github.com/ZeeD26/colorizedlog',
    py_modules=[
        'colorizedlog'
    ],
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: System :: Logging'
    ])
