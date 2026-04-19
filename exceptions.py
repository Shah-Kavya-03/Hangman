class WrongGuessException(Exception):
    def __init__(self, message="Wrong Guess!"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message