import tkinter as tk
import random

from data import words
from hangman_art import hangman_stages
from exceptions import WrongGuessException   

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("800x500")
        self.root.configure(bg="#222831")

        self.root.bind("<Key>", self.key_input)
        self.main_menu()

    def main_menu(self):
        self.clear()

        frame = tk.Frame(self.root, bg="#222831")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text="HANGMAN", font=("Arial", 26, "bold"),
                 fg="white", bg="#222831").grid(row=0, column=0, columnspan=3, pady=20)

        self.category = tk.StringVar(value="Fruits")
        tk.Label(frame, text="Category:", fg="white", bg="#222831").grid(row=1, column=0)

        col = 1
        for cat in words:
            tk.Radiobutton(frame, text=cat, variable=self.category, value=cat,
                           bg="#222831", fg="white", selectcolor="#393e46").grid(row=1, column=col)
            col += 1

        self.level = tk.StringVar(value="easy")
        tk.Label(frame, text="Difficulty:", fg="white", bg="#222831").grid(row=2, column=0)

        col = 1
        for lvl in ["easy", "medium", "hard"]:
            tk.Radiobutton(frame, text=lvl.capitalize(), variable=self.level, value=lvl,
                           bg="#222831", fg="white", selectcolor="#393e46").grid(row=2, column=col)
            col += 1

        tk.Button(frame, text="Start Game", bg="#00adb5", fg="white",
                  font=("Arial", 12, "bold"), command=self.start_game)\
            .grid(row=3, column=0, columnspan=3, pady=20)

    def start_game(self):
        self.clear()

        self.word = random.choice(words[self.category.get()][self.level.get()])
        self.display = ["_"] * len(self.word)
        self.attempts = 0

        self.time_left = 180 if self.level.get() == "easy" else 150 if self.level.get() == "medium" else 120

        main_frame = tk.Frame(self.root, bg="#222831")
        main_frame.pack(expand=True)

        left = tk.Frame(main_frame, bg="#222831")
        left.grid(row=0, column=0, padx=40)

        self.hangman_label = tk.Label(left, font=("Courier", 16),
                                     fg="white", bg="#222831", justify="left")
        self.hangman_label.pack()

        right = tk.Frame(main_frame, bg="#222831")
        right.grid(row=0, column=1, padx=40)

        self.word_label = tk.Label(right, text=" ".join(self.display),
                                   font=("Courier", 28, "bold"),
                                   fg="#00fff5", bg="#222831")
        self.word_label.pack(pady=20)

        self.timer_label = tk.Label(right, text=f"Time: {self.time_left}s",
                                    font=("Arial", 14, "bold"),
                                    fg="#ffcc00", bg="#222831")
        self.timer_label.pack(pady=10)

        self.keyboard = tk.Frame(right, bg="#222831")
        self.keyboard.pack()

        for i in range(26):
            letter = chr(65 + i)
            btn = tk.Button(self.keyboard, text=letter, width=4, height=2,
                            bg="#393e46", fg="white",
                            activebackground="#00adb5",
                            command=lambda l=letter: self.check(l))
            btn.grid(row=i//9, column=i%9, padx=5, pady=5)

        self.update_hangman()
        self.run_timer()

    def check(self, letter):
        for btn in self.keyboard.winfo_children():
            if btn["text"] == letter:
                btn.destroy()

        letter = letter.lower()

        try:
            if letter not in self.word:
                raise WrongGuessException()

            self.time_left += 10
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.display[i] = letter

        except WrongGuessException:
            self.attempts += 1
            self.time_left -= 5

        self.word_label.config(text=" ".join(self.display))
        self.update_hangman()

        if "_" not in self.display:
            self.root.after(200, lambda: self.end("You Win! 🎉"))

        if self.attempts == 6:
            self.root.after(200, lambda: self.end("You Lose! Word: " + self.word))

    def update_hangman(self):
        self.hangman_label.config(text=hangman_stages[self.attempts])

    def run_timer(self):
        if self.time_left > 0:
            color = "#00ff00" if self.time_left > 60 else "#ffcc00" if self.time_left > 20 else "#ff0000"
            self.timer_label.config(text=f"Time: {self.time_left}s", fg=color)

            self.time_left -= 1
            self.timer_job = self.root.after(1000, self.run_timer)
        else:
            self.end("Time's Up! ⏰ Word: " + self.word)

    def key_input(self, event):
        if event.keysym == "Return":
            self.start_game()
        elif event.keysym == "Escape":
            self.main_menu()
        elif hasattr(self, "keyboard"):
            letter = event.char.upper()
            if letter.isalpha():
                for btn in self.keyboard.winfo_children():
                    if btn["text"] == letter:
                        btn.invoke()
                        break

    def end(self, msg):
        if hasattr(self, "timer_job"):
            self.root.after_cancel(self.timer_job)

        self.clear()
        tk.Label(self.root, text=msg, font=("Arial", 20),
                 fg="white", bg="#222831").pack(pady=20)

        tk.Button(self.root, text="Play Again",
                  bg="#00adb5", fg="white",
                  command=self.main_menu).pack()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    HangmanGame(root)
    root.mainloop()
