from tkinter import *
from tkinter import ttk

import requests

def Weather():

    city=city_name.get()

    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=beebdd4c82ff232c6c0f02c1815d6eb0").json()
    label2.config(text=data["weather"][0]["main"])
    label4.config(text=data["wind"]["speed"])
    label6.config(text=int((data["main"]["temp"])-273.15))
    label8.config(text=data["main"]["pressure"])




win=Tk()
win.title("Weather App")
win.geometry("500x600")
win.config(bg="skyblue")

label=Label(win,text="Weather App",font=("Times New Roman",30,"italic","bold"),bg="skyblue")
label.place(x=100,y=20,height=50,width=300)

list=["faisalabad","sargodha","islamabad","lahore","gujranwala"]

city_name=StringVar()

combo=ttk.Combobox(win,font=("Times New Roman",15,"bold","italic"),values=list,textvariable=city_name)
combo.place(x=100,width=300,height=30,y=100)

button=Button(win,text="Get Weather",font=("Times New Roman",10,"bold"),relief=RIDGE,command=Weather)
button.place(x=150,width=200,height=30,y=150)

label1=Label(win,text="Weather",font=("Tomes New Roman",10,"bold","italic"),bg="skyblue")
label1.place(x=150,y=280,height=20,width=90)

label2=Label(win,text="",font=("Tomes New Roman",10,"bold","italic"),bg="skyblue")
label2.place(x=260,y=280,height=20,width=90)

label3=Label(win,text="Wind",font=("Tomes New Roman",10,"bold","italic"),bg="skyblue")
label3.place(x=150,y=320,height=20,width=90)

label4=Label(win,text="",font=("Tomes New Roman",10,"bold","italic"),bg="skyblue")
label4.place(x=260,y=320,height=20,width=90)

label5=Label(win,text="Temperature",font=("Tomes New Roman",10,"bold","italic"),bg="skyblue")
label5.place(x=150,y=360,height=20,width=90)

label6=Label(win,text="",font=("Tomes New Roman",10,"bold","italic"),bg="skyblue")
label6.place(x=260,y=360,height=20,width=90)

label7=Label(win,text="Pressure",font=("Tomes New Roman",10,"bold","italic"),bg="skyblue")
label7.place(x=150,y=400,height=20,width=90)

label8=Label(win,text="",font=("Tomes New Roman",10,"bold","italic"),bg="skyblue")
label8.place(x=260,y=400,height=20,width=90)








win.mainloop()