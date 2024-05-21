from random import choice, randint, shuffle
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_letters = [choice(letters) for _ in range(randint(8, 10))]
    pw_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pw_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = pw_letters + pw_symbols + pw_numbers

    shuffle(password_list)

    generated_password = "".join(password_list)

    print(f"Your password is: {generated_password}")



def custom_askokcancel(title, message):
    dialog = Toplevel(window)
    dialog.title(title)
    dialog.geometry("300x250")

    result = [False]

    Label(dialog, text=message, wraplength=250).pack(pady=20)

    def on_ok():
        result[0] = True
        dialog.destroy()

    def on_cancel():
        result[0] = False
        dialog.destroy()

    ok_button = Button(dialog, text="OK", command=on_ok)
    ok_button.pack(side=LEFT, padx=20, pady=20)

    cancel_button = Button(dialog, text="Cancel", command=on_cancel)
    cancel_button.pack(side=RIGHT, padx=20, pady=20)

    dialog.transient(window)
    dialog.grab_set()
    window.wait_window(dialog)

    return result[0]


def save_password():
    website = website_entry.get()
    login = login_entry.get()
    password = password_entry.get()

    print(website, password)

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = custom_askokcancel(
            title=website,
            message=f"These are the details entered: \nEmail/Username: {login}\n Password: {password}\n Do you wish to continue?"
        )

        if is_ok:
            with open("../../../Documents/Data.txt", "a") as password_file:
                password_file.write(f"{website} | {login} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


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
