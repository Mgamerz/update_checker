#!/usr/bin/env python
import os
import re
from setuptools import setup

MODULE_NAME = 'update_checker'

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
VERSION = re.search("__version__ = '([^']+)'",
                    open('{0}.py'.format(MODULE_NAME)).read()).group(1)

setup(name=MODULE_NAME,
      author='Bryce Boe',
      author_email='bbzbryce@gmail.com',
      classifiers=['Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.1',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3'],
      description='A python module that will check for package updates.',
      install_requires=['requests>=1.0.2', 'setuptools'],
      license='Simplified BSD License',
      long_description=README,
      py_modules=[MODULE_NAME, '{0}_test'.format(MODULE_NAME)],
      test_suite='update_checker_test',
      url='https://github.com/bboe/update_checker',
      version=VERSION)
