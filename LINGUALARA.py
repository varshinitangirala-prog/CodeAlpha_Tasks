import tkinter as tk
from tkinter import messagebox
import random


# ==============================
# LANGUAGE DATA
# ==============================

lessons = [
    {
        "word": "Hello",
        "meaning": "Hola",
        "category": "Greetings"
    },
    {
        "word": "Thank You",
        "meaning": "Gracias",
        "category": "Common Phrases"
    },
    {
        "word": "Good Morning",
        "meaning": "Buenos Dias",
        "category": "Greetings"
    },
    {
        "word": "Friend",
        "meaning": "Amigo",
        "category": "Vocabulary"
    }
]


questions = [
    {
        "question": "What is the Spanish word for Hello?",
        "options": ["Hola", "Gracias", "Amigo", "Adios"],
        "answer": "Hola"
    },

    {
        "question": "What does Gracias mean?",
        "options": ["Hello", "Thank You", "Friend", "Morning"],
        "answer": "Thank You"
    },

    {
        "question": "What is the meaning of Amigo?",
        "options": ["Friend", "House", "Food", "Water"],
        "answer": "Friend"
    }
]


score = 0
current_question = 0



# ==============================
# FUNCTIONS
# ==============================


def show_lesson():

    lesson = random.choice(lessons)

    lesson_label.config(
        text=f"{lesson['word']}  =  {lesson['meaning']}\n\nCategory: {lesson['category']}"
    )



def start_quiz():

    global current_question
    current_question = 0

    quiz_window()



def quiz_window():

    global current_question
    global score

    if current_question >= len(questions):

        messagebox.showinfo(
            "Quiz Completed",
            f"Your Final Score: {score}/{len(questions)}"
        )

        score = 0
        return



    q = questions[current_question]


    quiz = tk.Toplevel()

    quiz.title("Language Quiz")
    quiz.geometry("400x400")


    question_label = tk.Label(
        quiz,
        text=q["question"],
        font=("Arial",14),
        wraplength=350
    )

    question_label.pack(pady=20)



    def check(answer):

        global current_question
        global score


        if answer == q["answer"]:
            score += 1
            messagebox.showinfo(
                "Correct",
                "Great Job!"
            )

        else:
            messagebox.showinfo(
                "Wrong",
                f"Correct Answer: {q['answer']}"
            )


        current_question += 1

        quiz.destroy()

        quiz_window()



    for option in q["options"]:

        btn = tk.Button(
            quiz,
            text=option,
            width=20,
            command=lambda x=option: check(x)
        )

        btn.pack(pady=5)




def show_progress():

    messagebox.showinfo(
        "Progress",
        f"Quiz Score: {score}"
    )



# ==============================
# MAIN WINDOW
# ==============================


app = tk.Tk()

app.title("Linguara - Language Learning App")

app.geometry("500x600")

app.config(bg="#f2f2f2")



title = tk.Label(
    app,
    text="🌍 Linguara Language App",
    font=("Arial",22,"bold"),
    bg="#f2f2f2"
)

title.pack(pady=20)



lesson_label = tk.Label(
    app,
    text="Start Learning",
    font=("Arial",16),
    bg="#f2f2f2"
)

lesson_label.pack(pady=20)



learn_btn = tk.Button(
    app,
    text="Learn Vocabulary",
    width=25,
    command=show_lesson
)

learn_btn.pack(pady=10)



quiz_btn = tk.Button(
    app,
    text="Start Language Quiz",
    width=25,
    command=start_quiz
)

quiz_btn.pack(pady=10)



progress_btn = tk.Button(
    app,
    text="View Progress",
    width=25,
    command=show_progress
)

progress_btn.pack(pady=10)



exit_btn = tk.Button(
    app,
    text="Exit",
    width=25,
    command=app.destroy
)

exit_btn.pack(pady=10)



app.mainloop()