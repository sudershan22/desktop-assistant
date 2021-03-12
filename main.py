import os
import time
import uuid
import getpass
import playsound
import subprocess
import webbrowser
import speech_recognition as sr
from win10toast import ToastNotifier
from datetime import datetime
from gtts import gTTS

username = getpass.getuser()

def ask():
    input = sr.Recognizer()
    with sr.Microphone() as source:
        audio = input.listen(source)
        data = ""
        try:
            data = input.recognize_google(audio)
            print("You said : ", data)
        except sr.UnknownValueError:
            speak("Sorry couldn't hear you, Please repeat again.")
    return data

def speak(listen):

    notifier = ToastNotifier()
    response = gTTS(text=listen, lang="en")
    file = str(uuid.uuid4()) + ".mp3"
    response.save(file)
    notifier.show_toast("Desktop Assistant", listen, duration=3)
    playsound.playsound(file,True)
    os.remove(file)

def wish():
    hours_now = datetime.now().hour
    if hours_now < 12:
        speak("Good Morning " + username)
    elif hours_now in range(12, 16):
        speak("Good Afternoon " + username)
    else:
        speak("Good Evening " + username)
    time.sleep(3)

if __name__=='__main__':

    wish()
    speak("I'm your Desktop Assistant, How can I help you?")
    while (1):

        listen = ask()

        if 'open browser' in listen:
            speak("Opening default browser")
            webbrowser.open_new_tab("https://www.google.com")

        elif 'search' in listen:
            text = listen.replace("search", "")
            speak("Searching " + text)
            webbrowser.open_new_tab("https://www.google.com/search?q=" + text)
            time.sleep(5)

        elif 'calculator' in listen:
            speak("Opening calculator")
            subprocess.Popen('C:\Windows\System32\calc.exe')


        elif "stop" in str(listen) or "exit" in str(listen) or "bye" in str(listen):
            speak("Bye " + username + "! Have a nice day!")
            break

        else:
            speak("Feature not yet available")