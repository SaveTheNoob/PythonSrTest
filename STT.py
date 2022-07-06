
from posixpath import split
import pyautogui
import time
from gtts import gTTS
import speech_recognition as sr
import random


def getAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        audio =r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)  

            print(said)
        except sr.UnknownValueError:
            print("dddd")
        except sr.RequestError as e:
            print("asasad; {0}".format(e))
    return said


while True:
    wordsaid = getAudio()
    for index,text in enumerate(wordsaid):
        inex_ofIndex = len(wordsaid)-1
        if index == inex_ofIndex:
            pyautogui.press(text)
            words = wordsaid.split()
            if any(i in words[-1] for i in ["and", "but", "or", "so", "or else", "for", "nor", "yet"]):
                pyautogui.write(" ")
            else:
                ad = [". ", ", "]
                pyautogui.write(random.choice(ad))
        else: 
            pyautogui.press(text) 

