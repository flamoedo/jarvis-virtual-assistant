#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
 
import speech_recognition as sr
# from playsound import playsound
from time import ctime
from time import strftime
import locale
import time
import os
from gtts import gTTS
from pygame import mixer
from tempfile import TemporaryFile
import pyttsx3

 
def speak2(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='pt-br')
    mixer.init()

    sf = TemporaryFile()
    tts.write_to_fp(sf)
    sf.seek(0)
    mixer.music.load(sf)
    mixer.music.play()

def speak(astring):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(astring)
    engine.runAndWait()
 
def adjustAudio():
    r = sr.Recognizer()
    with sr.Microphone(device_index = 0, sample_rate = 48000) as source:
        r.adjust_for_ambient_noise(source, duration = 1)

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio, language='pt-br')
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    return data
 
def jarvis(data):

    if data == '':
        return

    if "temperatura" in data:
        speak("quarenta graus na sombra")
        return
    
    if "hora" in data:
        speak(strftime('%H:%M'))
        return

    if "dia" in data:
        locale.setlocale(locale.LC_ALL,'pt_BR')
        speak(strftime("%d de %b"))
        return


    if "Bom dia" in data:
        speak("bom dia!")
        return

    if "jogo" in data:
        speak("O Corinthians, é claro!")    
        return
    
    if "Onde fica" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Frank, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
        return

    
    speak("Não sei")
    

if __name__ == "__main__":
    # initialization
    time.sleep(2)

    # adjustAudio()

    speak("Olá")


    while 1:
        data = recordAudio()
        jarvis(data)