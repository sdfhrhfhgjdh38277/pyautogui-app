import pyautogui as pg
from time import sleep
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("voice", "ru")
com = pg.prompt("Enter command (1 from set): search, open, say, help: ")

# commands list:
commands = ["search", "open", "say", "help"]
# search command
if com == commands[0]:
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

# open command
if com == commands[1]:
    open_app = pg.prompt("Enter app name: ")
    sleep(1)
    pg.hotkey("winleft")
    sleep(0.5)
    pg.write(open_app, 0.5)
    pg.press("enter")
