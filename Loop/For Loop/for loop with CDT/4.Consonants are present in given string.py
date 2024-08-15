V='aeiouAEIOU'
s=input()
c=0
for i in s:
    if i.isalpha() and i not in V:
        c+=1
print(c)

#Execution
'''
1.taking input from the user
2.taking c variable with value 0 bcoz
   assuming that the given string might be empty
3.My user input is Vasavi
  iteration starts
iteration1: extracts V and check v isalpha and not in 'aeiouAEIOU'  condition true count is 1
iteration2: extracts a and check a isalpha and not in 'aeiouAEIOU' condition false count is 1
iteration3: extracts s and check s isalpha and not in 'aeiouAEIOU' condition true count is 2
iteration4: extracts a and check a isalpha and not in 'aeiouAEIOU' condition false count is 2
iteration5: extracts v and check v isalpha and not in 'aeiouAEIOU' condition true count is 3
iteration6: extracts i and check i isalpha and not in 'aeiouAEIOU' condition false count is 3
$.Prints c that value is "3" '''
