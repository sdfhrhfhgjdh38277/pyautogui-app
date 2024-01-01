import pyttsx3
from time import sleep

engine = pyttsx3.init()
engine.setProperty("voice", "ru")


def hello():
    engine.say("Hello! I you voice assistant")
    engine.runAndWait()


def search_command():
    engine.say("Okay, one second")
    sleep(0.5)
    engine.say("Complete")
    engine.runAndWait()


def open_command():
    engine.say("One moment")
    sleep(1)
