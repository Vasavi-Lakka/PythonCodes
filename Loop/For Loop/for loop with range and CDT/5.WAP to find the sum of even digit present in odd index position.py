#WAP to find the sum of even digits present in odd index position
s=input()
es=0
for ip in range(len(s)):
    if s[ip].isdigit():
        k=int(s[ip])
        if k%2==0 and ip%2!=0:
            es+=k
print(es)



#Execution
'''
1-> Take string as an ip.
2-> summ=0
3-> As we are dealing with index we are going to use for with range and  CDT
4-> check the element is digit or not(by using indexing)
5-> if it is digit we need to type cast it into integer
6-> Now check the condition that element is even or not
7-> If condition is True in both conditions the only do ES+=K'''
