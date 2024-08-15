#to check the given credentials or correct or not
#username=input()
#password=input()
#d={'username':'Ashu', 'password' : 'Assifa'}
#d1=d.get('username')
#d2=d.get('password')
#if d1==username and d2==password:
 #   print('Login successfull')
#else:
  #  print("Invalid credentials")

-----------------------------------------------
username=input()
password=input()
d={'username':'Ashu', 'password' : 'Assifa'}
if username==d['username'] and password==d['password']:
    print("Login Succesfull")
else:
    print("Invalid credentials")
    
