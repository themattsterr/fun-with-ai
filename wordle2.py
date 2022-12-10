import random
import tkinter as tk

# Create the root window
root = tk.Tk()
root.title("Wordle")

# Read the list of words from the file
with open("words.txt") as f:
    words = f.read().splitlines()

# Generate a random five-letter word
word = random.choice(words)

# # Prompt the user to guess the word
# guess = input("Guess a five-letter word: ")

# Keep track of the number of guesses
num_guesses = 0

# Create the grid of labels
cells = []
for i in range(6):
    row = []
    for j in range(5):
        label = tk.Label(root, text=" ", width=10, height=5, borderwidth=1, relief="solid", font=("Arial", 12))
        label.grid(row=i, column=j)
        row.append(label)
    cells.append(row)

# Create the input field and button
input_field = tk.Entry(root, font=("Arial", 12))
input_field.grid(row=6, column=0, columnspan=3)

button = tk.Button(root, text="Guess", font=("Arial", 12))
button.grid(row=6, column=3, columnspan=2)

# Define the action taken when the button is pressed
def on_button_press():
    # Get the word from the input field
    guess = input_field.get()
    # Clear the input field
    input_field.delete(0, tk.END)
    # Generate colors for grid based on user guess
    colors = gen_colors(word, guess)
    # Update grid with guess and colors
    update_grid(guess, colors)
    # Increment the number of guesses
    global num_guesses
    num_guesses += 1

def gen_colors(word, guess):
    colors = []
    for i in range(len(guess)):
        if guess[i] == word[i]:
            colors.append("green")
        elif guess[i] in word:
            colors.append("yellow")
        else:
            colors.append("white")
    return colors

def update_grid(word, colors):
    # Set the text of each cell to a letter of the word
    # and change the color of the cell based on the corresponding color in the colors list
    for i in range(5):
        cells[num_guesses][i].configure(text=word[i])
        cells[num_guesses][i].configure(bg=colors[i])

# Tell the button what to do when it is pressed
button.config(command=on_button_press)

# Start the GUI event loop
root.mainloop()