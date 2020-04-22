#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#List created from another list or iterator
def main():
    seq = range(11)
    print_list(seq)

    #create list compreension
    seq2 = [x * 2 for x in seq]
    print_list(seq2)

    seq2 = [x for x in seq if x % 3 != 0]
    print_list(seq2)

    #tuples with squares
    seq2 = [(x, x**2) for x in seq]
    print_list(seq2)

    from math import pi
    seq2 = [round(pi, i) for i in seq]
    print_list(seq2)

    #create a dictionary
    seq2 = {x: x**2 for x in seq}
    print(seq2)

    #create a set
    seq2 = {x for x in 'superduper' if x not in 'pd'}
    print_list(seq2)

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()
