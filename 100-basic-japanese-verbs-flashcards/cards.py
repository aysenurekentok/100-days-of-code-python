from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#BCD8DF"
RANDOM_WORD = ""


class Cards:

    def __init__(self):
        self.window = Tk()
        self.window.title("100 Basic Japanese Verbs Every Beginner Should Know")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        self.front_side = PhotoImage(file="images/totoro_front_side.png")
        self.back_side = PhotoImage(file="images/totoro_back_side.png")
        self.facepalm = PhotoImage(file="images/facepalm.png")
        self.give_reward = PhotoImage(file="images/give_reward.png")

        self.card = Canvas(width=700, height=394, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.background = self.card.create_image(350, 197, image=self.front_side)
        self.title = self.card.create_text(350, 50, text="Japanese", font=("Ariel", 16, "italic"))
        self.kanji = self.card.create_text(350, 180, text="", font=("BIZ UDGothic", 65, "bold"))
        self.hiragana = self.card.create_text(350, 320, text="", font=("BIZ UDGothic", 15))
        self.romaji = self.card.create_text(350, 370, text="", font=("Ariel", 15))
        self.card.grid(row=0, column=0, columnspan=3)

        self.check_mark = PhotoImage(file="images/check_mark.png")
        self.cross_mark = PhotoImage(file="images/cross_mark.png")

        self.check_button = Button(image=self.check_mark, bg=BACKGROUND_COLOR, command=self.got_it)
        self.check_button.grid(row=1, column=2)

        self.cross_button = Button(image=self.cross_mark, bg=BACKGROUND_COLOR, command=self.new_card)
        self.cross_button.grid(row=1, column=0)

        self.flip_button = Button(text="FLIP", bg=BACKGROUND_COLOR, font=("Ariel", 36, "bold"), command=self.flip)
        self.flip_button.grid(row=1, column=1)

        self.data_dict = {}
        self.open_file()
        self.new_card()
        self.window.mainloop()

    def open_file(self):
        try:
            data = pandas.read_csv("data/review_list.csv")
        except FileNotFoundError:
            full_data = pandas.read_csv("data/100-basic-japanese-verbs.csv")
            self.data_dict = full_data.to_dict(orient="records")
        else:
            self.data_dict = data.to_dict(orient="records")

    def new_card(self):
        global RANDOM_WORD
        RANDOM_WORD = random.choice(self.data_dict)
        self.card.itemconfig(self.background, image=self.front_side)
        self.card.itemconfig(self.title, text="Japanese", fill="black")
        self.card.itemconfig(self.kanji, text=RANDOM_WORD["Japanese"], fill="black")
        self.card.itemconfig(self.hiragana, text=RANDOM_WORD["Hiragana"], fill="black")
        self.card.itemconfig(self.romaji, text=RANDOM_WORD["Romaji"], fill="black")

    def got_it(self):
        self.data_dict.remove(RANDOM_WORD)
        learn = pandas.DataFrame(self.data_dict)
        learn.to_csv("data/review_list.csv", index=False)
        self.new_card()

    def flip(self):
        self.card.itemconfig(self.background, image=self.back_side)
        self.card.itemconfig(self.title, text="English", fill="white")
        self.card.itemconfig(self.kanji, text=RANDOM_WORD["English"], font=("Ariel", 40, "bold"), fill="white")
        self.card.itemconfig(self.hiragana, text="")
        self.card.itemconfig(self.romaji, text="")
