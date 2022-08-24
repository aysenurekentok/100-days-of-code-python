from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [random.choice(letters) for letter in range(random.randint(8, 10))]
    number_list = [random.choice(numbers) for number in range(random.randint(2, 4))]
    symbol_list = [random.choice(symbols) for symbol in range(random.randint(2, 4))]

    password_list = letter_list + number_list + symbol_list
    random.shuffle(password_list)

    password = "".join(password_list)

    input_password.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    if len(input_website.get()) == 0 or len(input_password.get()) == 0:
        messagebox.showinfo(title="Warning", message="Make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=input_website.get(), message=f"These are the details you entered:\nEmail: "
                                                                  f"{input_email.get()}\nPassword:{input_password.get()}")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{input_website.get()} / {input_email.get()} / {input_password.get()}\n")
                input_website.delete(0, END)
                input_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=60, pady=60)

canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=img)
canvas.grid(row=0, column=1)

# Labels
label_website = Label(text="Website:")
label_website.grid(row=1, column=0)

label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0)

label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

# Inputs
input_website = Entry(width=52)
input_website.focus()
input_website.grid(row=1, column=1, columnspan=2)

input_email = Entry(width=52)
input_email.insert(END, "aysenurekentok@gmail.com")
input_email.grid(row=2, column=1, columnspan=2)

input_password = Entry(width=33)
input_password.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(width=44, text="Add",command=save)
add_button.grid(row=4, column=1, columnspan=2)







window.mainloop()