def chandu(arg):
    def inner():
        print('chandu has taken the call')
        arg()
        print('chandu has ended the call')
    return inner
@chandu
def vasavi():
    print('vasavi has started speaking')
    print('vasavi has ended speaking')
vasavi()
@chandu
def yamini():
    print('yamini has started speaking')
    print('yamini has ended the call')
yamini()
