'''
*
 *
  *
   *
    *

*(1,1) *(1,2) *(1,3) *(1,4) *(1,5) 
*(2,1) *(2,2) *(2,3) *(2,4) *(2,5)
*(3,1) *(3,2) *(3,3) *(3,4) *(3,5)
*(4,1) *(4,2) *(4,3) *(4,4) *(4,5)
*(5,1) *(5,2) *(5,3) *(5,4) *(5,5)

'''

n=int(input())
stars=1
spaces=0
for row in range(1,n+1):
    for sp in range(1,spaces+1):
        print(' ', end='')
    for st in range(1, stars+1):
        print('*', end=' ')
    print()
    spaces+=1
        
'''
w
