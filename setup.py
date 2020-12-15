#!/usr/bin/env python
from setuptools import setup, find_packages
from distutils.core import setup

setup(name='Distutils',
      version='1.0',
      description='TSP Service',
      author='Charanjeet Singh',
      author_email='charan678@hotmail.com',
      packages=['tspapp', 'tspapp.consumer', 'tspapp.consumer.tsp', 'tspapp.publish', 'tspapp.queue'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      )