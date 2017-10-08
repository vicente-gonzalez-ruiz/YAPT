#!/usr/bin/env python3

import sys
from IPython.core import ultratb
sys.excepthook = ultratb.FormattedTB(mode='Verbose', color_scheme='Linux', call_pdb=1)

def call_me():
    print("Debug me with \"python -i debug_me.py\"")
    print("After the run-time error, you should have access to the \"a\" variable")
    a=1
    c=0
    import ipdb; ipdb.set_trace()
    d=1/c
    print("This code is never reached")
    a=2

b=1

call_me()
