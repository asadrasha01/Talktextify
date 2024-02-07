import tkinter as tk

import speech_recognition

from guiApp import GUIApp
from speech_recog import SpeechRecognizer
import threading

if __name__ == "__main__":
    root = tk.Tk()
    app = GUIApp(root)
    recognizer = SpeechRecognizer()


    def recognition_thread():
        while app.is_listening:
            try:
                recognized_text = recognizer.recognize_speech()
                app.text.insert(tk.END, f"Recognized: {recognized_text}\n")
            except speech_recognition.UnknownValueError:
                pass


    root.mainloop()
