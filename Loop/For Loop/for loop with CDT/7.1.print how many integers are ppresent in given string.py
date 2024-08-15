s=input()
c=0
for i in s:
    if i.isdigit():
        c+=1
print(c)

#Execution
'''1-> Taking input from the user
2-> taking count is 0 assuming that there is no integer value in the given string
3-> Taking input as V1a2s3u4
4-> Iterationn starts
    iteration1: extracts V checks the condition false count c remains 0
    Iteration2: extracts 1 checks the condition True count c becomes 1
    iteration3: extracts a checks the condition false count c remains 1
    Iteration4: extracts 2 checks the condition True count c becomes 2
    iteration5: extracts s checks the condition false count c remains 2
    Iteration6: extracts 3 checks the condition True count c becomes 3
    iteration7: extracts u checks the condition false count c remains 3
    Iteration8: extracts 4 checks the condition True count c becomes 4
5-> Prints count as 4'''
