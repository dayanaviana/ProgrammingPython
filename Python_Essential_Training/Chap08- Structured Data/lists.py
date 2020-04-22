#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    #not mutable!
    game_tuple = ('Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' )
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    print(game[1])
    #slice: not inclusive
    print(game[1:3])
    #add steps
    print(game[1:3:5])
    #search itens
    i = game.index('Paper')
    print(i)
    #mutable!
    game.append('Computer')
    # insert by index
    game.insert(0,'Obj')
    #remove by value
    game.remove('Paper')
    #remove from the end and return
    game.pop()
    game.pop(3)
    #delete
    del game[3]
    #delete by slice
    del game[1:3]
    #join
    print(', '.join(game))

    len(game)


    print_list(game)
   

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()
