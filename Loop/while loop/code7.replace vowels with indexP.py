#WAP To Replace all the vowels with their index positions
s=input()
v='aeiouAEIOU'
us=''
for ip in range(len(s)):
    if s[ip] in v:
        us+=str(ip)
    else:
        us+=s[ip]
print(us)


#Execution
'''
1-> Take input from the user.
2-> Take vowels in a variable
3-> Take an updated empty string
4-> Take input as vasu
5-> Iteration starts
    Iteration-1: ip=0 checks condition s[ip] value is "v" is in v condition false goes to else condition us becomes "v"
    Iteration-2: ip=1 checks condition s[ip] value is "a" is in v condition True enters into if block now us is added with
                 the index position 1 now us becomes "v1"
    Iteration-3: ip=2 checks condition s[ip] value is "s" is in v condition false goes to else condition us becomes "v1s"
    Iteration-4: ip=3 checks condition s[ip] value is "u" is in v condition True enters into if block now us is added with
                 the index position 3 now us becomes "v1s3"
6-> Print updated string as v1s3.
'''
