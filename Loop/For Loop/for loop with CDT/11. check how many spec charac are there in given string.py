#Check how many special characters are present in given string
s=input()
c=0
for i in s:
   if not i.isalnum():
       c+=1
print(c)

#execution
'''
1-> Take input from the user
2-> take c=0 assuming that there is no special characters in given string
3-> Taking input as @12$V_
4-> Iteration starts
    Iteration1: Extracts @ and checks condition True count becomes 1
    Iteration2: Extracts 1 and checks condition False count remains 1
    Iteration3: Extracts 2 and checks condition False count remains 1
    Iteration4: Extracts $ and checks condition True count becomes 2
    Iteration5: Extracts V and checks condition False count remains 2
    Iteration6: Extracts _ and checks condition True count becomes 3
5-> Prints special charac count 3'''
