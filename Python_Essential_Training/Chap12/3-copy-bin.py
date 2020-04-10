#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    # b for binary file
    infile = open('berlin.jpg', 'rb')
    outfile = open('berlin-copy.jpg', 'wb')
    while True:
        #buffer full 10k - small
        #chunk size you're reading at a time
        buf = infile.read(10240)
        if buf:
            outfile.write(buf)
            print('\n.', end='', flush=True)
        else: break
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()
