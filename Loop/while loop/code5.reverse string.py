#WAP to reverse a string without using slicing

#By using slicing
s=input()
print(s[::-1])
#By using for loop one approach
#--------------------------------
s=input()
rev=''
for ip in range(-1, -(len(s)+1), -1):
    rev+=s[ip]
print(rev)

#Another Approach by for loop
#-----------------------------
s=input()
rev=''
for ch in s:
    rev=ch+rev
print(rev)

#By using while loop
#-------------------------
s=input()
rev=''
i=-1
while i>-(len(s)+1):
    rev+=s[i]
    i-=1
print(rev)


#EXecution
'''
1-> Taking input from the user
2-> Take rev as empty string
3-> take i=-1 as the 1st step for while loop we need to initialize a variable
4-> Now write the condition as checking till that conditions becomes false.
5-> taking input from the user as vasu
6-> Iteration starts
    Iteration1-> i=-1 checks the condition True rev+=s[i] here s[i] is "u" now u is added to
                 empty rev becomes "u" and i is decremented by -1 now i becomes -2
    Iteration2-> i=-2 checks the condition True rev+=s[i] here s[i] is "s" now s is added to
                 empty rev becomes "us" and i is decremented by -1 now i becomes -3
    Iteration3-> i=-3 checks the condition True rev+=s[i] here s[i] is "a" now a is added to
                 empty rev becomes "usa"and i is decremented by -1 now i becomes -4
    Iteration4-> i=-4 checks the condition True rev+=s[i] here s[i] is "v" now v is added to
                 empty rev becomes "usav"and i is decremented by -1 now i becomes -5
    Iteration5-> i=-5 checks the condition False doesnt enter in to the loop comes out from the loop
7-> print reverse string as "usav".
                
'''
