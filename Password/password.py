from tkinter import *
import string
import secrets
import pyperclip

root = Tk()
root.geometry("300x300")
root.title('Password Generator')
root.config(bg='#ffe5d9')

Font = ('arial', 15, 'bold')

label1 = Label(root, text='Password Generator', font=('Times', 18, 'bold'), bg='#FFF4E6', fg='#1D4C6B')
label1.grid(pady=10)
label2 = Label(root, text="Choose Password Length", font=('cairo', 13, 'bold'), bg='#FFF4E6', fg='#1D4C6B')
label2.grid()

length_Box = Spinbox(root, from_=4, to_=12, font=Font, width=5, wrap=True)
length_Box.grid()

passwordField = Entry(root, width=15, bd=2, font=Font)
passwordField.grid(padx=40)

button1 = Button(root, text='Generate', font=(Font, 10, 'bold'), bg='#FFF4E6',
       command=lambda: passwordField.insert(0, ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation) for _ in range(int(length_Box.get())))))
button1.grid(pady=5)

button2 = Button(root, text='Copy to Clipboard', font=(Font, 10, 'bold'), bg='#FFF4E6',
       command=lambda: pyperclip.copy(passwordField.get()))
button2.grid(pady=5)

root.mainloop()
