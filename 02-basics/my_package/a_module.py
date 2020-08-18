a = 1
print("a_module: Hi from my_package/" + __name__ + ".py!")

if __name__ == "__main__":
  print("a_module: I was invoked from a script.")
else:
  print("a_module: I was invoked from a Pyton module (probably using 'import').") 
print("a_module: My name is =", __name__)
