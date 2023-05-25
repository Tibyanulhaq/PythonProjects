from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES


def change(text="type",src="English",dest="hindi"):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1=trans.translate(text1, src=src1, dest=dest1)
    return trans1.text

def data():
    s=src_box.get()
    d=dest_box.get()
    t=src_text.get(1.0,END)
    textget=change(text=t,  src=s,  dest=d)
    dest_text.delete(1.0,END)
    dest_text.insert(END,textget)




root= Tk()
root.title("Translator")
root.geometry("500x600")
root.config(bg="grey")

# Label

lbl=Label(root,text="Translator",font=("Times New Roman",30,"bold","italic"),bg="grey")
lbl.place(x=100,y=15,width=300,height=70)

# source text box

src_text=Text(root,font=("Times New Roman",20,"bold"),wrap=WORD)
src_text.place(x=10,y=100,width=480,height=200)

# Source ComboBoxes
list=list(LANGUAGES.values())
src_box=ttk.Combobox(root,values=list)
src_box.place(x=10,y=320,height=40,width=150)
src_box.set("English")

# Button

button=Button(root,text="Translate",font=("Times New Roman",20,"bold","italic"),relief=RAISED,bd=5,command=data)
button.place(x=175,width=150,y=320,height=40)
 
# Destination combobox 
dest_box=ttk.Combobox(root,values=list)
dest_box.place(x=340,width=150,height=40,y=320)
dest_box.set("English")


# destination text box

dest_text=Text(root,font=("Times New Roman",20,"bold"),wrap=WORD)
dest_text.place(x=10,y=380,width=480,height=200)



root.mainloop()
