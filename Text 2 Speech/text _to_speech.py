from gtts import gTTS
import os
import pygame

Text = """Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability
        with the use of significant indentation."""

tts = gTTS(Text)
tts.save(f"audio.mp3")

pygame.init()

audio_files = 'audio.mp3'

pygame.mixer.init()

if os.path.exists('audio.mp3'):
    pygame.mixer.music.load('audio.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
else:
    print(f"File '{mp3_file_path}' not found.")