#print max number in the given list
L=[1,2,25,3,4]
mx=0
for i in L:
    if i>mx:
        mx=i
print(mx)

#Execution
'''
1-> Take input from the user
2-> take mx=0 assuming that there is no greater num in a given list.
3-> Taking input as [1, 2,'hai',3]
4-> Iteration starts
    Iteration1: Extract 1 and checks condition true mx is 1
    Iteration2: Extract 2 and checks condition true mx is 2
    Iteration3: Extract 25 and checks condition true mx is 25
    Iteration4: Extract 3 and checks condition true mx remains 25
    Iteration5: Extract 4 and checks condition true mx remains 25
5-> Prints max number as 25'''

# by using max funtion
'''L=[1,2,25,3,4]
print(max(L))
    
#by using sort method and indexing
L=[1,2,25,3,4]
L.sort()
print(L[-1])'''
