print("Q1.Create a dict with name and mobile number.Define a GUI interface and pack the label and create a scrollbar to scroll the list of keys in the dictionary.\n")


from tkinter import *
dictionary = {'Ashutosh': '8171xxxxxx', 'Prerak': '7066xxxxxx', 'Kushagra': '7289xxxxxx', 'Mayank': '8009xxxxxx', 'Harsh': '7792xxxxxx'}
tk = Tk()
f = Frame(master=tk)
f.pack()
scroll = Scrollbar(master=f)
scroll.pack(fill=Y, side=RIGHT)
l = Listbox(f, yscrollcommand=scroll.set)
for key in dictionary:
    l.insert(END, '{}'.format(key))
l.pack(side=LEFT)
scroll.config(command = l.yview)




print("\n\nQ2. In the same tkinter file as created above, create a function to insert items into the dictionary.\n")


def add():
    dictionary.update({e1.get(): e2.get()})
    for key in dictionary.keys():
        print(key)
    i = key
    l.insert(END, i)

btn = Button(master=f, text="ADD", command=add)
btn.pack()
lbl = Label(f,text="Enter the name and phone number: ")
lbl.pack()
e1 = Entry(f, text="Name")
e2 = Entry(f, text="Phone No.")
e1.pack()
e2.pack()

tk.mainloop()