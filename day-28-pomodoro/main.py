from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_title.config(text="Timer")
    check_box.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        count_down(work_sec)
        label_title.config(text="Work", fg=GREEN)
    else:
        if reps % 8 == 0:
            count_down(long_break_sec)
            label_title.config(text="Break", fg=RED)
        else:
            count_down(short_break_sec)
            label_title.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0"+str(count_sec)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        checks = ""
        repeat = int(reps / 2)
        for r in range(repeat):
            checks += "🗹"
        check_box.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(103, 128, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(row=1, column=1)

label_title = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
label_title.grid(row=0, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_box = Label( fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check_box.grid(row=3, column=1)


window.mainloop()
