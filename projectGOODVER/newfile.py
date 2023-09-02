import tkinter as tk
import random
import requests
import time

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GUI Quiz Application")
        self.geometry("400x300")
       
        self.questions = self.fetch_questions()
        self.current_question = 0
        self.score = 0
        self.start_time = None
       
        self.create_widgets()
        self.show_question()
       
    def fetch_questions(self):
        response = requests.get("https://sheet2api.com/v1/RbUpSfgxS9mT/data-sheet-internship")
        data = response.json()
        questions = []
       
        for item in data["results"]:
            question = item["question"]
            correct_answer = item["correct_answer"]
            incorrect_answers = item["incorrect_answers"]
            answers = [correct_answer] + incorrect_answers
            random.shuffle(answers)
            questions.append((question, answers, correct_answer))
           
        return questions
       
    def create_widgets(self):
        self.label = tk.Label(self, text="Welcome to the Quiz App!")
        self.label.pack(pady=10)
       
        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(self, text="", command=lambda i=i: self.check_answer(i))
            btn.pack(fill=tk.BOTH, padx=10, pady=5)
            self.option_buttons.append(btn)
           
        self.score_label = tk.Label(self, text="")
        self.score_label.pack(pady=10)
       
    def show_question(self):
        if self.current_question < len(self.questions):
            question, answers, _ = self.questions[self.current_question]
            self.label.config(text=question)
           
            for i in range(4):
                self.option_buttons[i].config(text=answers[i], state=tk.NORMAL)
               
            self.start_time = time.time()
        else:
            self.label.config(text="Quiz Completed!")
            for btn in self.option_buttons:
                btn.config(state=tk.DISABLED)
            self.score_label.config(text=f"Final Score: {self.score}/{len(self.questions)}")
           
    def check_answer(self, selected_option):
        _, _, correct_answer = self.questions[self.current_question]
       
        if self.option_buttons[selected_option]["text"] == correct_answer:
            self.score += 1
       
        end_time = time.time()
        time_taken = round(end_time - self.start_time, 2)
        self.current_question += 1
        self.show_question()
       
        if self.current_question > 0:
            self.score_label.config(text=f"Score: {self.score}/{self.current_question} | Time taken: {time_taken}s")

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()