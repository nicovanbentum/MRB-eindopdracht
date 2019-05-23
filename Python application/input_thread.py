from sys import platform
import threading
import queue
import time
import re

# This interface reads keyboard input from a queue.
# https://stackoverflow.com/questions/5404068/how-to-read-keyboard-input/53344690#53344690

def poll_events(input_queue):
    while True:
        input_str = input()
        input_queue.put(input_str)

def get_kbd_string(input_queue):
    if (input_queue.qsize() > 0):
        return input_queue.get()
    return None

def launch_thread():
    input_queue = queue.Queue()
    input_thread = threading.Thread(target=poll_events, args=(input_queue,), daemon=True)
    input_thread.start()
    return input_queue