"""Module to setup the library. All library dependencies are added here.
"""
import sys
from setuptools import setup, find_packages


print(find_packages(), file=sys.stderr)

setup(
    name='url-robots-checker',
    version='0.1.0',
    packages=find_packages(),
    python_requires='>= 3.6',
    install_requires=[
        'requests==2.24.0',
        'reppy==0.4.14'
    ]
)
