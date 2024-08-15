#WAP to check given number is palindrome or not
n=int(input())
dummy=n
rev=0
while dummy>0:
    rem=dummy%10
    dummy//=10
    rev=rev*10+rem
if n==rev:
    print("Palindrome")

else:
    print("Not Palindrome")


#Execution
'''
1-> Take input from the user
2-> Take dummy input n is initialized with dummy
3-> Take rev=0 asuming that
4-> write condition when we need to extarct numbers from the given number we need to do remainder operation
    To extarct individual number and we need to do floor division operation to extract remain values
5-> Take user input as 123
6-> Iteration starts:
    Iteration1: 123>0 True enters into while condition gives remainder 3 and we get remain values 12
                Now rev becomes rev=0*10+3-->rev=3
    Iteration2: 12>0 True enters into while condition gives remainder 2 and we get remain values 1
                Now rev becomes rev=3*10+2-->rev=32
    Iteration3: 1>0 True enters into while condition gives remainder 1 and we get remain values 0
                Now rev becomes rev=32*10+1-->rev=321
    Iteration4: 0>0 False doesnt enters into while condition comes out from the loop
7-> After completion of iteration checks if condition that n==rev condition false enter into else block
8-> Prints output as not palindrome.
                
'''
