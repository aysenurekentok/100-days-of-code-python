from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("QUIZZLER")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas()
        self.canvas.config(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="TEXT",
                                                     width=280, font=("Arial", 20, "italic"))
        self.score_label = Label(text="Score:", bg=THEME_COLOR,
                                 fg="white", font=("Arial", 20, "bold"))
        self.score_label.grid(row=0, column=1, pady=10)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40)
        self.check_mark = PhotoImage(file="images/true.png")
        self.cross_mark = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.check_mark, highlightthickness=0,
                                  activebackground=THEME_COLOR, bd=0, command=self.is_true)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=self.cross_mark, highlightthickness=0,
                                   activebackground=THEME_COLOR, bd=0, command=self.is_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="yellow")
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've completed the quiz. Your final score is: {self.quiz.score}")
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def is_true(self):
        self.feedback(self.quiz.check_answer("True"))

    def is_false(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_it_true):
        if is_it_true:
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
