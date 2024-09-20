from pynput import keyboard
import pygame
import os
import time

# Initialize Pygame mixer
pygame.mixer.init()

# Paths to the sound files
sound_file_1 = os.path.join(os.path.dirname(__file__), 'key_press.wav')
sound_file_2 = os.path.join(os.path.dirname(__file__), 'key_press2.wav')

if not os.path.isfile(sound_file_1):
    raise FileNotFoundError(f"Sound file not found: {sound_file_1}")
if not os.path.isfile(sound_file_2):
    raise FileNotFoundError(f"Sound file not found: {sound_file_2}")

sound1 = pygame.mixer.Sound(sound_file_1)
sound2 = pygame.mixer.Sound(sound_file_2)

# State variables
ctrl_pressed = False
keys_held = set()  # To track keys that are currently held down

def play_sound_for_key(key):
    # Play sound2 for special keys (enter, backspace)
    if key == keyboard.Key.enter or key == keyboard.Key.backspace:
        sound2.play()
    else:
        # Use sound1 for other keys (including space)
        sound1.play()

def on_press(key):
    global ctrl_pressed
    try:
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            ctrl_pressed = True
        
        # Check if key is already held down
        if key not in keys_held:
            keys_held.add(key)  # Mark key as held
            print(f"Key pressed: {key}")
            # Play the appropriate sound only when the key is first pressed
            play_sound_for_key(key)
            time.sleep(0.1)  # Brief pause to prevent overlapping sound issues
    except AttributeError:
        # Handle special keys (non-character keys)
        if key not in keys_held:
            keys_held.add(key)  # Mark key as held
            print(f"Special key pressed: {key}")
            # Play sound for special keys
            play_sound_for_key(key)
            time.sleep(0.1)

def on_release(key):
    global ctrl_pressed
    # Remove key from held keys when released
    if key in keys_held:
        keys_held.remove(key)

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
