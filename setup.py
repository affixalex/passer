# https://github.com/pypa/sampleproject/blob/master/setup.py

# Always prefer setuptools over distutils
from setuptools import setup
from os import path
# Get a handle on where we're at :)
here = path.abspath(path.dirname(__file__))

setup(
    name = 'passer',
    version = '0.0.1',
    author = 'Alex Caudill',
    author_email = 'nobody@nowhere.io',
    url = 'https://github.com/hypoalex/passer',
    description = 'A Python 3.5 implementation of the Sparrow scheduler',
    packages=['passer', 'passer.proto', 'passer.daemon'],
)