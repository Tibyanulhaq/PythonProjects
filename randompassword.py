import random
import string as s

print("Welcome to our Random Password Generator")

def main():
    user_input=int(input("Enter length of password what you want : "))
    lower=s.ascii_lowercase
    upper=s.ascii_uppercase
    digit=s.digits
    symbols="!@#$%^&*"
    combine=lower+upper+digit+symbols
    x=random.sample(combine,user_input)
    password="".join(x)
    print(password)
    main()
    

main()    

