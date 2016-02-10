'''
Created on Feb 6, 2016

@author: owner
'''

class Queue(object):
    '''
    Queue is First in first out. It's like waiting in line to grab your ticket.
    
    '''
    a = []

    def __init__(self):
        pass
    
    def isEmpty(self):
        return len(self.a) == 0
    
    def Enqueue(self, val):
        self.a.append(val)
        pass
    
    def Dequeue(self):
        if(self.isEmpty() == False):
            x = self.a[0]
            self.a.remove(x)
            return x
        else:
            return None