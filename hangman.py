import tkinter as tk
import random

words = ["apple", "mango", "grape", "lemon"]

root = tk.Tk()
root.title("Hangman - Basic GUI")
root.geometry("500x400")

word = random.choice(words)
display = ["_"] * len(word)
attempts = 6

word_label = tk.Label(root, text=" ".join(display), font=("Arial", 24))
word_label.pack(pady=20)

attempt_label = tk.Label(root, text=f"Attempts Left: {attempts}", font=("Arial", 14))
attempt_label.pack()

def guess(letter):
    global attempts

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                display[i] = letter
    else:
        attempts -= 1

    word_label.config(text=" ".join(display))
    attempt_label.config(text=f"Attempts Left: {attempts}")

    if "_" not in display:
        result_label.config(text="You Win!")
    elif attempts == 0:
        result_label.config(text=f"You Lose! Word: {word}")

result_label = tk.Label(root, text="", font=("Arial", 16))
result_label.pack(pady=10)

keyboard_frame = tk.Frame(root)
keyboard_frame.pack()

for i in range(26):
    letter = chr(65+i)
    tk.Button(keyboard_frame, text=letter, width=4,
              command=lambda l=letter: guess(l.lower())
              ).grid(row=i//9, column=i%9)

root.mainloop()