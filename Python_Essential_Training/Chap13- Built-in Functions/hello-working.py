#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# s = 'Hello, World.'
# #print a string representation
# print(repr(s))

class bunny:
    def __init__(self, n):
        self.__n = n
    def __repr__(self):
        return f"repr: The number of bunnies is {self.__n} 😄 " 
    def __str__(self):
        return f"str: The number of bunnies is {self.__n}"

s = bunny(47)
print(s)
print(repr(s))
#does not show emoticons
print(ascii(s))

print(chr(128516))
print(ord('😄'))