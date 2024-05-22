from tkinter import *
 
 
def verify_pass_cond():
    password = entry.get()
 
 
#Creating the password conditions
    conditions = [
        lambda p: len(p) >= 8,
        lambda p: sum(c.isdigit() for c in p) >= 1,
        lambda p: sum(c.isalpha() for c in p) >= 2,
        lambda p: any(not c.isalnum() for c in p),
        lambda p: any(c.isupper() for c in p)
    ]
 
 
#Creating the messages
    messages = [
        "password should have at least 8 characters.",
        "password should contain at least one digit.",
        "password should contain at least two letters.",
        "password should contain at least one special character.",
        "password should contain at least one capital letter"
    ]
 
 
    errors =[msg for condition, msg in zip(conditions, messages) if not condition(password)]
 
 
    if not errors:
        result.config(text="password meets all conditions.", fg="green")
    else:
        result.config(text="\n".join(errors), fg="red")
 
 
#Creating password visibility function
def make_password_visible():
    if appear_password.get():
        entry.config(show="")
    else:
        entry.config(show="*")
 
 
#Create the main window
root = Tk()
root.title("password condition checker - The pycodes")
root.geometry("300x200")
 
 
#Create a label and an entry for the password
label = Label(root, text="Enter your password:")
label.grid(row=0, column=3)
entry = Entry(root, show="*", width=30)
entry.grid(row=2, column=3, ipadx=30, padx=30)
 
 
#Create a checkbutton to render password visible
appear_password = BooleanVar()
appear_password_button = Checkbutton(root, text="show password", variable=appear_password, command=make_password_visible)
appear_password_button.grid(row=3, column=3)
 
 
#Create a check condition button
button = Button(root, text="Check conditions", command=verify_pass_cond)
button.grid(row=4, column=3, columnspan=2)
 
 
#Display result
result = Label(root, text="")
result.grid(row=5,column=3)
 
 
#Starting the event loop
root.mainloop()
