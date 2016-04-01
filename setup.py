from setuptools import setup
from os import path
# Get a handle on where we're at :)
here = path.abspath(path.dirname(__file__))

setup(
    name='passer',
    version='0.0.2',
    author='Alex Caudill',
    author_email='hypoalex@users.noreply.github.com',
    url='https://github.com/hypoalex/passer',
    description='A Python 3.5 implementation of the Sparrow scheduler',
    packages=['passer', 'passer.proto', 'passer.daemon'],
    platforms="Linux, Mac OS X",
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    entry_points = {
     'console_scripts': [
      'passerd = passer.daemon:main',
     ],
    }
)
