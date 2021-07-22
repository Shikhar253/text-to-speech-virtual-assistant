import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import cv2
import wikipedia
import pyjokes
import subprocess
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[17].id)
engine.say("hi i am siri")
engine.say("what can i help you with")
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice= listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'siri' in command:
                command = command.replace('siri', '')
                print(command1)
    except:
        pass
    return command

def run_siri():
    command = take_command()
    print(command)
    if 'play' in command:
        command = command.replace('play', '')
        talk('playing'+ command)
        pywhatkit.playonyt(command)
    elif 'time' in command:
        command = datetime.datetime.now().strftime('%I:%M %p')
        print(command)
        talk(command)
    elif 'tell me' in command:
        person = command.replace('tell me', '')
        inf = wikipedia.summary(person, 1)
        print(inf)
        talk(inf)
    elif 'how are you' in command:
        res = command.replace('how are you', '')
        talk('i am fine')
    elif 'open google' in command:
        command = command.replace('open', '')
        talk('opening google')
        pywhatkit.search(command)
    elif 'open youtube' in command:
        command = command.replace('open', '')
        talk('opening youtube')
        pywhatkit.search(command)
    elif 'open amazon' in command:
        command = command.replace('open', '')
        talk('opening amazon')
        pywhatkit.search(command)
    elif 'open' in command:
        command = command.replace('open', '')
        talk(command)
        pywhatkit.search(command)
    elif 'camera' in command:
        talk('opening camera')
        cam = cv2.VideoCapture(0)
        while True:
            ret, img = cam.read()
            cv2.imshow('webcam',img)
            j = cv2.waitKey(10)
            if j==27:
                break
        cam.release()
        cv2.destroyAllWindows()
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif command in command:
        talk('heres what i found')
        pywhatkit.search(command)
    else:
        talk('i didnt understand you')


while True:
    run_siri()