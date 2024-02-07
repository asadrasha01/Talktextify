import tkinter as tk
import speech_recognition
from guiApp import GUIApp
from speech_recog import SpeechRecognizer
import threading
import os
os.environ['NSApplicationDelegate'] = '1'


if __name__ == "__main__":
    root = tk.Tk()
    app = GUIApp(root)
    root.mainloop()
