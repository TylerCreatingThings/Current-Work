'''
Created on Feb 6, 2016

@author: owner
'''

class Stack(object):
    '''
    Stack is last in first out. Like taking a pringle out of a container
    '''
    a = []

    def __init__(self, params):
        pass
        
    def isEmpty(self):
        return len(self.a) == 0
    
    def push(self, val):
        self.a.append(val);
        pass
    
    def pop(self):
        if(self.isEmpty()):
            return self.a.pop()
        else:
            return None