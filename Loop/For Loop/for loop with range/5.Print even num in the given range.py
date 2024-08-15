#Print even numbers in the given range
LL=int(input())
UL=int(input())
for n in range(LL,UL+1):
    if n%2==0:
        print(n)

#execution
'''
1-> Taking lower limit from the user
2-> Taking upper limit from the user
3-> taking input LL as 1 and UL as 5
4-> iteration starts
    Iteration1: Extracts 1 checks condition False prints noting
    Iteration2: Extracts 2 checks condition True prints 2
    Iteration3: Extracts 3 checks condition False prints noting
    Iteration4: Extracts 4 checks condition True prints 4
    Iteration5: Extracts 5 checks condition False prints noting
5-> Prints output as 2
                     4'''
    
