import random # Importing python library called random to use random choice function.
import sys # Importing python library called sys to use bold function.
import os # Importing os.

# Function to make text bold, credit to @RedCoder on replit for this.
def bold(type): sys.stdout.write("\033[1m" + type + "\033[0m")

# Defining a function to clear the console.
def screen_clear():
  # Clear the screen depending on what os type is being used.
  if os_type == 'nt': # If the os is Windows use cls to clear the screen.
    os.system('cls')
  elif os_type == 'posix': # If the os is Unix-like (Linux, MacOS, etc.) use clear to clear the screen.)
    os.system('clear')

# Defining a function to restart the game.
def restart():
  repeat = input('Try again? (y/n): ').lower()
  if repeat == 'n':
    quit()
  elif repeat == 'y':
    screen_clear()

os_type = os.name # Storing the OS type.

# List of the options.
options = ["1", "2", "3"]

# While loop to loop the game.
while True:
  bold('Rock Paper Scissors Game\n')
  print('1 = Rock 🪨') # Prints input option.
  print('2 = Paper 📄') # Prints input option.
  print('3 = Scissors ✂️') # Prints input option.
  user_option = input("Enter your choice (1, 2, 3): ")
  computer_option = random.choice(options)
  if user_option not in options:
        print("\nInvalid choice.")
        restart()
  elif user_option == "1":
    user_option = "Rock 🪨"
  elif user_option == "2":
    user_option = "Paper 📄"
  elif user_option == "3":
    user_option = "Scissors ✂️"
  if computer_option == "1":
   computer_option = "Rock 🪨"
  elif computer_option == "2":
    computer_option = "Paper 📄"
  elif computer_option == "3":
    computer_option = "Scissors ✂️"

  print(f"You chose: {user_option}")
  print(f"Computer chose: {computer_option}\n")

  if user_option == computer_option:
    print("It's a tie!")
    restart()
    continue
  elif user_option == "Rock 🪨" and computer_option == "Scissors ✂️":
    print(f"You win! {user_option} beats {computer_option}")
    restart()
    continue
  elif user_option == "Paper 📄" and computer_option == "Rock 🪨":
    print(f"You win! {user_option} beats {computer_option}")
    restart()
    continue
  elif user_option == "Scissors ✂️" and computer_option == "Paper 📄":
    print(f"You win! {user_option} beats {computer_option}")
    restart()
    continue
  else:
    print(f"You lose! {computer_option} beats {user_option}")
    restart()
    continue
