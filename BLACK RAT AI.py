import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices ', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")

    elif  hour>=12 and hour<18:
        speak("Good Afternoon Sir")
        speak("I am Black Rat Sir tell me how can i help you Sir")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
         print("Recognizing....please wait Sir")
         query = r.recognize_google(audio, language='en-in')
         print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please....")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # logical for our black rat 
        if 'wikipedia' in query:
            speak('Serching in Wikipedia.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
 
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open google' in query:
            webbrowser.open("google.com") 

        elif 'open bing' in query:
            webbrowser.open("bing.com")               

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com") 

        elif 'play song for me' in query:
            music_dir = 'O:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif  'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"the time is {strTime}")

        elif 'open edge' in query:
            edgePath = "C:\\Program Files\\Microsoft\Edge\\Application\\msedge.exe"
            os.startfile(edgePath)

        elif 'open visual studio code' in query:
            codePath = "C:\\Users\\adesh tanmay\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open notepad ' in query:
            notePath = "%windir%\\system32\\notepad.exe"
            os.startfile(notePath) 

        elif 'open command prompt ' in query:
            cmdPath = "%windir%\\system32\\cmd.exe"
            os.startfile(cmdPath)
