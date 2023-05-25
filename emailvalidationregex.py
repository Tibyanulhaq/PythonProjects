import re

user_email=input("Enter your Email Here : ")
condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

if re.search(condition,user_email):
    print("Right Email")
else:
    print("Wrong Email")    