from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    password_file = open("../../../Documents/Data.txt", "a")
    website = website_entry.get().strip()
    login = login_entry.get().strip()
    password = password_entry.get().strip()
    password_file.write(f"{website} | {login} | {password}\n")
    password_file.close()
    website_entry.delete(0, END)
    password_entry.delete(0, END)


# TODO: Add validation to check for .com on website field
# TODO: Add logic to check if login exists. Option to change or add new.
# TODO: Delete functionality?
# TODO: Search functionality?
# TODO: Copy fields functionality?

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(130, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="nsew")
website_entry.focus()

login_label = Label(text="Email/Username:")
login_label.grid(column=0, row=2)
login_entry = Entry(width=35)
login_entry.grid(column=1, row=2, columnspan=2, sticky="nsew")
login_entry.insert(0, "sarahmarie73@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="nsew")

generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3, sticky="nsew")

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="nsew")

window.mainloop()
