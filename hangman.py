import random
words = ["apple", "mango", "grape", "lemon"]
word = random.choice(words)
display = ["_"] * len(word)
attempts = 6
while attempts > 0 and "_" in display:
    print("Word:", " ".join(display))
    guess = input("Enter letter: ").lower()
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)
if "_" not in display:
    print("You Win!")
else:
    print("You Lose! Word:", word)
