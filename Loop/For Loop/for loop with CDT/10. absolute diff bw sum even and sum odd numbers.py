#Absolute diff between odd sum and even sum
s=input()
ES=0
OS=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            ES+=k
        else:
            OS+=k
print(abs(OS-ES))
#if ES>OS:
    #print(ES-OS)
#else:
    #print(OS-ES)

#Execution
'''1-> Take input from the user
2-> take ES=0  and OS=0 assuming that Even sum  and odd sum of integers are not  a given string is 0
3-> Taking input as 12V47
4-> Iteration starts
    Iteration-1: Extracts 1 checks condition isdigit true and converts into int and checks another condition
                 even or not False Enters into else block Odd Sum is 1
    Iteration-2: Extracts 2 checks condition isdigit true and converts into int and checks another condition
                 even or not True even Sum is 2
    Iteration-3: Extracts V checks condition isdigit False Doesnt enter into loop
    Iteration-4: Extracts 4 checks condition isdigit true and converts into int and checks another condition
                 even or not True even Sum is 6
    Iteration-5: Extracts 7 checks condition isdigit true and converts into int and checks another condition
                 even or not False Enters into else block Odd Sum is 8
5-> printts the absolute diff as 2'''