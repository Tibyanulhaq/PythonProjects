from tkinter import *
import speedtest 


def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down=str(round(sp.download()/(10**6),3)) + " Mbps "
    up=str(round(sp.upload()/(10**6),3)) + " Mbps "
    download.config(text=down)
    upload.config(text=up)




sp=Tk()
sp.geometry("500x600")
sp.title("Internet Speed Tester")
sp.config(bg="grey")

lbl=Label(sp,text="Internet Speed Tester",font=("Times New Roman",20,"bold","italic"),relief=RAISED,border=5)
lbl.place(x=50,y=50,width=400,height=70)

lbl_down=Label(sp,text="Downloading Speed",font=("Times New Roman",20,"bold","italic"),relief=RAISED,border=5)
lbl_down.place(x=70,y=160,width=360,height=60)

download=Label(sp,text="00",font=("Times New Roman",20,"bold","italic"),relief=RAISED,border=5)
download.place(x=70,y=230,width=360,height=60)

lbl_upload=Label(sp,text="Uploading Speed",font=("Times New Roman",20,"bold","italic"),relief=RAISED,border=5)
lbl_upload.place(x=70,y=320,width=360,height=60)

upload=Label(sp,text="00",font=("Times New Roman",20,"bold","italic"),relief=RAISED,border=5)
upload.place(x=70,y=390,width=360,height=60)

button=Button(sp,text="Click To Check",font=("Times New Roman",20,"bold","italic"),relief=RAISED,border=5 ,command=speedcheck)
button.place(x=100,width=300,height=60,y=480)


sp.mainloop()