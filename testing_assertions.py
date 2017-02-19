def divide(a,b):
    assert(b>0), 'Error! (b == {})'.format(b)
    return a/b
    
try:
    print(divide(1,0))
except AssertionError as e:
    print(e)
    
try:
    print(divide(1,2))
except AssertionError as e:
    print(e)
