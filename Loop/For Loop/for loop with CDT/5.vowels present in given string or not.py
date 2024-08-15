s=input()
c=0
for i in s:
    if i in 'aeiouAeiou':
        c+=1
print(c)#o/p:2

#Execution
'''
1.taking input from the user
2.taking c variable with value 0 bcoz
   assuming that the given string might be empty
3.My user input is Vasavi
  iteration starts
iteration1: extracts V and check v in 'aeiouAEIOU'  condition false count is 0
iteration1: extracts a and check a in 'aeiouAEIOU' condition false count is 1
iteration1: extracts s and check s in 'aeiouAEIOU' condition true count is 1
iteration1: extracts a and check a in 'aeiouAEIOU' condition false count is 2
iteration1: extracts v and check v in 'aeiouAEIOU' condition false count is 2
iteration1: extracts i and check i in 'aeiouAEIOU' condition false count is 3
$.Prints c that value is "3"'''
