#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
        'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    print_dict(animals)

    # animals_dict = dict(kitten= 'meow', puppy='ruff!', lion='grrr', giraffe='I am a giraffe!', dragon='rawr' )
    # print_dict(animals)

    # for k, v in animals.items():
    #     print(f'{k}: {v}')

    for v in animals.values() : print(v)

    for k in animals.keys() : print(k)

    print(animals['lion'])

    animals['lion'] = 'grrrrrrrr'

    animals['monkey'] = 'uu-ha-ha'
    
    print('lion' in animals)

    print('Found' if 'godzilla' in animals else 'nope!')

    #Trow exception: error
    print(animals['godzilla'])

    #return None
    print(animals.get('godzilla'))


def print_dict(o):
    for k, v in o.items(): print(f'{k}: {v}')

if __name__ == '__main__': main()
