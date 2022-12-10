import tkinter as tk

# Create the root window
root = tk.Tk()
root.title("test")

# Keep track of the number of guesses
num_guesses = 0

button = tk.Button(root, text="Add", font=("Arial", 12))
button.grid(row=6, column=3, columnspan=3)

# Define the action taken when the button is pressed
def on_button_press():
    # Increment the number of guesses
    num_guesses += 1
    print(num_guesses)


# Tell the button what to do when it is pressed
button.config(command=on_button_press)

# Start the GUI event loop
root.mainloop()