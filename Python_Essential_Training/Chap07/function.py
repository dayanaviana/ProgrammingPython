#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    #integer is not mutable
    x = 5
    kitten(x,6,7)
    # python passes the value/copy, not the variable id
    print(f'in main x is {x}')

    #for mutable objects we pass reference
    list1 = [5]
    list2 = list1
    list2[0] = 3
    print(id(list1))
    print(id(list2))
    print(list1)
    print(list2)



#has default values
def kitten(n, b, c = 0):
    n = 3
    print(f'{n} Meow.')
    print(b, c)

#__name__ print the name of the module
if __name__ == '__main__': main()


