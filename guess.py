import random

# Generate a random five-letter word
word = random.choice(["apple", "pear", "grape", "kiwi", "melon", "lemon"])

# Prompt the user to guess the word
guess = input("Guess a five-letter word: ")

# Keep track of the number of guesses
num_guesses = 1

# Keep looping until the user guesses the word or runs out of guesses
while guess != word and num_guesses < 6:
    # Annotate the user's guess with correct letters and correct letters in the correct position
    annotated_guess = ""
    for i in range(len(guess)):
        if guess[i] == word[i]:
            annotated_guess += guess[i].upper()
        elif guess[i] in word:
            annotated_guess += guess[i].lower()
        else:
            annotated_guess += "*"
    print("Your guess: {}".format(annotated_guess))

    # Prompt the user to try again
    guess = input("Guess a five-letter word: ")
    num_guesses += 1

# If the user guessed the word, let them know they won
if guess == word:
    print("Correct! You won in {} guesses.".format(num_guesses))

# If the user ran out of guesses, let them know they lost
else:
    print("Sorry, you ran out of guesses. The word was '{}'".format(word))
