#!/usr/bin/env python
# encoding: utf-8

from distutils.core import setup

setup(name='webtrack',
    version='0.1.0',
    description='Keep track of updates from websites.',
    author='peterrr',
    url='https://github.com/peterr/webtrack/',
    install_requires=['lxml >= 3.0',
                      'cssselect'],
    packages=['webtrack'],
    scripts=['bin/webtrack']
)
