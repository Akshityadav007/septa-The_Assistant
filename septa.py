import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir")
    elif 12 <= hour < 18:
        speak("Good afternoon Sir")
    else:
        speak("Good Evening Sir")

    speak("I am Septa. I am your personal assistant. How would you like to be served, Sir ?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"You: {query}\n ")

    except Exception as e:
        # print("Error : " + e)
        print("Say that again please")
        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing tasks

        if 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences= 2)
            speak('According to Wikipedia')
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'play movie cars' in query:
            music_dir = 'D:\\Movies'
            movies = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, movies[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open chrome' in query:
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif 'how are you' in query:
            speak('I am good, Sir. How are you?')

        elif 'bye' in query:
            speak('Hope you liked my service. See you soon, Sir. Bye.')
            exit(0)



