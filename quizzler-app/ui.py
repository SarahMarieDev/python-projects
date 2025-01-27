from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0", font=("Arial", 14), fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.question_background = Canvas(width=300, height=250)
        self.question_background.config(bg="white", highlightthickness=0)
        self.question_background.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.question_background.create_text(
            150, 125,  # Position (x, y) at the center of the canvas
            text="Some question text",  # Text content
            font=("Arial", 20, "italic"),  # Font style
            fill=THEME_COLOR,  # Text color
            width=280  # Optional: Wrap text to fit within this width
        )

        check_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=check_image, highlightthickness=0, command=self.answer_true, bd=0)
        self.true_button.grid(column=0, row=2, padx=20, pady=20)

        cross_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=cross_image, highlightthickness=0, command=self.answer_false, bd=0)
        self.false_button.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.question_background.itemconfig(self.question_text, text=q_text)

    def get_score(self):
        return self.quiz.score

    def answer_true(self):
        self.quiz.check_answer("True")
        if self.quiz.question_number <= len(self.quiz.question_list):
            self.get_next_question()

    def answer_false(self):
        self.quiz.check_answer("False")
        if self.quiz.question_number <= len(self.quiz.question_list):
            self.get_next_question()
