'''
* * * * *      *(1,1) *(1,2) *(1,3) *(1,4) *(1,5) 
* * * * *      *(2,1) *(2,2) *(2,3) *(2,4) *(2,5)
* * * * *      *(3,1) *(3,2) *(3,3) *(3,4) *(3,5)
* * * * *      *(4,1) *(4,2) *(4,3) *(4,4) *(4,5)
* * * * *      *(5,1) *(5,2) *(5,3) *(5,4) *(5,5)
'''
n=int(input())
for row in range(1,n+1):
    for col in range(1, n+1):
        print('*', end=' ')
    print()


'''
1-> Take input from the user
2-> we are deailing with rows and columns
3-> outer for loop should be row
3-> Inner for loop should be column
4-> Take input as 3
5-> Iteration starts
    Iteration1. n=3
                row=1 checks it is present in row range or not condition satified enters into col loop
                      col=1 it is in range so prints * doesnt enter innto next row becoz in print we written end='' it means stay in the same line
                      col=2 it is in range so prints * * and stays in goes to next line
                      col=3 it is in range so prints * * * and stays in same line
                row=2 checks it is present in row range or not condition satified enters into col loop
                      col=1 it is in range so prints * doesnt enter innto next row becoz in print we written end='' it means stay in the same line
                      col=2 it is in range so prints * * and stays in same line
                      col=3 it is in range so prints * * * and stays in goes to next line
                
                row=3 checks it is present in row range or not condition satified enters into col loop
                      col=1 it is in range so prints * doesnt enter innto next row becoz in print we written end='' it means stay in the same line
                      col=2 it is in range so prints * * and stays in same line
                      col=3 it is in range so prints * * * and stays in goes to next line
6-> prints output as * * *
                     * * *
                     * * *
'''
