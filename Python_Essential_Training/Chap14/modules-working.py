#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys
import os
import random as rm
import datetime as dt

def main():
    #v = sys.version_info
    # print('Python version {}.{}.{}'.format(*v))

    # v = sys.platform
    # print('Python version {}.{}.{}'.format(*v))

    # v = os.name
    # print(v)

    # v = os.getenv('PATH')
    # print(v)

    # #currently working directory
    # v = os.getcwd()
    # print(v)

    # #25 bites off
    # v = os.urandom(25).hex()
    # print(v)

    # x = rm.randint(1,1000)
    # print(x)

    # x = list(range(25))
    # print(x)
    # rm.shuffle(x)
    # print(x)

    now = dt.datetime.now()
    print(now)
    print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)


if __name__ == '__main__': main()
