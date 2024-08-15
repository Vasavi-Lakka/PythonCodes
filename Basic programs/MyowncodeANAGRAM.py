w1=input('enter a word')
w2=input('enter a word')
word1=set(w1)
word2=set(w2)
words1=set(word1.difference(word2))
words2=set(word2.difference(word1))
print(words1)
print(words2)
if (len(w1)==len(w2)) and (words1 == words2):
    print("Anagarams")
else:
    print("Not Anagrams")


