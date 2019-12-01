import speech_recognition as sr
import time

r = sr.Recognizer()

print("Made By Mohamedhany.")
print("This Tool Helps You To Capture Speech As Text And display it on The screen.")
print("Which Might Help You Better Communicate With deaf People.")

time.sleep(3)

def offlineMode ():
    r = sr.Recognizer()  
    with sr.Microphone() as source:  
        print("Say something!")  
        audio = r.listen(source)  
   
    # recognize speech using Sphinx  
    try:  
        print(r.recognize_sphinx(audio))  
    except sr.UnknownValueError:  
        print("Sorry, Your Voice wasn't Clear")  
    except sr.RequestError as e:  
        print("Sphinx error; {0}".format(e))  

with sr.Microphone() as source:
    print("Now...Listening")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(format(text))
        time.sleep(5)
    except:
        print("Either Your Voice Wasn't Clear Or You don't Have internet Connection. Please Use The Offline Version if you can't acces The Internet.")
        uInput = input("Do You Want To Swith To Offline Mode?")

        if uInput == "yes":
            offlineMode()
        if uInput == "no":
            exit()

