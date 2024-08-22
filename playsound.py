from pynput import keyboard
import pygame
import os
import time

# Initialize Pygame mixer
pygame.mixer.init()

# Path to the sound file
sound_file = os.path.join(os.path.dirname(__file__), 'key_press.wav')
if not os.path.isfile(sound_file):
    raise FileNotFoundError(f"Sound file not found: {sound_file}")

sound = pygame.mixer.Sound(sound_file)

# State variables
ctrl_pressed = False

def on_press(key):
    global ctrl_pressed
    try:
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            ctrl_pressed = True
        print(f"Key pressed: {key.char}")
    except AttributeError:
        print(f"Special key pressed: {key}")

    # Play the sound
    sound.play()
    time.sleep(0.1)  # Brief pause to prevent overlapping sound issues

def on_release(key):
    global ctrl_pressed
    if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        ctrl_pressed = False
    elif key == keyboard.Key.esc and ctrl_pressed:
        # Stop listener
        return False

# Debug message to confirm the script starts
print("Starting key listener...")

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Debug message to confirm the script is still running
print("Listener has stopped.")