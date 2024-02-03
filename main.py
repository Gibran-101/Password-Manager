from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle

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

# ---------------------------- SAVE PASSWORD ------------------------------- #


def clear_canvas():
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    email_entry.insert(0, "username@gmail.com")
    password_entry.delete(0, END)


def save():
    web_text = website_entry.get()
    mail_text = email_entry.get()
    password_text = password_entry.get()

    is_ok = messagebox.askokcancel(title=web_text, message=f"These are the details entered: \n{mail_text} "
                                                             f"\n{password_text} \n Is it ok to save?")

    if website_entry.get() == "" or password_entry.get() == "":
        messagebox.showwarning("Warning", "The credentials are empty.")

    if is_ok:
        with open("data.txt", mode='a') as data:
            data.write(f"Website: {web_text}, Email Address: {mail_text}, Password: {password_text}\n")
            clear_canvas()
    else:
        clear_canvas()

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

website_entry = Entry(width=43)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=43)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "username@gmail.com")

password_entry = Entry(width=33, show="*", )
password_entry.grid(row=3, column=1)

password_generator = Button(text="Generate", bg="white", highlightthickness=0, command=generate_password)
password_generator.grid(row=3, column=2)

add_password = Button(text="Add", width=36, bg="white", highlightthickness=0, command=save)
add_password.grid(row=4, column=1, columnspan=2)

window.mainloop()
