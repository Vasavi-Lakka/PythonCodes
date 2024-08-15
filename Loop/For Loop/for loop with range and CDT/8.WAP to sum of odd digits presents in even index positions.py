#WAP to find sum of even index positions of odd numbers
s=input()
summ=0
for ip in range(len(s)):
    if s[ip].isdigit():
        k=int(s[ip])
        if k%2!=0 and ip%2==0:
            summ+=k
print(summ)


#Execution
'''
1-> Take string as an ip.
2-> ipsumm=0
3-> As we are dealing with index we are going to use for with range and  CDT
4-> check the element is digit or not(by using indexing)
5-> if it is digit we need to type cast it into integer
6-> Now check the condition that element is odd or not and check index position is even or not
7-> If condition is True in both conditions the only do ipsumm+=ip'''

