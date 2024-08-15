#WAP to print index positions of consonants in a given string
s=input()
v='aeiouAEIOU'
for ip in range(len(s)):
    if s[ip].isalpha():
        if s[ip] not in v:
            print(ip)


#Execution
'''
1-> Taking string from the user
2-> take vowels into one variable
3-> we are dealing with the index positions so we are going to use for loop with range and cdt
4-> check the condition isalpha 
5-> Now check whether the element is not present in vowels.
6-> print index position of consonants.
