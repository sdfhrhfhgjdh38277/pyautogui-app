# imports
import pyautogui as pg
import webbrowser
from voice_py import *

# hello phrase and window to request
hello()
com = pg.prompt("Enter command (1 from set): search, open, say, help: ")

# commands list:
commands = ["search", "open", "say", "help", "commands"]
# search command
if com == commands[0]:
    search_command()
    user_input = pg.prompt("Enter text and browser (Example: youtube.com, chrome): ")
    search_text, browser_name = map(
        str.strip, user_input.split(",")
    )  # open selected browser
    pg.hotkey("winleft")
    sleep(0.5)
    pg.write(browser_name, 0.5)
    pg.press("enter")
    # Type the search text
    sleep(2)
    pg.write(search_text, interval=0.5)
    pg.press("enter")
    engine.say("Complete")
    engine.runAndWait()
# open command
if com == commands[1]:
    open_command()
    open_app = pg.prompt("Enter app name: ")
    sleep(1)
    pg.hotkey("winleft")
    sleep(0.5)
    pg.write(open_app, 0.5)
    pg.press("enter")
# say command
if com == commands[2]:
    say_text = pg.prompt("Enter text to say")
    engine.say(say_text)
# all commands
if com == commands[3]:
    all_commands()

if com == commands[4]:  # help command
    help()
