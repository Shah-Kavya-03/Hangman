import tkinter as tk
import random

from data import words
from hangman_art import hangman_stages
from exceptions import WrongGuessException   

# 🎨 Color Theme
BG      = "#222831"
CARD    = "#393e46"
ACCENT  = "#00adb5"
TEXT    = "#eeeeee"
WARNING = "#ffcc00"
SUCCESS = "#00ff00"
DANGER  = "#ff0000"
MUTED   = "#888e99"

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("800x500")
        self.root.configure(bg=BG)

        # Session stats
        self.wins   = 0
        self.losses = 0
        self.streak = 0

        self.root.bind("<Key>", self.key_input)
        self.main_menu()

    def main_menu(self):
        self.clear()

        outer = tk.Frame(self.root, bg=BG)
        outer.place(relx=0.5, rely=0.5, anchor="center")

        # Title
        tk.Label(outer, text="HANGMAN",
                 font=("Segoe UI", 32, "bold"),
                 fg=ACCENT, bg=BG).pack(pady=(0, 4))
        tk.Label(outer, text="guess the word before it's too late",
                 font=("Segoe UI", 11),
                 fg=MUTED, bg=BG).pack(pady=(0, 20))

        # Stats bar
        stats_frame = tk.Frame(outer, bg=CARD, padx=24, pady=10)
        stats_frame.pack(fill="x", pady=(0, 18))

        for label, val, color in [
            ("Wins",   self.wins,   SUCCESS),
            ("Losses", self.losses, DANGER),
            ("Streak", self.streak, WARNING),
        ]:
            col = tk.Frame(stats_frame, bg=CARD)
            col.pack(side="left", expand=True)
            tk.Label(col, text=str(val), font=("Segoe UI", 20, "bold"),
                     fg=color, bg=CARD).pack()
            tk.Label(col, text=label, font=("Segoe UI", 9),
                     fg=MUTED, bg=CARD).pack()

        # Category
        tk.Label(outer, text="Category:", fg=TEXT, bg=BG,
                 font=("Segoe UI", 11)).pack(anchor="w")

        self.category = tk.StringVar(value="Fruits")
        cat_frame = tk.Frame(outer, bg=BG)
        cat_frame.pack(fill="x", pady=(4, 14))

        for cat in words:
            rb = tk.Radiobutton(
                cat_frame, text=cat, variable=self.category, value=cat,
                bg=BG, fg=TEXT, selectcolor=CARD,
                activebackground=BG, activeforeground=ACCENT,
                font=("Segoe UI", 10), indicatoron=0,
                relief="flat", padx=10, pady=5,
                cursor="hand2"
            )
            rb.pack(side="left", padx=3)
            rb.bind("<Enter>", lambda e: e.widget.config(fg=ACCENT))
            rb.bind("<Leave>", lambda e: e.widget.config(fg=TEXT))

        # Difficulty
        tk.Label(outer, text="Difficulty:", fg=TEXT, bg=BG,
                 font=("Segoe UI", 11)).pack(anchor="w")

        self.level = tk.StringVar(value="easy")
        lvl_frame = tk.Frame(outer, bg=BG)
        lvl_frame.pack(fill="x", pady=(4, 20))

        lvl_colors = {"easy": SUCCESS, "medium": WARNING, "hard": DANGER}
        for lvl in ["easy", "medium", "hard"]:
            c = lvl_colors[lvl]
            rb = tk.Radiobutton(
                lvl_frame, text=lvl.capitalize(),
                variable=self.level, value=lvl,
                bg=BG, fg=c, selectcolor=CARD,
                activebackground=BG, activeforeground=c,
                font=("Segoe UI", 10, "bold"), indicatoron=0,
                relief="flat", padx=14, pady=5,
                cursor="hand2"
            )
            rb.pack(side="left", padx=4)

        # Start Button
        start_btn = tk.Button(outer, text="Start Game",
                              bg=ACCENT, fg="white",
                              font=("Segoe UI", 12, "bold"),
                              relief="flat", padx=30, pady=10,
                              cursor="hand2",
                              command=self.start_game)
        start_btn.pack()
        start_btn.bind("<Enter>", lambda e: e.widget.config(bg="#00c4cb"))
        start_btn.bind("<Leave>", lambda e: e.widget.config(bg=ACCENT))

        tk.Label(outer, text="Press Enter to start  |  Esc for menu",
                 font=("Segoe UI", 9), fg=MUTED, bg=BG).pack(pady=(12, 0))

    def start_game(self):
        self.clear()

        self.word = random.choice(words[self.category.get()][self.level.get()])
        self.display = ["_"] * len(self.word)
        self.attempts = 0

        self.time_left = 180 if self.level.get() == "easy" else 150 if self.level.get() == "medium" else 120

        main_frame = tk.Frame(self.root, bg=BG)
        main_frame.pack(expand=True)

        left = tk.Frame(main_frame, bg=BG)
        left.grid(row=0, column=0, padx=40)

        self.hangman_label = tk.Label(left, font=("Courier New", 16),
                                     fg=TEXT, bg=BG, justify="left")
        self.hangman_label.pack()

        # 🎯 CARD LAYOUT
        right = tk.Frame(main_frame, bg=CARD, padx=20, pady=20)
        right.grid(row=0, column=1, padx=40)

        self.word_label = tk.Label(right,
                                  text="   ".join(self.display),
                                  font=("Courier New", 28, "bold"),
                                  fg="#00fff5", bg=CARD)
        self.word_label.pack(pady=20)

        self.timer_label = tk.Label(right,
                                   text=f"⏰ Time: {self.time_left}s",
                                   font=("Segoe UI", 16, "bold"),
                                   fg=WARNING, bg=CARD)
        self.timer_label.pack(pady=10)

        self.keyboard = tk.Frame(right, bg=CARD)
        self.keyboard.pack()

        for i in range(26):
            letter = chr(65 + i)
            btn = tk.Button(self.keyboard,
                            text=letter,
                            width=4,
                            height=2,
                            bg=CARD,
                            fg="white",
                            activebackground=ACCENT,
                            font=("Segoe UI", 10, "bold"),
                            command=lambda l=letter: self.check(l))

            btn.grid(row=i//9, column=i%9, padx=5, pady=5)

            # 🎛️ Hover Effect
            btn.bind("<Enter>", lambda e: e.widget.config(bg=ACCENT))
            btn.bind("<Leave>", lambda e: e.widget.config(bg=CARD))

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

        self.word_label.config(text="   ".join(self.display))
        self.update_hangman()

        if "_" not in self.display:
            self.root.after(200, lambda: self.end("You Win! 🎉"))

        if self.attempts == 6:
            self.root.after(200, lambda: self.end("You Lose! Word: " + self.word))

    def update_hangman(self):
        self.hangman_label.config(text=hangman_stages[self.attempts])

    def run_timer(self):
        if self.time_left > 0:
            color = SUCCESS if self.time_left > 60 else WARNING if self.time_left > 20 else DANGER
            self.timer_label.config(text=f"⏰ Time: {self.time_left}s", fg=color)

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

        # Update stats
        if "Win" in msg:
            self.wins   += 1
            self.streak += 1
        else:
            self.losses += 1
            self.streak  = 0

        self.clear()
        tk.Label(self.root, text=msg,
                 font=("Segoe UI", 22, "bold"),
                 fg=TEXT, bg=BG).pack(pady=20)

        tk.Button(self.root, text="Play Again",
                  bg=ACCENT, fg="white",
                  font=("Segoe UI", 12, "bold"),
                  command=self.main_menu).pack()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    HangmanGame(root)
    root.mainloop()