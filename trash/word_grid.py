import tkinter as tk

def create_grid(root, word, colors, row):
    # Create a 5x1 grid of cells
    cells = []
    for i in range(5):
        cell = tk.Label(root, text="", width=10, height=5, borderwidth=1, relief="solid")
        cell.grid(row=row, column=i)
        cells.append(cell)

    # Set the text of each cell to a letter of the word
    # and change the color of the cell based on the corresponding color in the colors list
    for i in range(5):
        cells[i].configure(text=word[i])
        cells[i].configure(bg=colors[i])

def main():
    # Create the main window
    root = tk.Tk()

    # Create the first row of cells with the word "Hello"
    create_grid(root, "Hello")

    # Create the second row of cells with a user-provided word
    word = input("Enter a five-letter word: ")
    create_grid(root, word)

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()
