#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    #t for text mode, even though it is default
    infile = open('lines.txt', 'rt')
    outfile = open('lines-copy.txt', 'wt')
    for line in infile:
        #I can strip and change the line enddings
        #print(line.rstrip(), file=outfile)
        outfile.writelines(line)
        # print dot's for each line of the file
        #end "" prevent from reading a new line after each dot 
        print('.', end='', flush=True)
        #flush = output buffer, Do (not?) print until read new line 
    outfile.close()
    infile.close()
    print('\ndone.')

if __name__ == '__main__': main()
