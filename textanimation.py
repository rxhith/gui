from tkinter import *
root=Tk()
root.geometry("900x600")
root.title("Sliding animation")
txt="Come Here!!!!!"
count=0
text=''
label=Label(root,text=txt,font=('Arial',30,"bold"),fg='black')
label.pack(pady=100)



def slider():
    global count,text
    if count>=len(txt):
        count=-1
        text=''
        label.config(text=text)
    else:
        text=text+txt[count]
        label.config(text=text)
    count=count+1
    label.after(150,slider)

slider()
root.mainloop()

















