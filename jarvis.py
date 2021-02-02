import pyttsx3
import datetime
import speech_recognition as sr

import wikipedia
import webbrowser
import os

engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")
    
    speak("I am Jarvis. Please tell me how may I help you?")

def takeCommand():
    """ 
    This function will take command from user and return it in a string
    """
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1  #pause threshold is if we pause in between speaking it shouldnt consider the sentence as complete
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio,language='en-in')
        print(f"User said: {query} \n")

    except Exception as e:
        print(e)
        print("Please say that again...")
        return "None"


    return query

if __name__ == "__main__":
    
    wishMe()
    while True:
        print("Can only run commands to search something on wikipedia, open youtube, open google, play music, show time and open visual code studio")
        query= takeCommand().lower()  # to match the query properly as it may contain capital letters and our condition will fail below

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results= wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir='C:\\Users\\sk\\Desktop\\Jarvis\\music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            startTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {startTime}")

        elif 'open code' in query:
            codePath= "C:\\Users\\sk\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'exit' in query:
            speak(f"Thank you sir. Exiting now....")
            exit()
            
       



        







