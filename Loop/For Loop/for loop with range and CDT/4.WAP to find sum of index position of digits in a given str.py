s=input()
ipsumm=0
for ip in range(len(s)):
    if s[ip].isdigit():
        ipsumm+=ip
print(ipsumm)

#Execution
'''
1-> Taking string from the user
2-> take index position sum as 0
3-> we are dealing with the index positions so we are going to use for loop with range and CDT
4-> check the element is digit or not (by using index position).
5-> if condition is true add ip to ipsumm.
6-> print summ outside of loop.
