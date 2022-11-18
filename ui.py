from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=2, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=1, columnspan=2, row=1, pady=50)
        self.question_text = self.canvas.create_text(
            150, 125, text="Some Text", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=280)

        yes_image = PhotoImage(file="images/true.png")
        self.yes = Button(image=yes_image, highlightthickness=0, command=self.check_yes)
        self.yes.grid(column=1, row=2)
        no_image = PhotoImage(file="images/false.png")
        self.no = Button(image=no_image, highlightthickness=0, command=self.check_no)
        self.no.grid(column=2, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")

            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.yes.config(state="disabled")
            self.no.config(state="disabled")

    def check_yes(self):
        self.right_or_wrong(self.quiz.check_answer("True"))

    def check_no(self):
        self.right_or_wrong(self.quiz.check_answer("True"))

    def right_or_wrong(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)