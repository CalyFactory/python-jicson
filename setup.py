#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup
from codecs import open
from os import path
import os


here = path.abspath(path.dirname(__file__))
readme_path = path.join(here, 'README.md')

long_description = 'See https://github.com/CalyFactory/python-jicson\n'


if path.exists(readme_path):
    with open(readme_path, encoding='utf-8') as f:
        long_description += f.read()

setup(
    name    = 'jicson', 
    version = '1.0.2', 
    packages=['jicson'],
    author = 'jspiner',
    author_email = 'jspiner@naver.com', 
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='ICS iCalendar JSon calendar caldav',
    url = 'http://caly.io',
    description = 'Easy ics file parser',
)