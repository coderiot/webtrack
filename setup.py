#!/usr/bin/env python
# encoding: utf-8

from distutils.core import setup

setup(name='webtrack',
    version='0.1.0',
    license="GPLv2",
    description='Keep track of updates from websites.',
    author='peterrr',
    url='https://github.com/peterr/webtrack/',
    install_requires=['lxml >= 3.0',
                      'cssselect'],
    packages=['webtrack'],
    entry_points="""
        [console_scripts]
        webtrack = webtrack.feed:main
    """
)
