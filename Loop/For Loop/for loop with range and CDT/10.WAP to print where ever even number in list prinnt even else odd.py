#Wite a program to print where ever even number present in the list print even number else odd.
L=eval(input('enter list:'))
for ip in range(len(L)):
    if L[ip] % 2 ==0:
        L[ip]="Even"
    else:
        L[ip]="Odd"
print(L)

'''
L=eval(input())
NL=[]
for i in L:
    if i%2==0:
        NL.append('even')
    else:
        NL.append('odd')
'''
#Execution
'''
1-> Take input from the user(as we are dealing with the list so we need to take "eval")
2-> We are dealing with index positions so we need to go with range and collection.
3-> Based on index position value we need to check that value is even or odd
4-> if it is even number we need to replace that number with "EVEN" or else "ODD".
5-> print List.
'''
