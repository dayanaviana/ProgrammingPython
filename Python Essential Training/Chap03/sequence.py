#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# x = [ 1, 2, 3, 4, 5 ]
# x[2] = 42
# for i in x:
#     print('i is {}'.format(i))

# # Tuple object () is not mutable!
# x = ( 1, 2, 3, 4, 5 )
# x[2] = 42
# for i in x:
#     print('i is {}'.format(i))

# x = range(5)
# for i in x:
#     print('i is {}'.format(i))

# x = range(5, 10)
# for i in x:
#     print('i is {}'.format(i))

## We cannot reassign range
# x = range(5, 20, 2)
# x[2] = 42
# for i in x:
#     print('i is {}'.format(i))

# # SOLUTION
# x = list(range(5, 20, 2))
# x[2] = 42
# for i in x:
#     print('i is {}'.format(i))

# # Dictionary: Key Value pairs
# x = {"one":1, "two":2, "three":3, "four":4, "five":5, }
# for key in x:
#     print('key is {}'.format(key))

# x = {"one":1, "two":2, "three":3, "four":4, "five":5, }
# for key, value in x.items():
#     print('k:{}, v:{}'.format(key, value))

# Dictionaries are mutable
x = {"one":1, "two":2, "three":3, "four":4, "five":5, }
x["three"] = 42
for key, value in x.items():
    print('k:{}, v:{}'.format(key, value))