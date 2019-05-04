# Use no hangup to run the program in background even if you close the terminal.
# Do not forget to use & to put it in background.
# nohup python3.6 app.py &

import os
import subprocess
import speech_recognition as sr
import pyttsx3
import io_text


speech_engine = pyttsx3.init()
speech_engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
recognizer = sr.Recognizer()
mic = sr.Microphone()


def speak(text_to_speak):
    speech_engine.say(text_to_speak)
    speech_engine.runAndWait()


def process_audio_input(text):
    if (len(text) <= 0 or text == None):
        return None
    if text == io_text.JARVIS:
        speak(io_text.YES_MASTER)
    elif text == io_text.HELLO_JARVIS:
        speak(io_text.HELLO_MASTER)
    elif text == io_text.OPEN_VS_CODE:
        speak(io_text.OPENING_VS_CODE)
        subprocess.call('code')


with mic as source:
    recognizer.adjust_for_ambient_noise(source)
    while True:
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            process_audio_input(text.lower())
        except Exception as e:
            print(e)
        finally:
            audio = None


