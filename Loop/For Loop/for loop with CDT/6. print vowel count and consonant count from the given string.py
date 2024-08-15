# print how many vowels and consosnts are there in a given string


s=input()
v='AEIOUaeiou'
vc=0
cc=0
for i in s:
    if i.isalpha():
        if i in v:
            vc+=1
        else:
            cc+=1
print(f'vowel count is {vc}')
print(f'consonants is {cc}')

#execution
'''
1-> Take input from the user
2-> Assigning vowels to the variable v='aeiouAEIOU'
3-> taking vowels count vc as 0, Assuming that there is no vowels in the given input
4-> taking consonants count cc as 0, Assuming that there is no vowels in the given input
5-> my user input is vasavi
6-> Iteration starts
 Iteration-1: extracts v and checks it is alpha condition true and checks another condition
              v in v condition false enters into else block consonant count "cc" becomes 1
 Iteration-2: extracts a and checks it is alpha condition true and checks another condition
              a in v condition true enters vowel count "vc" becomes 1
 Iteration-3: extracts s and checks it is alpha condition true and checks another condition
              s in v condition false enters into else block consonant count "cc" becomes 2
 Iteration-4: extracts a and checks it is alpha condition true and checks another condition
              a in v condition true enters vowel count "vc" becomes 2
 Iteration-5: extracts v and checks it is alpha condition true and checks another condition
              v in v condition false enters into else block consonant count "cc" becomes 3
 Iteration-6: extracts i and checks it is alpha condition true and checks another condition
              i in v condition true enters vowel count vc becomes 3
7-> print(f'vowel count is 3')
    print(f'consonants count is 3')
