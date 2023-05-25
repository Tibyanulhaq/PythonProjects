from time import *
import random as r

def mistakes(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:

            if partest[i] != usertest[i]:
                error=error+1
        except:
            error=error+1
    return error 

def speed(time_s,time_e,usertest):
    time_delay=time_e-time_s
    time_R=round(time_delay,2) 
    speed=len(usertest)/time_R
    return round(speed)                

test=["Why you so sad,do well projects in python and you will get a job in a multinational company","python is a most popular worldwide language most of the people use it nowadays thank u"]
test1=r.choice(test)
print("    ****** Typing Test *****   ")
print(test1)
print()
print()


time1=time()
usertest=input("Enter : ")
time2=time()

print("MISTAKES : ",mistakes(test1,usertest))
print("SPEED : ",speed(time1,time2,usertest),"letter / sec")