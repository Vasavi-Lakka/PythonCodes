#Sum of even numbers present in a given string

s=input()
ES=0
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            ES+=k
print(ES)

#execution
'''1-> Take input from the user
2-> take sum=0 assuming that Even sum of integers in a given string is 0
3-> Taking input as 12V45
4-> Iteration starts
    Iteration-1: Extracts 1 checks condition isdigit true and converts into int and
                 checks another condition even or not False sum remains 0
    Iteration-2: Extracts 2 checks condition isdigit true and converts into int and
                 checks another condition even or not True sum becomes 2
    Iteration-3: Extracts V checks condition isdigit False doesnt enter into loop sum remains 2
    Iteration-1: Extracts 4 checks condition isdigit true and converts into int and
                 checks another condition even or not True sum becomes 6
                 Iteration-1: Extracts 1 checks condition isdigit true and converts into int and
                 checks another condition even or not False sum remains 6
5-> Prints sum of even num as 6'''
