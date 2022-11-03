#!/usr/bin/python3
import time
# in command prompt, type "pip install pynput" to install pynput.
from pynput.keyboard import Key, Controller

keyboard = Controller()
key = "Test Text"

for i in range(len(key)):
	keyboard.press(key[i])
	keyboard.release(key[i])
	time.sleep(0.5)
