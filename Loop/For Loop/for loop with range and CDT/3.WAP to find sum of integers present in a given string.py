#WAP to find the sum of integers in a given string
s=input()
summ=0
for ip in range(len(s)):
    if s[ip].isdigit():
        k=int(s[ip])
        summ+=k
print(summ)

#Execution
'''
1-> Take string as an ip.
2-> summ=0
3-> As we are dealing with index we are going to use for with range and  CDT
4-> check the element is digit or not(by using index positions
5-> if it is digit we need to type cast it into integer
6-> Now add that interger with summ summ+=k
7-> print summ of integers.'''


