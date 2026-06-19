from tkinter import *
from rsa_logic import *
from file_util import *

master = Tk()
master.geometry("500x500")
master.title("RSA Cipher")
master.config(background="black")

label = Label(master, text="RSA Cipher",
              font=("Times New Roman", 15, 'bold'),
              fg="#00F0FF",
              bg="black")
label.pack()

def click():
    if message.get() == "" or p.get() == "" or q.get() == "":
        wout.delete("1.0", END)
        wout.insert("1.0", "Enter message and keys")
        return

    phi, n = param(int(p.get()), int(q.get()))

    if operationBtn.get() == 0:
        e = choose_e(phi)
        output = encrypt(message.get(), e, n)

    elif operationBtn.get() == 1:
        e = choose_e(phi)
        d = mod_inverse(e, phi)
        output = decrypt(eval(message.get()), d, n)

    wout.delete("1.0", END)
    wout.insert("1.0", str(output))



def clearAll():
    message.delete(0, END)
    p.delete(0, END)
    q.delete(0, END)
    wout.delete("1.0", END)

operation = ["Encrypt", "Decrypt"]
operationBtn = IntVar(value=0)
for index in range(len(operation)):
    radioBtn = Radiobutton(master,
                         text=operation[index],
                         variable=operationBtn,
                         value=index,
                         fg="#00F0FF",
                         bg="black",
                         selectcolor="black",
                         activeforeground="#FF00FF",
                         activebackground="black")
    radioBtn.pack()

message = Entry(master,
                font=('Arial', 7, 'bold'),
                fg="black",
                bg="#00F0FF")
message.pack()

p = Entry(master,
            font=('Arial', 7, 'bold'),
            fg="black",
            bg="#00F0FF")
p.pack()

q = Entry(master,
            font=('Arial', 7, 'bold'),
            fg="black",
            bg="#00F0FF")
q.pack()

####### OPEN
openBtn = Button(master,text="OPEN", command=lambda: open_file(message),
                 font=('Arial', 7, 'bold'),
                 fg="#00F0FF",
                 bg="black",
                 activeforeground="#00F0FF")
openBtn.pack()
####### SAVE
saveBtn = Button(master,text="SAVE", command=lambda: save_file(wout),
                 font=('Arial', 7, 'bold'),
                 fg="#00F0FF",
                 bg="black",
                 activeforeground="#00F0FF")
saveBtn.pack()
####### GO
button = Button(master,
                text="GO!",
                 command=click,
                 font=('Arial', 7, 'bold'),
                 fg="#00F0FF",
                 bg="black",
                 activeforeground="#00F0FF")
button.pack()

deleteBtn = Button(master,
                   text="Clear all",
                   command=clearAll,
                   font=('Arial', 7, 'bold'),
                   fg="#00F0FF",
                   bg="black",
                   activeforeground="#00F0FF")
deleteBtn.pack()

wout = Text(master,
                     font=('Arial', 15, 'bold'),
                     fg="#00F0FF",
                     bg="black",)
wout.pack()

master.mainloop()
