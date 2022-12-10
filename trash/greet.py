# Import the required modules
import sys

# Initialize a variable to track whether the user wants to continue
should_continue = True

# Enter a loop to continually accept input
while should_continue:
  # Get the user's input
  name = input("Enter your name (or 'exit' to quit): ")

  # Check if the user wants to exit
  if name == "exit":
    # If so, set the flag to False to break out of the loop
    should_continue = False
  else:
    # If not, print a greeting to the user
    print("Hello, " + name + "!")
