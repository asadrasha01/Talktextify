import speech_recognition
import pyttsx3
from moviepy.editor import VideoFileClip

video = VideoFileClip('path_to_your_video_file')
video.audio.write_audiofile('output_audio.wav')



class SpeechRecognizer:
    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()

    def recognize_speech(self):
        with speech_recognition.Microphone() as mic:
            self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = self.recognizer.listen(mic)
            text = self.recognizer.recognize_google(audio)
            return text.lower()
