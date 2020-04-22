#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#login example

secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 5

while pw != secret:
    count += 1
    if count > max_attempt : break
    #skip the execution of the body when is 3
    if count == 3 : continue
    pw = input(f"{count}: What's the secret word? ")
# executes if while loop executes
else:
    auth = True

print("Authorized" if auth else "Caling the FBI!")