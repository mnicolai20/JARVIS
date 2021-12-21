import pyttsx3;
import speech_recognition as sr;
from decouple import config;
from datetime import datetime;
from random import choice
from utils import opening_text;

USERNAME = config("USER");
BOTNAME = config("BOTNAME");

engine = pyttsx3.init("sapi5");

# set rate
engine.setProperty("rate", 190);

# set volume
engine.setProperty("volume", 1.0);

# set voice
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id);

# text to speech conversion
def speak(text):
    engine.say(text)
    engine.runAndWait();

# Greeting
def greet_user():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good Afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?");

# take user input
def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query