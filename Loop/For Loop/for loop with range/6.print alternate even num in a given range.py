LL=int(input())
UL=int(input())
c=0
for i in range(LL, UL+1):
    if i%2==0:
        c+=1
        if c%2!=0:#to print 2nd even num if c%2==0:
            print(i)

'''LL=int(input())
UL=int(input())
L=[]
for i in range(LL,UL+1):
    if i%2==0:
        L.append()
print(L[::2])'''
        
#Execution
'''
1-> Taking lower limit from the user
2-> Taking upper limit from the user
3-> taking input LL as 1 and UL as 10
4-> iteration starts
    Iteration1: extracts 1 checks conditon false doesnt enter into loop
    Iteration2: extracts 2 checks condition True Checks count condition true Prints 2
    Iteration3: extracts 3 checks conditon false doesnt enter into loop
    Iteration4: extracts 4 checks condition True Checks count condition False doesnt print anything
    Iteration5: extracts 5 checks conditon false doesnt enter into loop
    Iteration6: extracts 6 checks condition True Checks count condition true Prints 6
    Iteration7: extracts 7 checks conditon false doesnt enter into loop
    Iteration8: extracts 8 checks condition True Checks count condition False doesnt print anything
    Iteration9: extracts 9 checks conditon false doesnt enter into loop
    Iteration10: extracts 10 checks condition True Checks count condition true Prints 10
5-> prints alternate even number as 2, 6, 10'''


#to print 2nd even num from given range(if c%2==0):
'''LL=int(input())
UL=int(input())
L=[]
for i in range(LL,UL+1):
    if i%2==0:
        L.append()
print(L[1::2])'''
#Execution
'''
1-> Taking lower limit from the user
2-> Taking upper limit from the user
3-> taking input LL as 1 and UL as 12
4-> iteration starts
    Iteration1: extracts 1 checks conditon false doesnt enter into loop
    Iteration2: extracts 2 checks condition True Checks count condition False doesnt Prints anything
    Iteration3: extracts 3 checks conditon false doesnt enter into loop
    Iteration4: extracts 4 checks condition True Checks count condition True prints 4
    Iteration5: extracts 5 checks conditon false doesnt enter into loop
    Iteration6: extracts 6 checks condition True Checks count condition False doesnt Prints anything
    Iteration7: extracts 7 checks conditon false doesnt enter into loop
    Iteration8: extracts 8 checks condition True Checks count condition True Prints 8
    Iteration9: extracts 9 checks conditon false doesnt enter into loop
    Iteration10: extracts 10 checks condition True Checks count condition False doesnt Prints anything
    Iteration11: extracts 11 checks conditon false doesnt enter into loop
    Iteration12: extracts 12 checks condition True Checks count condition True Prints 12
5-> prints alternate even number as 4, 8, 12'''


'''LL=int(input())
UL=int(input())
c=0
for i in range(LL, UL+1):
    if i%2==0:
        c+=1
        if c%2!=0:#to print 3rd even num if c%3==0:
            print(i)'''



'''LL=int(input())
UL=int(input())
L=[]
for i in range(LL,UL+1):
    if i%2==0:
        L.append()
print(L[2::3])'''




