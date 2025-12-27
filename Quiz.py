import tkinter as tk
from tkinter import messagebox
from utils import load_questions

# ---------------- DATA ---------------- #

questions = load_questions("data/questions.json")
current_q = 0
score = 0

# ---------------- FUNCTIONS ---------------- #

def check_answer(selected_option):
    global current_q, score

    correct_answer = questions[current_q]["answer"]

    if selected_option == correct_answer:
        score += 1
        feedback_label.config(text="Correct!", fg="green")
    else:
        feedback_label.config(
            text=f"Wrong! Correct answer: {correct_answer}",
            fg="red"
        )

    score_label.config(text=f"Score: {score}")

    root.after(1200, next_question)

def next_question():
    global current_q

    current_q += 1
    feedback_label.config(text="")

    if current_q < len(questions):
        load_question()
    else:
        messagebox.showinfo(
            "Quiz Completed",
            f"Final Score: {score} / {len(questions)}"
        )
        root.destroy()

def load_question():
    question_label.config(text=questions[current_q]["question"])

    for i, option in enumerate(questions[current_q]["options"]):
        option_buttons[i].config(
            text=option,
            command=lambda opt=option: check_answer(opt)
        )

# ---------------- GUI SETUP ---------------- #

root = tk.Tk()
root.title("Python Quiz Application")
root.geometry("450x350")
root.configure(bg="SystemButtonFace")  # default system color

# ---------------- SCORE ---------------- #

score_label = tk.Label(
    root,
    text="Score: 0",
    font=("Arial", 12, "bold"),
    fg="black",
    bg="SystemButtonFace"
)
score_label.pack(pady=10)

# ---------------- QUESTION ---------------- #

question_label = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    wraplength=400,
    fg="black",
    bg="SystemButtonFace"
)
question_label.pack(pady=15)

# ---------------- OPTIONS ---------------- #

option_buttons = []

for _ in range(4):
    btn = tk.Button(
        root,
        text="",
        font=("Arial", 11),
        width=30,
        bg="lightgray",
        fg="black"
    )
    btn.pack(pady=5)
    option_buttons.append(btn)

# ---------------- FEEDBACK ---------------- #

feedback_label = tk.Label(
    root,
    text="",
    font=("Arial", 11, "bold"),
    fg="black",
    bg="SystemButtonFace"
)
feedback_label.pack(pady=10)

# ---------------- START ---------------- #

load_question()
root.mainloop()
