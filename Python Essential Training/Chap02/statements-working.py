#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#statement
import platform

#expression
version = platform.python_version()

#statement and expression
print('This is python version {}'.format(version))

#it's unusual to write more than one statement per line
print("Hello "); print("You!")
