from moviepy.editor import VideoFileClip
import speech_recognition as sr


def extract_audio_from_video(video_path, output_audio_path='output_audio.wav'):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(output_audio_path)
    print(f"Extracted audio saved as {output_audio_path}")


r = sr.Recognizer()

with sr.AudioFile('output_audio.wav') as source:
    audio = r.record(source)

text = r.recognize_google(audio)
print(text)
