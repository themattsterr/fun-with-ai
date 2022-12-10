import random
import string
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel

# This is the target word that the user needs to guess
target_word = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))

# This is the number of attempts the user has to guess the target word
num_attempts = 6

class GuessingGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # Set the window title
        self.setWindowTitle('Guessing Game')
        
        # Create a text field where the user can enter their guess
        self.guess_field = QLineEdit(self)
        self.guess_field.move(20, 20)
        self.guess_field.resize(100, 20)
        
        # Create a button that the user can click to submit their guess
        self.guess_button = QPushButton('Guess', self)
        self.guess_button.move(20, 50)
        
        # Create a label where we can display the result of the user's guess
        self.result_label = QLabel(self)
        self.result_label.move(20, 80)
        
        # Connect the clicked signal of the guess button to the on_click() method
        self.guess_button.clicked.connect(self.on_click)
        
        # Show the window
        self.show()
    
    def on_click(self):
        # Get the user's guess from the text field
        user_guess = self.guess_field.text()
        
        # Check if the user's guess is correct
        if user_guess == target_word:
            # If the user's guess is correct, set the result label to "You win!"
            self.result_label.setText('You win!')
        else:
            # If the user's guess is incorrect, decrement the number of attempts remaining
            num_attempts -= 1
            
            # Check if the user has any attempts remaining
            if num_attempts > 0:
                # If the user has attempts remaining, set the result label to tell the user
                # which letters in their guess are in the target word and whether they are
                # in the correct position
                correct_letters = ''
                for i in range(len(user_guess)):
                    if user_guess[i] == target_word[i]:
                        correct_letters += user_guess[i]
                self.result_label.setText('Correct letters: {}'.format(correct_letters))
            else:
                # If the user has no attempts remaining, set the result label to "You lose!"
                self.result_label.setText('You lose!')

if __name__ == '__main__':
    app = QApplication([])
    game = GuessingGame()
    app.exec_()
