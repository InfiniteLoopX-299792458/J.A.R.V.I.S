import time

frames = ["", ".", "..", "...", "....", "....."]

for _ in range(3):
    for dots in frames:
        print(f"\rInitializing J.A.R.V.I.S{dots}     ", end="", flush=True)
        time.sleep(0.4)

print("\r✔  Systems Online!                 ")

#   "     " Those spaces at the end are intentional.
# They overwrite any leftover dots from the previous frame.
# This is an old but effective terminal trick.
# Professional terminal programs don't use extra spaces.
# They use ANSI escape sequences to erase the line completely.
# "\033[2K" -> which means "Erase the entire line".
