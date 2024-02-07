from tkinter import *
import tkinter as tk
import threading
from speech_recog import SpeechRecognizer
import threading


class GUIApp:
    def __init__(self, root):
        self.root = root
        # Size of the window
        self.root.geometry("800x500")
        # Window name
        self.root.title("TalkTextify")

        self.label = tk.Label(root, text="To get subtitles press Start!", font=("Arial", 18))
        self.label.pack(padx=20, pady=20)

        self.text = tk.Text(root, height=12, font=("Arial", 12))
        self.text.pack(padx=10, pady=10)

        self.startButton = tk.Button(root, text="Start", font=("Arial", 18), command=self.start_recognition)
        self.startButton.pack(padx=10, pady=10)

        self.stopButton = tk.Button(root, text="Stop", font=("Arial", 18), command=self.stop_recognition)
        self.stopButton.pack(padx=10, pady=10)

        self.is_listening = False
        self.recognizer = SpeechRecognizer()

    def start_recognition(self):
        self.is_listening = True
        self.label.config(text="Listening!")
        self.recognition_thread = threading.Thread(target=recognition_thread)
        self.recognition_thread.start()


        # Call the recognition function from speechrecog.py
    def stop_recognition(self):
        self.is_listening = False
        self.label.config(text="To get subtitles press Start!")
        self.recognizer.stop_recognition()


# The following lines are optional if you want to run the GUI independently for testing.
if __name__ == "__main__":
    main_root = tk.Tk()
    app = GUIApp(main_root)
    recognizer = SpeechRecognizer()
    main_root.mainloop()
