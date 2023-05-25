from tkinter import *
import datetime


def date_time():
    time=datetime.datetime.now()
    h=time.strftime("%I")
    min=time.strftime("%M")
    sec=time.strftime("%S")
    am=time.strftime("%p")


    lbl_hr.config(text=h)
    lbl_min.config(text=min)
    lbl_sec.config(text=sec)
    lbl_am.config(text=am)

    # DATE

    d=time.strftime("%d")
    m=time.strftime("%m")
    y=time.strftime("%y")
    day=time.strftime("%A")

    lbl_date.config(text=d)
    lbl_mon.config(text=m)
    lbl_year.config(text=y)
    lbl_day.config(text=day)

    lbl_hr.after(1000,date_time)



ob=Tk()
ob.title("Digital Clock")
ob.geometry("600x450")
ob.config(bg="grey")


lbl=Label(ob,text="Digital Clock",font=("Times New Roman",30,"bold","italic"),bg="grey")
lbl.place(x=100,y=40,width=400,height=50)

lbl_hr=Label(ob,text="00",font=("Times New Roman",30,"bold","italic"),bg="grey")
lbl_hr.place(x=110,width=80,height=50,y=120)

lbl_min=Label(ob,text="00",font=("Times New Roman",30,"bold","italic"),bg="grey")
lbl_min.place(x=210,width=80,height=50,y=120)

lbl_sec=Label(ob,text="00",font=("Times New Roman",30,"bold","italic"),bg="grey")
lbl_sec.place(x=310,width=80,height=50,y=120)

lbl_am=Label(ob,text="AM",font=("Times New Roman",30,"bold","italic"),bg="grey")
lbl_am.place(x=410,width=80,height=50,y=120)

lbl_hr_text=Label(ob,text="Hours.",font=("Times New Roman",20,"bold","italic"),bg="grey")
lbl_hr_text.place(x=110,width=80,height=30,y=190)

lbl_min_text=Label(ob,text="Mins.",font=("Times New Roman",20,"bold","italic"),bg="grey")
lbl_min_text.place(x=210,width=80,height=30,y=190)

lbl_sec_text=Label(ob,text="Sec.",font=("Times New Roman",20,"bold","italic"),bg="grey")
lbl_sec_text.place(x=310,width=80,height=30,y=190)

lbl_am_text=Label(ob,text="AM/PM",font=("Times New Roman",15,"bold","italic"),bg="grey")
lbl_am_text.place(x=410,width=80,height=30,y=190)


# DATE PART

lbl_date=Label(ob,text="00",font=("Times New Roman",30,"bold","italic"),bg="grey")
lbl_date.place(x=110,width=80,height=50,y=290)

lbl_mon=Label(ob,text="00",font=("Times New Roman",30,"bold","italic"),bg="grey")
lbl_mon.place(x=210,width=80,height=50,y=290)

lbl_year=Label(ob,text="00",font=("Times New Roman",30,"bold","italic"),bg="grey")
lbl_year.place(x=310,width=80,height=50,y=290)

lbl_day=Label(ob,text="00",font=("Times New Roman",15,"bold","italic"),bg="grey")
lbl_day.place(x=410,width=80,height=50,y=290)

lbl_date_text=Label(ob,text="Date.",font=("Times New Roman",20,"bold","italic"),bg="grey")
lbl_date_text.place(x=110,width=80,height=30,y=360)

lbl_mon_text=Label(ob,text="Month.",font=("Times New Roman",20,"bold","italic"),bg="grey")
lbl_mon_text.place(x=210,width=80,height=30,y=360)

lbl_year_text=Label(ob,text="Year.",font=("Times New Roman",20,"bold","italic"),bg="grey")
lbl_year_text.place(x=310,width=80,height=30,y=360)

lbl_day_text=Label(ob,text="Day.",font=("Times New Roman",20,"bold","italic"),bg="grey")
lbl_day_text.place(x=410,width=80,height=30,y=360)

date_time()


ob.mainloop()