def outer(arg):#arg=wish function address
    print('outer function is started')
    print(arg)
    def inner():
        print('inner fnction is started')
        arg()
        print('inner function is ended')
    print('outer function is ended')
    return inner
@outer #wish=outer(wish f/n address) #wish =inner f/n address
def wish():
    print('wish function is started')
    print('wish function is ended')
wish()
