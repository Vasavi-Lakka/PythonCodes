#WAP to print index positions of a vowles present in given string
s=input()
v='aeiouAEIOU'
for ip in range(len(s)):
    k=s[ip]
    if k in v:
        print(ip,s[ip])


#Execution
'''
1-> Taking string from the user
2-> take vowels into one variable
3-> we are dealing with the index positions so we are going to use for loop with range and cdt
4-> take that indexposition element in to one variable
5-> Now check whether the element is present in vowels are not
6-> print index position of vowels
'''
