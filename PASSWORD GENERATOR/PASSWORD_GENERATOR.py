from tkinter import *
import string
import random

root = Tk()
root.title("Password Generator")
root.config(bg='gray20')
root.geometry("500x300")

def generate_password():
    # Get the user's input for name and password length
    user_name = Name.get()
    password_length = int(length.get())

    # Define the characters for password generation
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password of the specified length
    generated_password = user_name + ''.join(random.choice(characters) for _ in range(password_length - len(user_name)))

    # Display the generated password in the entry field
    Generated1.delete(0, END)
    Generated1.insert(0, generated_password)

# Label for the password generator title
password_label = Label(root, text='PASSWORD GENERATOR', font=('times new roman', 20, 'bold'), bg='gray20', fg='white')
password_label.config(anchor=CENTER)
password_label.pack()

# Label and Entry field for user name
name_label = Label(root, text="Enter user name", font=("times new roman", 15, "bold"), bg="gray20", fg="white")
name_label.place(x=50, y=100)
Name = Entry(root, font=("times new roman", 15), width=15)
Name.place(x=250, y=100)

# Label and Entry field for password length
length_label = Label(root, text="Enter password length", font=("times new roman", 15, "bold"), bg="gray20", fg="white")
length_label.place(x=50, y=150)
length = Entry(root, font=("times new roman", 15), width=15)
length.place(x=250, y=150)

# Label and Entry field for displaying generated password
generated_label = Label(root, text="Generated password", font=("times new roman", 15, "bold"), bg="gray20", fg="white")
generated_label.place(x=50, y=200)
Generated1 = Entry(root, font=("times new roman", 15), width=15)
Generated1.place(x=250, y=200)

# Button to generate password
generate_button = Button(root, text="GENERATE PASSWORD", font=("times new roman", 12), bd=0, cursor="hand2",
                         bg="orange", fg="white", command=generate_password)
generate_button.place(x=90, y=250, width=220)

# Button to clear inputs and generated password
restart_button = Button(root, text="RESTART", font=("times new roman", 12), bd=0, cursor="hand2",
                        bg="orange", fg="white", command=lambda: [Name.delete(0, END), length.delete(0, END),
                                                                 Generated1.delete(0, END)])
restart_button.place(x=315, y=250, width=100)



root.mainloop()
