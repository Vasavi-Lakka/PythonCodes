s=input()
r=""
for i in range(len(s)):
    if i%2==0:
        r=r+(s[i].upper())
    else:
        r=r+(s[i].lower())

print(r)
