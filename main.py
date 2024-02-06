from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters+password_symbols+password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def clear_canvas():
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    email_entry.insert(0, "username@gmail.com")
    password_entry.delete(0, END)


def write_to_file(content):
    with open("data.json", mode='w') as data_file:
        json.dump(content, data_file, indent=4)


def save():
    web_text = website_entry.get()
    mail_text = email_entry.get()
    password_text = password_entry.get()
    new_data = {
        web_text: {
            "email": mail_text,
            "password": password_text,
        }
    }

    if website_entry.get() == "" or password_entry.get() == "":
        messagebox.showwarning("Warning", "The credentials are empty.")

    else:
        try:
            with open("data.json", mode='r') as data_file:
                # it reads the old data from json file
                current_data = json.load(data_file)
                # this updates the content of json file
                # new_data which you see here is the dic which we have created in the save() function
                current_data.update(new_data)
        except FileNotFoundError:
            write_to_file(new_data)
        else:
            # this writes the updated data back into the file
            write_to_file(current_data)
        finally:
            clear_canvas()


# ---------------------------- FIND PASSWORD -------------------------------- #
def find_password():
    web_text = website_entry.get().title()
    with open("data.json", mode='r') as data_file:
        file_info = json.load(data_file)
        if web_text in file_info:
            website_name = web_text
            email_name = file_info[web_text]["email"]
            password_name = file_info[web_text]["password"]
            print(f"{website_name}, {password_name}")
            messagebox.showinfo(title=web_text, message=f"Email Address: {email_name} \n Password: {password_name}")
        else:
            messagebox.showinfo(title="ERROR", message=f"Details not found for {web_text}")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")
canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(row=0, column=1)


website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/ Username:", bg="white")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)

website_entry = Entry(width=34)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=43)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "username@gmail.com")

password_entry = Entry(width=34, show="*")
password_entry.grid(row=3, column=1)

search_data = Button(text="Search", bg="white", highlightthickness=0, command=find_password)
search_data.grid(row=1, column=2)

password_generator = Button(text="Generate", bg="white", highlightthickness=0, command=generate_password)
password_generator.grid(row=3, column=2)

add_password = Button(text="Add", width=36, bg="white", highlightthickness=0, command=save)
add_password.grid(row=4, column=1, columnspan=2)

window.mainloop()
