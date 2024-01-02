import pyttsx3
from time import sleep
import webbrowser

engine = pyttsx3.init()
engine.setProperty("voice", "ru")


def hello():
    engine.say("Hello! I you voice assistant")
    engine.runAndWait()


# search
def search_command():
    engine.say("Okay, one second")
    sleep(0.5)
    engine.say("Complete")
    engine.runAndWait()


# open command
def open_command():
    engine.say("One moment")
    sleep(1)


def before_open():
    engine.say("Task complete")
    engine.runAndWait()


# commands list
def all_commands():
    engine.say("I have this commands: help, say, open, search")
    engine.runAndWait()


# help command
def help():
    webbrowser.open("https://t.me/python_tor")
