from tkinter import *
root = Tk()
root.geometry("500x400")
root.title("Translator")
root.configure(bg='Blue')
################################################################## Entry Box
varname1 = StringVar()
entry1=Entry(root,width=30,textvariable=varname1,font ="comicsansms 14 bold")
entry1.place(x=150,y=40)
varname2= StringVar()
entry2=Entry(root,width=30,textvariable=varname2,font ="comicsansms 14 bold")
entry2.place(x=150,y=100)

######################################################################### Labels

label1 = Label(root,text= "Enter Words : ",font ="comicsansms 14 bold",bg="yellow")
label1.place(x=5,y=40)

label2 = Label(root,text= "Translated : ",font ="comicsansms 14 bold",bg="yellow")
label2.place(x=5,y=100)


######################################################################## Buttons

btn1 = Button(root,text="Click",bd=10,bg="orange",activebackground= "blue",width=10,font ="comicsansms 14 bold")
btn1.place(x=70,y=170)

btn2 = Button(root,text="Exit",bd=10,bg="red",activebackground= "blue",width=10,font ="comicsansms 14 bold")
btn2.place(x=280,y=170)

root.mainloop()