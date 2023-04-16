import sys
import winshell
import ctypes
import subprocess
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
from pyttsx3 import Engine

listener = sr.Recognizer()
engine: Engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'hey google' in command:
                command = command.replace('hey google', '')
                print(command)
            else:
                print('Nothing to be answer')
    except Exception as e:
        print(str(e))
    return command


def run_google():
    try:
        command = take_command()
        print(command)
        if 'play' in command:
            try:
                song = command.replace('play', '')
                talk('now playing' + song)
                pywhatkit.playonyt(song)
            except Exception as e:
                talk("Sorry, there's an error occurs while playing music. Please try again.")
                print("Sorry, there's an error occurs while playing music. Please try again.")
                print(str(e))

        elif 'search' in command:
            try:
                info = command.replace('search', '')
                talk('now searching for' + info)
                pywhatkit.search(info)
            except Exception as e:
                talk("Sorry, there's an error occurs while searching. Please try again.")
                print("Sorry, there's an error occurs while searching. Please try again.")
                print(str(e))

        elif 'open youtube' in command:
            talk("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in command:
            talk("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in command:
            talk("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'who is' in command:
            try:
                person = command.replace('who is', '')
                p_info = wikipedia.summary(person, 1)
                print(p_info)
                talk(p_info)
            except Exception as e:
                talk("Sorry, I don't know the person.")
                print("Sorry, I don't know the person.")
                print(str(e))

        elif 'what is' in command:
            try:
                things = command.replace('what is', '')
                t_info = wikipedia.summary(things, 1)
                print(t_info)
                talk(t_info)
            except Exception as e:
                talk("Sorry, I don't know what it is.")
                print("Sorry, I don't know what it is.")
                print(str(e))

        elif 'how are you' in command:
            talk("I am fine, Thank you")
            talk("How are you, Sir")

        elif 'joke' in command:
            print(pyjokes.get_joke())
            talk(pyjokes.get_joke())

        elif 'time' in command:
            try:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print(time)
                talk('The current time is ' + time)
            except Exception as e:
                talk("Sorry, I could not retrieve the time now. Please try again.")
                print("Sorry, I could not retrieve the time now. Please try again.")
                print(str(e))

        elif 'date' in command:
            try:
                today = datetime.datetime.now().strftime("%d %B %Y %A")
                print(today)
                talk("Today date is: " + today)
            except Exception as e:
                talk("Sorry, I could not retrieve the date now. Please try again.")
                print("Sorry, I could not retrieve the date now. Please try again.")
                print(str(e))

        elif 'lock window' in command:
            try:
                talk("locking the device")
                ctypes.windll.user32.LockWorkStation()
                sys.exit()
            except Exception as e:
                talk("Sorry, I could not lock your device at the moment.")
                print("Sorry, I could not lock your device at the moment.")
                print(str(e))

        elif 'shutdown system' in command:
            try:
                talk("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                sys.exit()
            except Exception as e:
                talk("Sorry, I could not shut down your device at the moment.")
                print("Sorry, I could not shut down your device at the moment.")
                print(str(e))

        elif 'empty recycle bin' in command:
            try:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                talk("Recycle Bin Recycled")
            except Exception as e:
                talk("Sorry, there's an error occur, please try again.")
                print("Sorry, there's an error occur, please try again.")
                print(str(e))

        elif 'thank you' in command:
            try:
                print("You're welcome, see you soon!")
                talk("You're welcome, see you soon!")
            except Exception as e:
                print("An Unexpected Error!")
                print(str(e))
            sys.exit()
        else:
            talk('Please say the command again.')
    except Exception as e:
        print("Session terminated: " + str(e))
        sys.exit()


while True:
    run_google()
