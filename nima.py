import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<4:
        speak("Good afternoon")
    else:
        speak("Good Evening")

    speak("My name is Nima and Im your personal assistant")
    
def takeCommand():
    # takes commands from microphone and gives text
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print("user said : ", query)
    except Exception as e:
        print(e)
        speak("I didn't quite get you. Can you repeat that again?")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        speak("How can i help you?")
        query = takeCommand().lower()
        
        if 'Wikipedia' in query:
                speak("searching in wikipedia")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences = 2)
                speak("According to wikipedia")
                print(results)
                speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("youtube is opened")
            
        elif 'open google.com' in query:
            webbrowser.open("google.com")
            speak("google is opened")
        
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
            speak("gmail is opened")
        
        
        elif 'news for today' in query:
            webbrowser.open("news.google.com")
            speak("Here's what's making news")
            
            
        elif 'time' in query:
            now = datetime.datetime.now()
            speak('Current time is %d hours %d minutes' % (now.hour, now.minute))

        
        elif 'tell me the weather' in query:
            webbrowser.open('accuweather.com')
            speak("you can check the weather on Accuweather. Opening accuweather")
                    
            
        else:
            if 'stop' in query:
                speak("I hope I was helpful. See you soon!")
            break
