🎮 Hangman Game
📌 Project Overview
This project is a GUI-based Hangman Game developed using Python and Tkinter. It follows an Object-Oriented Programming (OOP) approach and is modularized into multiple files for better structure and maintainability.
Players must guess a hidden word within limited attempts and time. The game includes categories, difficulty levels, and interactive UI elements.

✨ Features
🎯 Core Gameplay
Guess the hidden word letter by letter
Maximum 6 wrong attempts
Visual hangman progression with each incorrect guess 

🧠 Categories & Word Bank
Multiple categories:
Fruits, Movies, Animals, Countries, Sports, Tech 

Each category includes:
Easy, Medium, Hard difficulty levels

⚙️ Difficulty Levels
Level  | Time Limit
Easy   | 180 sec
Medium | 150 sec
Hard   | 120 sec

⏱️ Timer-Based Gameplay
Countdown timer for each round
Time increases on correct guesses
Time decreases on wrong guesses

🎮 Input Support
Mouse (on-screen keyboard)
Physical keyboard (A–Z input)

📊 Game Statistics
Tracks:
Wins
Losses
Win streak

🎨 Modern UI Design
Dark theme interface
Interactive buttons with hover effects
Card-style layout for gameplay

🧱 Project Structure
project/
│
├── hangman.py        # Main GUI and game logic
├── data.py           # Word categories and difficulty levels
├── hangman_art.py    # ASCII hangman drawings
├── exceptions.py     # Custom exception handling
└── README.md         # Project documentation

🧩 Module Description
🔹 hangman.py
Main entry point of the application 
Contains:
GUI setup (Tkinter)
Game logic
Event handling (keyboard + buttons)
Timer system
Score tracking

🔹 data.py
Stores all words categorized by:
Category
Difficulty level 

🔹 hangman_art.py
Contains ASCII representations of hangman stages 
Updates visually with incorrect guesses

🔹 exceptions.py
Defines custom exception:
WrongGuessException
Used to handle incorrect guesses cleanly 

▶️ How to Run the Project
1️⃣ Install Requirements
Python 3.x installed
(No external libraries required — Tkinter comes pre-installed)

2️⃣ Setup Project
Place all files in the same folder:
hangman.pydata.pyhangman_art.pyexceptions.py

3️⃣ Run the Game
python hangman.py

🎮 How to Play
Select:
Category
Difficulty level
Click Start Game or press Enter

Guess letters:
Click buttons OR Use keyboard (A–Z)
Avoid wrong guesses (max 6)

Complete the word before:
Time runs out ⏰
Hangman is completed 💀

🧠 Game Logic Overview
Random word selection:
random.choice(words[category][difficulty])

Correct guess:
Reveals letters
+10 seconds bonus

Wrong guess:
Attempts +1
-5 seconds penalty

Game ends when:
Word completed ✅
Attempts reach 6 ❌
Timer reaches 0 ⏰

🚀 Advanced Concepts Used
Object-Oriented Programming (OOP)
Event-driven programming (Tkinter)
Exception handling
Modular design
GUI development
Real-time timer using after()

👨‍💻 Team Members
Name          | Roll No | Contribution                                            |
Soham Naik    | B037    | Project structuring, modularization, exception handling | 
Kavya Shah    | B056    | GUI design, main logic implementation                   | 
Shriya Shetty | B058    | Categories, difficulty system, game design              |

📽️ Demo / Video
Demo.mp4
