'''
Created on Feb 3, 2016

@author: owner
'''


#pass by reference
x1 = [[]]*5
x1[0].append("object")
print(x1)


#append adds a new index to the list.
x = [[]]*5
x.append("object")
print (x)

print(len(x))

#if statement syntax
count = 5
if(count>5):
    count+=1
elif(count<5):
    count-=1
else:
    count = count*2
print("This is the count "+ str(count))

#String Manipulation
practice = "If I give you my numbah you gottah be able to get it 416-735-3336"

print(practice.count("3"))
print(practice.split(sep=" "))

#not None = Null
x = not None
if(x):
    print("Woah")
else:
    print("Told you so.")
    
#for loops syntax
numbers = [1,2,3,4,5]

for num in numbers:
    print("Current Number: " + num)

for num in range(0,len(numbers)):
    print(num)
    
#while loop syntax
palm = False
k = 22
while palm==False:
    if(k%3==0):
        palm = True
    else:
        k-=1
        

    
    
