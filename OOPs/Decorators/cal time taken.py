def timeDectorator(arg):
    def inner():
        import time
        T1=time.time()
        arg()
        T2=time.time()
        print('time taken is', T2-T1)
    return inner
@timeDectorator
def evenNumber():
    c=0
    n=1
    while True:
        if n%2==0:
            print(n)
            c+=1
        if c==10:
            break
        n+=1
evenNumber()
