#WAP to check how many times the given sub string is present in the given string
s=input()
sub=input()
c=0
for i in s:
    if i == sub:
        c+=1
print(c)

#Execution
'''
1.taking input from the user
2.taking c variable with value 0 bcoz
   assuming that the given string might be empty
3.My user input is Vasavi
                sub string a
  iteration starts

  iteration1: extracts V and check 'a'=='V' condition False c remains 0:
  iteration2: extracts a and check 'a'=='a' condition True c becomes 1:
  iteration1: extracts s and check 'a'=='s' condition False c remains 1:
  iteration1: extracts a and check 'a'=='a' condition True c becomes 2:
  iteration1: extracts V and check 'a'=='V' condition false c remains 2: 
  iteration1: extracts i and check 'a'=='i' condition false c remains 2: 
  
4.Prints c that value is "2"'''
