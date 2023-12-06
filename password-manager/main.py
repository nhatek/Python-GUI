#   imports
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    created_password = ""
    for char in password_list:
        created_password += char
    entry3.delete(0, END)
    print(f"Your password is: {created_password}")
    entry3.insert(0, created_password)
    pyperclip.copy(created_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = entry1.get()
    email = entry2.get()
    password = entry3.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Couldn't add: empty field!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Details you've entered: \nEmail: {email}\nPassword: {password} \n\nDo you want to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                entry1.delete(0, END)
                entry2.delete(0, END)
                entry3.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_usr_label = Label(text="Email/Username:")
email_usr_label.grid(column=0, row=2)
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)


# Entries
entry1 = Entry(width=38)
entry1.focus()
entry1.grid(column=1, row=1, columnspan=2)
entry2 = Entry(width=38)
entry2.grid(column=1, row=2, columnspan=2)
entry3 = Entry(width=21)
entry3.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
