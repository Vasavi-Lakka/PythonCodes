s=input()
c=0
for i in s:
    if i.isdigit():
        c+=1
print(c)

#Execution
'''
1.taking input from the user
2.taking c variable with value 0 bcoz
   assuming that the given string might be empty
3.My user input is Vasu123
  iteration starts
iteration1: extracts V and check v isdigit or not condition false count c becomes 0
iteration2: extracts a and check a isdigit or not condition false count c becomes 0
iteration3: extracts s and check s isdigit or not condition false count c becomes 0 
iteration4: extracts u and check a isdigit or not condition false count c becomes 0
iteration5: extracts 1 and check 1 isdigit or not condition true count c becomes 1
iteration6: extracts 2 and check 2 isdigit or not condition true count c becomes 2
iteration7: extracts 3 and check 3 isdigit or not condition true count c becomes 3

5.prints c is 3'''
