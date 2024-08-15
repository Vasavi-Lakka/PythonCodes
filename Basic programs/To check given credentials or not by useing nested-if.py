d={'username':'Ashu', 'password' : 'Asifa'}

username=input()

if username==d['username']:
    password=input()
    if password==d['password']:
        print("Login Successfull")
    else:
        print("Invalid password")
else:
    print("Invalid username")
    
