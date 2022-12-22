from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
PADDING = 20


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        # creation of quiz GUI:
        self.window = Tk()
        self.window.title("myQuiz")
        self.window.config(bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")

        self.question_box = Canvas(width=300, height=250, highlightthickness=0)
        self.current_question = self.question_box.create_text(150, 125,
                                                              width=280,
                                                              text="Some Question Text",
                                                              font=("Arial", 20, "italic"))

        true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_image, highlightbackground=THEME_COLOR)

        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, highlightbackground=THEME_COLOR)

        self.score_label.grid(column=1, row=0, padx=PADDING, pady=PADDING)
        self.question_box.grid(column=0, row=1, columnspan=2, padx=PADDING, pady=PADDING)
        self.true_button.grid(column=0, row=2, padx=PADDING, pady=PADDING)
        self.false_button.grid(column=1, row=2, padx=PADDING, pady=PADDING)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        new_q_text = self.quiz.next_question()
        self.question_box.itemconfig(self.current_question, text=new_q_text)
