#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def f1():
    print('this is f1')

x = f1
x()
#----------------------------------------------
def f1():
    def f2():
        print('this is f2')
    return f2

x = f1()
x
#----------------------------------------------

#decorator!
def f1(f):
    def f2():
        print('this is before the function call')
        f()
        print('this is after the function call')
    return f2

def f3():
    print('this is f3')

x = f1(f3)
x()
#----------------------------------------
def f1(f):
    def f2():
        print('this is before the function call')
        f()
        print('this is after the function call')
    return f2
#locks function to be used outside f1
@f1
def f3():
    print('this is f3')

f3()