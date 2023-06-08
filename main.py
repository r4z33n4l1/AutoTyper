from pynput.keyboard import Key, Controller
import time
import sys

keyboard = Controller()

# Get filename from command line arguments
filename = sys.argv[1]

with open(filename, "r") as f:
    source = f.readlines()

print("starting")
time.sleep(4)

for i in source:
    for j in i:
        keyboard.press(j)
        keyboard.release(j)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

print("end")
