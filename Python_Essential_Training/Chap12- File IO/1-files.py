#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    # r : default, read mode
    # w: write mode, if do not exist create it
    # a: append, starts at the end of the file. does not creat
    # b or t: binary or text mode
    f = open('lines.txt')
    for line in f:
        print(line.rstrip())

if __name__ == '__main__': main()
