class ClassExample():
    '''This first line is a summary of this class. \
There must be ONLY one logical line in this overview.
    
    However (notice that must be an empty line between the summary and this
    block of text), the rest of this doctrings can be placed in several lines.
    These lines usually provides extended information about the functionality
    of the class. The last line of the docstring should contain only
    three simple quotation marks.
    '''
    
    x = 1
    
    def __init__(self):
        '''A summary about the constructor. This is an example of a one-line docstring.'''
        print(self.x)
        
    def set(self, x: int) -> None:
        '''A summary about \"set\".
        
        Arguments:
            x: an integer that ... bla, bla, bla.
            
        Returns:
            Nothing.
        '''
        self.x = x
        
    def get(self) -> int:
        '''A summary about \"get\".
        
        Arguments:
            None.
            
        Returns:
            The value of \"x\".
        '''
        return self.x
