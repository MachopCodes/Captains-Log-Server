"""Sets up the package"""

#!/usr/bin/env python
 # -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    README = f.read()

with open('LICENSE.md') as f:
    LICENSE = f.read()

setup(
    name='nautical_trip_planner',
    version='0.1.0',
    description='Trip Planner for Nautical Events',
    long_description=README,
    author='Will Andreae',
    author_email='wcandreae@gmail.com',
    url='https://github.com/MachopCodes/Nautical-Trip-Planner-Server',
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs'))
)
