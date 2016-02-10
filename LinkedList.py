'''
Created on Feb 6, 2016

@author: owner
'''


class LinkedList(object):
    '''
    Normal Linked list, 1 value.
    '''
    head = None
    
    class Node(object):
        nextVal = None
        val = 0
        def __init__(self,val,nextVal):
              self.val = val
              self.nextVal = nextVal
    
    
    def __init__(self,val):
        self.head = self.Node(val,None)
    def insert(self):
        pass
    def insertBefore(self):
        pass
    def traverse(self):
        pass
    def search(self):
        pass
    