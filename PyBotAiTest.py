
import wikipedia
import datetime 
import os
import playsound
from gtts import gTTS
import speech_recognition as sr
import random
import time
import selenium.webdriver as webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import webbrowser
import pyttsx3
import re, requests, subprocess, urllib.parse, urllib.request
import pafy 
import vlc 
import threading

# DIFFERENT SOUNDS
# def speak(text): 
#     textas = gTTS(text=text, lang="en", slow=False)
#     filename = "sir.mp3"
#     textas.save(filename)
#     playsound.playsound(filename)
#     os.remove(filename)

def speak(text): 
    engine=pyttsx3.init()
    voice=engine.getProperty('voices')
    engine.setProperty('voice', voice[0].id)
    engine.setProperty("rate", 155)
    engine.say(text)
    engine.runAndWait()
# ----------------------------------------------------------------------------------
def playMusic(name, type):
        urll = urllib.request.urlopen("https://www.youtube.com/results?" + urllib.parse.urlencode({"search_query": name}))
        results = re.findall(r"watch\?v=(\S{11})", urll.read().decode())
        youtubevvideo = "https://www.youtube.com/watch?v=" + "{}".format(results[0])
        video = pafy.new(youtubevvideo) 
        if type == "video":
            videolink = video.getbest()
            print("video is playing")
        elif type =="audio":
            videolink =video.getbestaudio()  
            print("audio is playing")  

        media = vlc.MediaPlayer(videolink.url)  
        
        media.play()



    
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
            print("Google Speech could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech service; {0}".format(e))
    return said



def getResults(searchword):
    chrome_options = Options()
    chrome_options.add_argument("--headless")   
    url = "https://www.google.com"
    driver = webdriver.Chrome(executable_path=r'C:\Users\carsl\Creative Cloud Files\App challenge\chromedriver.exe', chrome_options=chrome_options)
    driver.get(url)
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(searchword)
    search_box.submit()
    try:
        speak(driver.find_element(By.XPATH, "//span[@class='pclqee']").text)
        
    except:
        speak(driver.find_element(By.XPATH, "//span[@class='pclqee']").text)
        
      
def greetingsRunbot():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!, Im E-Girl banana what can i do for you")
    elif hour>=12 and hour <18:
        speak("Good Afternoon!, Im E-Girl banana what can i do for you")
    else:
        speak("Good Evening!, Im E-Girl banana what can i do for you")    




now = datetime.datetime.now()


responseThanks = ["you're welcome!", "No problem", "Ase is jesus", "cool!", "I'm here if you need me!",
             "Please dont call me if it is not a big deal"]

goodbye =["Bye please dont call me again", "Have a good day", "Call me if you need"]


botis_alive = True

greetingsRunbot()
while botis_alive:
    wordsaid = getAudio().lower()
    if "hey banana" in wordsaid:
        speak("Im here, Sir")

    if "wikipedia" in wordsaid:
        speak("searching wikipedia")
        wordsaid = wordsaid.replace("wikipedia","")
        results = wikipedia.summary(wordsaid, sentences = 2)
        print(results)
        speak("getting results from wikipedia")
        speak(results)

    elif 'price' in wordsaid:
        speak("Getting Results please wait a few second")
        getResults(wordsaid)

    elif "time" in wordsaid  and "is" in wordsaid  and "it" in wordsaid:
        speak(now.strftime("%I:%M %p'"))

    elif any(i in wordsaid for i in ["thank you", "thanks"]):
        speak(random.choice(responseThanks))

    elif "search" in wordsaid: 
            wordsaid = wordsaid.replace("open","")
            pathy = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(pathy))
            webbrowser.get('chrome').open_new_tab(wordsaid)
            speak("Opened website")

    
    elif "play" in wordsaid:
        typpes = wordsaid.split()[1]
        wordsaid = wordsaid.replace("play"+ typpes,"")
        speak("I am searching for your music")
        playMusic(wordsaid, typpes)

    elif any(i in wordsaid for i in ["exit", "bye", "shut up", "sleep"]):
        speak(random.choice(goodbye))
        botis_alive = False

