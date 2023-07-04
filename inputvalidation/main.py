import re
name = input("Enter your name:\n")

if re.match('[0-9]', name): 
  print("Sorry enter a proper name")
else:
  username = input("Enter your username:\n")
  password = input("Enter your password:\n")
  confirmpassword = input("enter your password again:\n")
  if password  == confirmpassword:
    print('your password matched')
  else:
    print('Enter your password again')


