from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


def convert():
    mile = float(input.get())
    km = mile * 1.609344
    result.config(text=f"{km}")


label_miles = Label(text="Miles", font=20)
label_miles.grid(row=0, column=2)

label_is_equal_to = Label(text="is equal to", font=20)
label_is_equal_to.grid(row=1, column=0)

label_km = Label(text="Km", font=20)
label_km.grid(row=1, column=2)

result = Label(text="0")
result.grid(row=1, column=1)

input = Entry(width=10)
input.focus()
input.get()
input.grid(row=0, column=1)

button = Button(text="Calculate", command=convert)
button.grid(row=2, column=1)

window.mainloop()
