#.WAP to check how many times the given sub_string present in given string
s=input()
sub_s=input()
c_sub=0
for ip in range(len(s)):
    if s[ip:ip+len(sub_s):]==sub_s:
        c_sub+=1
print(c_sub)


#Execution
'''
1-> Take string as an input.
2-> Take sub string as an input.
3-> As we are dealing with index we are going to use for with range and  CDT.
4-> 
5-> 
6-> 
7-> '''


