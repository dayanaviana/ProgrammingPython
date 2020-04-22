#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Animal:

    #variable not encapsulated
    #belongs to the class, not to the object
    x = [1, 2, 3]

    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'

    #encapsulation, variable belongs only to the object
    def type(self, t = None):
        if t: self._type = t
        return self._type

    def name(self, n = None):
        if n: self._name = n
        return self._name

    def sound(self, s = None):
        if s: self._sound = s
        return self._sound

    def __str__(self):
        #reads using the getter
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

def main():
    a0 = Animal(type = 'kitten', name = 'fluffy', sound = 'rwar')
    a1 = Animal(type = 'duck', name = 'donald', sound = 'quack')
    print(a0)
    print(a1)

    #variable not encapsulated
    #is defined/belongs to the class, not to the object
    print(a0.x)
    a1.x[0] = 7
    print(a0.x)


if __name__ == '__main__': main()
