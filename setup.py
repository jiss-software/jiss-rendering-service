#!/usr/bin/env python

from setuptools import setup

setup(
    name='JissRenderingService',
    description='Service for operations on files.',
    version='1.0',
    author='Anton Iskov',
    author_email='aiskov@jiss-software.com',
    url='http://www.jiss-software.com',
    packages=[
        'core',
        'handler',
        'utils'
    ],
    install_requires=[
        'tornado==4.2.1',
        'Pillow'
    ]
)
