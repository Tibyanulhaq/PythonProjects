from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 10")

def shutdown():
    os.system("shutdown /s /t 1")

def logoff():
    os.system("shutdown -l")        

st=Tk()
st.title("SHUTDOWN")
st.geometry("500x400")
st.config(bg="grey")

r_button=Button(st,text="Restart",font=("Times New Roman",20,"bold","italic"),relief=RAISED , cursor="plus", border=8,command=restart)
r_button.place(x=150,y=40,height=50,width=200)

rt_button=Button(st,text="Restart Time",font=("Times New Roman",20,"bold","italic"),relief=RAISED , cursor="plus", border=8,command=restart_time)
rt_button.place(x=150,y=220,height=50,width=200)

s_button=Button(st,text="Shutdown",font=("Times New Roman",20,"bold","italic"),relief=RAISED , cursor="plus", border=8,command=shutdown)
s_button.place(x=150,y=130,height=50,width=200)

l_button=Button(st,text="Log Off",font=("Times New Roman",20,"bold","italic"),relief=RAISED , cursor="plus", border=8,command=logoff)
l_button.place(x=150,y=310,height=50,width=200)








st.mainloop()