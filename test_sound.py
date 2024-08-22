import pygame
import os

# Initialize Pygame mixer
try:
    pygame.mixer.init()
    print("Pygame mixer initialized successfully.")
except Exception as e:
    print(f"Failed to initialize Pygame mixer: {e}")

# Path to the sound file
sound_file = os.path.join(os.path.dirname(__file__), 'click.mp3')
if not os.path.isfile(sound_file):
    raise FileNotFoundError(f"Sound file not found: {sound_file}")

sound = pygame.mixer.Sound(sound_file)
print("Playing sound...")

# Play the sound
try:
    sound.play()
    pygame.time.wait(1000)  # Wait to ensure sound plays
    print("Sound should have played.")
except Exception as e:
    print(f"Error playing sound: {e}")
