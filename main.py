import tkinter as tk
from speech_recognition import recognize_speech
from gtts import gTTS
import os

# Function to update subtitle text
def update_subtitle():
    subtitle = recognize_speech()
    if subtitle:
        subtitle_text.set(subtitle)
        tts = gTTS(text=subtitle, lang='en')
        tts.save("temp.mp3")
        os.system("afplay temp.mp3")  # Assumes macOS, change the command for other platforms


# Function to stop speech recognition
def stop_recognition():
    global recognizer
    recognizer.stop_listening()
       
# Application window
root = tk.Tk()
root.title("TalkTextify")

subtitle_text = tk.StringVar()

# Subtitle label
subtitle_label = tk.Label(root, textvariable = subtitle_text , wraplength=400)
subtitle_label.pack(pady = 20)

# Start button
start_button = tk.Button(root, text="Start", command=update_subtitle)
start_button.pack()

# Stop button
stop_button = tk.Button(root, text="Stop", command=stop_recognition)
stop_button.pack()

# Widgets and functionalities

# Run the Tkinter event loop
root.mainloop()