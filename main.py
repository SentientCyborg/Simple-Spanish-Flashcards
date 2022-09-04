import random
import pandas as pd
import tkinter as tk
from ctypes import windll


def update_word():
    global active_card
    global timer
    window.after_cancel(timer)
    word_id = random.randint(0, max_frequency)
    active_card = to_learn[word_id]
    canvas.itemconfig(lang, text=lang_to_learn, fill="black")
    canvas.itemconfig(sp_word, text=active_card[lang_to_learn], fill="black")
    canvas.itemconfig(canvas_image, image=img_front)
    timer = window.after(3000, func=reveal_card)


def reveal_card():
    canvas.itemconfig(canvas_image, image=img_back)
    canvas.itemconfig(lang, text=original_language, fill="white")
    canvas.itemconfig(sp_word, text=active_card[original_language], fill="white")


def is_known():
    to_learn.remove(active_card)
    new_data = pd.DataFrame(to_learn)
    new_data.to_csv("data/to_learn.csv", index=False)
    update_word()


# makes everything sharp on certain monitors -- comment the line below if it makes things worse
windll.shcore.SetProcessDpiAwareness(1)

BACKGROUND_COLOR = "#B1DDC6"
max_frequency = 99
active_card = {}

# Change these values to update the languages
original_csv = "data/spanish_english.csv"
original_language = "English"
lang_to_learn = "Spanish"

# Data
try:
    data = pd.read_csv("data/to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv(original_csv)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# UI
window = tk.Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, func=reveal_card)

img_front = tk.PhotoImage(file="images/card_front.png")
img_back = tk.PhotoImage(file="images/card_back.png")

canvas = tk.Canvas(width=800, height=525, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=img_front)
lang = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
sp_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"), tag="previous")
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
r_image = tk.PhotoImage(file="images/right.png")
r_button = tk.Button(image=r_image, highlightthickness=0, command=is_known)
r_button.grid(row=1, column=0)

w_image = tk.PhotoImage(file="images/wrong.png")
w_button = tk.Button(image=w_image, highlightthickness=0, command=update_word)
w_button.grid(row=1, column=1)

update_word()
window.mainloop()
