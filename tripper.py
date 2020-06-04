import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import speech_recognition as sr
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('own email id','own password')
    server.sendmail('akash250799@gmail.com',to,content)
    server.close()
def takename():
    #It takes microphone input and return textual output
    speak("what is your name sir or mam")
    n=sr.Recognizer()
    with sr.Microphone() as sourcen:
        print("Listening......")
        n.pause_threshold=1
        audio=n.listen(sourcen)

    try:
        print("Recognising....")
        name=n.recognize_google(audio,language="en-in")

    except Exception as e:
        print("I didn't get that ,speak again please....")
        return "none"
    hour=int(datetime.datetime.now().hour)
    print(f"Hii {name} welcome to Tripper Assistant ")
    if hour>0 and hour<12:
        speak(f"Goodmorning {name}")
    elif hour>=12 and hour<16:
        speak(f"Goodafternoon{name}")
    else:
        speak(f"Good evening {name}")
    speak("Hello I am Tripper, your virtual assistant developed by Akash")
    speak(f"How may i help you {name}")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognising....")
        query=r.recognize_google(audio,language="en-in")
        print(f"You just said :{query}\n")

    except Exception as e:
        speak("Sorry ,I didn't get that  ,speak again please....")
        return "None"
    return query

if __name__=="__main__":
    takename( )
    query=takecommand().lower()
    if 'play music' in query:
            music_dir="D:\\music\\"
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0-20]))
            speak("playing music")

    elif 'wikipedia' in query:
            speak('Searching wikipedia....')
            query=query.replace("Wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

    elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube")

    elif 'open google' in query:
            webbrowser.open("www.google.com")
            speak("opening google")
        
    elif 'open akash github' in query:
            webbrowser.open("www.github.com/akashrajput25")
            speak("opening akash's github")
        
    elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            speak("opening instagram")

    elif 'open github' in query:
            webbrowser.open("www.github.com")
            speak("opening github")

    elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            speak("opening facebook")

    elif 'what' and 'time' in query:
            strtime =datetime.datetime.now().strftime("%H"+" "+"%M"+" "+"%S"+"seconds")
            speak(f"The time is {strtime}")

    elif 'open visualstudio' in query:
            codepath="C:\\Users\AKASH RAJPUT\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codepath)
            speak("opening Visualstudio")

    elif 'send email' and 'akash' in query:
            try:
                speak("What should I send him?")
                content=takecommand()
                to="akash250799@gmail.com"
                sendemail(to,content)
                speak("email has been sent")
            except Exception as e:
                speak("Sorry I am unable to send message")
                print(e)
    elif 'love you' in query:
            speak("You are too beautiful like a rose")
   
    else:
            speak("You said something that i could not recognise as a command")

            
   
