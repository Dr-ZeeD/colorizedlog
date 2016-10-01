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

setup(
    name='colorizedlog',
    version=version,
    author='Dominik Steinberger',
    url='https://github.com/ZeeD26/colorizedlog',
    py_modules=[
        'colorizedlog'
    ],
    license='BSD')
