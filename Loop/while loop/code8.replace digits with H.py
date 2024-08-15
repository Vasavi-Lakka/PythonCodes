#WAP to replace all digits with H in a given string

s=input()
us=''
for ip in range(len(s)):
    if s[ip].isdigit():
        us+='H'
    else:
        us+=s[ip]
print(us)


#Execution
'''
1-> Take input from the user
2-> Take upadated string as empty
3-> take user input as v1s3
4-> Iteration starts:
    Iteration-1: ip=0 value is "v" checks condition False enters into else block us becomes "v"
    Iteration-2: ip=1 value is "1" checks condition True enters into if block that place is replaced with
                 H ,us becomes "vH"
    Iteration-3: ip=2 value is "s" checks condtion False enetrs into else block us becomes "vHs"
    Iteration-4: ip=3 value is "3" checks condition True enters into if block that place is replaced with
                 H ,us becomes "vHsH".
5-> Print output as updated string "vHsH".    
'''
