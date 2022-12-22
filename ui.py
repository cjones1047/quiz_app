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
        self.true_button = Button(image=true_image, highlightbackground=THEME_COLOR, command=self.click_true)

        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, highlightbackground=THEME_COLOR, command=self.click_false)

        self.score_label.grid(column=1, row=0, padx=PADDING, pady=PADDING)
        self.question_box.grid(column=0, row=1, columnspan=2, padx=PADDING, pady=PADDING)
        self.true_button.grid(column=0, row=2, padx=PADDING, pady=PADDING)
        self.false_button.grid(column=1, row=2, padx=PADDING, pady=PADDING)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.score_label["text"] = f"Score: {self.quiz.score}"
        self.question_box["bg"] = "white"
        if self.quiz.still_has_questions():
            self.true_button["state"] = "normal"
            self.false_button["state"] = "normal"
            new_q_text = self.quiz.next_question()
            self.question_box.itemconfig(self.current_question, text=new_q_text)
        else:
            self.end_game()

    def click_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def click_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, user_answer):
        # disable buttons while processing feedback
        self.true_button["state"] = "disabled"
        self.false_button["state"] = "disabled"
        if user_answer:
            # change background green
            self.question_box["bg"] = "#33FF46"
        else:
            # change background red
            self.question_box["bg"] = "#FF5B33"
        self.window.after(1000, func=self.get_next_question)

    def end_game(self):
        self.question_box.itemconfig(self.current_question,
                                     text="That's all.\n\n"
                                          f"Final score: {self.quiz.score}/{len(self.quiz.question_list)}"
                                     )
