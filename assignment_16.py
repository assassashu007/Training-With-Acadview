print("Q1. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.\n")


from tkinter import *
m = Tk()
label = Label(m, text= "\nHello World\n")
label.pack()






print("\n\nQ2. Write a python program to in the same interface as above and create a action when the button is click it will display some text.\n")

 
def write_some():
    print("Acadview Python Training is the Best")
button = Button(m,text='Click to See Message',width=50,command = write_some)
button.pack()





print("\n\nQ3. Create a frame using tkinter with any label text and two buttons. One to exit and other to change the label to some other text.\n")


r = Tk()
def change_label():
    label2["text"] = "Crotia 2-1 Iceland. Congo!! "
frame = Frame(r)
frame.pack()
label2 = Label(r,text="\nCLICK ONE OF THE BUTTONS\n")
label2.pack()
bottomframe = Frame(r)
bottomframe.pack(side=BOTTOM)
stopbutton = Button(frame, text='Abort', width = 30, fg = 'Red', command = r.destroy)
stopbutton.pack(side=LEFT)
printbutton = Button(frame, text='Change Label', width = 30, fg = 'Blue', command=change_label)
printbutton.pack(side=LEFT) 






print("Q4. Write a python program using tkinter interface to take an input in the GUI program and print it.")


tk = Tk()
def display():
    print(e1.get()+ " loves " +e2.get())
Label(tk, text = "Enter your name: ").grid(row=0)
Label(tk, text = "Enter name of favorite player: ").grid(row=1)
e1 = Entry(tk)
e2 = Entry(tk)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
button1 = Button(tk, text='PRINT',width=50,fg='Green',command=display)
button1.grid(row=4,column=1)

m.mainloop()