title = "J.A.R.V.I.S."

width = 44

print("╭" + "─" * width + "╮")
print("│" + title.center(width) + "│")
print("╰" + "─" * width + "╯")

import time

time.sleep(0.5)

import time

frames = ["", ".", "..", "...", "....", "....."]

for _ in range(3):
    for dots in frames:
        print(f"\rInitializing J.A.R.V.I.S{dots}     ", end="", flush=True)
        time.sleep(0.4)

time.sleep(1.5)

print("\r✔  Systems Online!                 ")

time.sleep(0.5)

#   "     " Those spaces at the end are intentional.
# They overwrite any leftover dots from the previous frame.
# This is an old but effective terminal trick.
# Professional terminal programs don't use extra spaces.
# They use ANSI escape sequences to erase the line completely.
# "\033[2K" -> which means "Erase the entire line".

from datetime import datetime

# Get the current hour (0–23)
current_hour = datetime.now().hour

# Decide the greeting
if 5 <= current_hour < 12:
    greeting = "Good Morning"

elif 12 <= current_hour < 17:
    greeting = "Good Afternoon"

else:
    greeting = "Good Evening"

if 5 <= current_hour < 12:
    greeting1 = "Your day awaits. I've been standing by!"

elif 12 <= current_hour < 17:
    greeting1 = "I hope your day is progressing well. How may I assist you?"

else:
    greeting1 = "Welcome back."

# Display the greeting
print(f"{greeting}, Guna.")
time.sleep(0.5)
print(f"{greeting1}")
print()

#Now lets make it listen to the user and respond accordingly.

from datetime import datetime

current_hour = datetime.now().hour

command = input("> ")

if command == "bye" or command == "exit":
    print()
    print("Bye Guna.")
    print("See you later.")
    # Say Good Night only at night
    if current_hour >= 21 or current_hour < 5:
        print("Good Night.")
        print()
    time.sleep(1)
    print("Shutting down J.A.R.V.I.S...")
    time.sleep(1)
    print("Offline.")

elif command == "hello" or command == "hi":
    print("Hello Guna.")
    time.sleep(0.5)
    print("How may I assist you?")
else:
    print("I'm still learning.")