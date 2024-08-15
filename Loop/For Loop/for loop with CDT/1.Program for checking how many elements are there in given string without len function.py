#WAP to check how many elements are there
#in the given string with out using the len function
s=input()
c=0
for i in s:
    c+=1
print(c)#returns 6 as a ouput

#Execution
'''
1.taking input from the user
2.taking c variable with value 0 bcoz
   assuming that the given string might be empty
3.My user input is Vasavi
  iteration starts
iteration1: extracts V and check add 1 to c, c becomes 1
iteration1: extracts a and check add 1 to c, c becomes 2
iteration1: extracts s and check add 1 to c, c becomes 3
iteration1: extracts a and check add 1 to c, c becomes 4
iteration1: extracts v and check add 1 to c, c becomes 5
iteration1: extracts i and check add 1 to c, c becomes 6
$.Prints c that value is "6"'''

s=input()
c=0
for i in s:
    c+=1
    print(c)'''gives out put as
                1
                2
                3
                4
                5
                6'''
