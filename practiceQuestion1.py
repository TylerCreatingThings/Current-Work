'''
Created on Feb 6, 2016

@author: owner
'''

#print the reverse order of an array, seperated by single spaces.
def reverseString(a):
    n = len(a)-1
    back = ""
    for num in a:
        back = str(num) +" "+ back
    print(back)
       


#get a 6x6 2d array filled with integers, find the largest hourglass. 
#is it necessary to calculate all of them? 
#each integer is ranged -9 to 9
#Gotta calculate the sum of each hourglass
def hourGlass(a):
    row = len(a[0])
    col = len(a)
    sums = []
    
    
#Given a sorted array of integers A, find such an integer x that ∑(A[i] - x)2 over all i has the minimum possible value. If there are several possible answers, output the smallest one.    
def squaresSumMinimization(A):
    xsum = []
    sum = 0
    for y in range(0,len(A)-1):
        for x in range(0,len(A)-1):
            sum+=((A[x]-y)^2)
        xsum.append(sum)
        sum = 0
        
    min = 1000
    
    for x in range(len(xsum)):
        if(xsum[x]<min and xsum[x]>0):
            print(xsum[x])
            min = xsum[x]
    return min

#test reverse
a = {1,2,3,4,5,6}
print(a)
reverseString(a)

#test hourGlass
a = [[]]