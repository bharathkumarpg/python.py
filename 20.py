uname1 = "appu"
pas1 = '123'
uname2 = "bhar"
pas2 = '1234'
uname3 = "vinay"
pas3 = '12345'
uname4 = "jyothi"
pas4 = '123456'
uname5 = "harish"
pas5 = '1234567'
username = input("Please enter the username ")
   if username  == uname1:
     password = input(f"Hey {username} Please enter your password ")
     if password == pas1:
         print("Hello You are loged in now ")
     else:
         print("Sorry your password is incorrect ")
     elif username  == uname2:
     password = input(f"Hey {username} Please enter your password ")
       if password == pas2:
         print("Hello You are loged in now ")
     else:
         print("Sorry your password is incorrect ")
elif username == uname3:
password = input(f"Hey {username} Please enter your password ")
 if password == pas3:
    print("Hello You are loged in now ")
else:
    print("Sorry your password is incorrect ")
 elif username == uname4:
password = input(f"Hey {username} Please enter your password ")
if password == pas4:
    print("Hello You are loged in now ")
else:
    print("Sorry your password is incorrect ")
elif username == uname5:
password = input(f"Hey {username} Please enter your password ")
if password == pas5:
    print("Hello You are loged in now ")
else:
    print("Sorry your password is incorrect ")

else:
    print("This user name is not valid")