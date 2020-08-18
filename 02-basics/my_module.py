#!/usr/bin/env python

a = 1
print("my_module.py: Hi from " + __name__ + ".py!")

if __name__ == "__main__":
  print("my_module.py: I was invoked from a script.")
else:
  print("my_module.py: I was invoked from a Python module (probably using 'import').")
print("my_module.py: My name is =", __name__)
