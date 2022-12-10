# Import necessary modules
import tkinter as tk

# Create the main window
root = tk.Tk()

# Create a 5x1 grid of cells
cells = []
for i in range(5):
    cell = tk.Label(root, text="", width=10, height=5, borderwidth=1, relief="solid")
    cell.grid(row=0, column=i)
    cells.append(cell)

# Set the text of each cell to a letter of the word
# and change the color of the cell based on the character
word = "Hello"
for i in range(5):
    cells[i].configure(text=word[i])
    if word[i] == "*":
        cells[i].configure(bg="white", fg="black")
    elif word[i].isupper():
        cells[i].configure(bg="green", fg="black")
    elif word[i].islower():
        cells[i].configure(bg="yellow", fg="black")

# Start the GUI event loop
root.mainloop()