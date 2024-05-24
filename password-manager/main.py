import json
import pyperclip
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_entry.delete(0, END)

    pw_letters = [choice(letters) for _ in range(randint(8, 10))]
    pw_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pw_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = pw_letters + pw_symbols + pw_numbers
    shuffle(password_list)
    generated_password = "".join(password_list)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


def save_password():
    website = website_entry.get()
    email = login_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("../../../Documents/Data.json", "r") as password_file:
                data = json.load(password_file)
        except FileNotFoundError:
            with open("../../../Documents/Data.json", "w") as password_file:
                json.dump(new_data, password_file, indent=4)
        else:
            if website in data:
                is_ok = messagebox.askokcancel(
                    message=f"Login for {website} already exists, would you like to update login details?")
                if not is_ok:
                    return
            data.update(new_data)
            with open("../../../Documents/Data.json", "w") as password_file:
                json.dump(data, password_file, indent=4)
            messagebox.showinfo(title="Success", message=f"Login information for {website} saved successfully.")
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    try:
        with open("../../../Documents/Data.json", "r") as password_file:
            data = json.load(password_file)
    except FileNotFoundError:
        messagebox.showinfo(message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Details for {website}: \n\nEmail: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(message=f"Details for {website} do not exist.")


def delete_entry():
    website = website_entry.get()
    try:
        with open("../../../Documents/Data.json", "r") as password_file:
            data = json.load(password_file)
    except FileNotFoundError:
        messagebox.showinfo(message="No data file found.")
    else:
        if website in data:
            del data[website]
            messagebox.showinfo(title=f"{website}", message=f"Details for {website} have been deleted.")
        else:
            messagebox.showinfo(message=f"Details for {website} do not exist.")
        with open("../../../Documents/Data.json", "w") as password_file:
            json.dump(data, password_file, indent=4)
    finally:
        website_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(130, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, sticky="nsew")
website_entry.focus()

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="nsew")

login_label = Label(text="Email/Username:")
login_label.grid(column=0, row=2)
login_entry = Entry(width=35)
login_entry.grid(column=1, row=2, columnspan=2, sticky="nsew")
login_entry.insert(0, "sarahmarie73@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="nsew")

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="nsew")

add_button = Button(text="Add", command=save_password)
add_button.grid(column=1, row=4, sticky="nsew")

delete_button = Button(text="Delete", command=delete_entry)
delete_button.grid(column=2, row=4, sticky="nsew")

window.mainloop()
