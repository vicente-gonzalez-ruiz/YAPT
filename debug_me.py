#!/usr/bin/env python3

#import pydb, sys
#sys.excepthook = pydb.exception_hook

def call_me():
    print("Debug me with \"python -i debug_me.py\"")
    print("After the run-time error, you should have access to the \"a\" variable")
    a=1
    c=0
    d=1/c
    print("This code is never reached")
    a=2

b=1

call_me()
