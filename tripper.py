import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import speech_recognition as sr
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('personal-email','password-of-email')
    server.sendmail('akash250799@gmail.com',to,content)
    server.close()
def takename():
    speak("What's your sweet name sir or mam")
    n=sr.Recognizer()
    with sr.Microphone() as sourcen:
        print("Listening......")
        n.pause_threshold=1.5
        audio=n.listen(sourcen)

    try:
        print("Recognising....")
        name=n.recognize_google(audio,language="en-in")

    except Exception as e:
        print("I didn't get that ,speak again please....")
        return "none"
    hour=int(datetime.datetime.now().hour)
    print(f".......... {name} welcome to Tripper Assistant.......... ")
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
        speak("Sorry ,I didn't get that  ,Thanks for trying Tripper")
        return "None"
    return query

if __name__=="__main__":
    takename( )
    query=takecommand().lower()
    if "play music" in query:
            music_dir="D:\\music\\"
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0-20]))
            speak("playing music")

    elif 'wikipedia' in query:
            speak('What to search on wikipedia?')
            word=takecommand()
            results=wikipedia.summary(word,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

    elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube")

    elif 'open google' in query:
            webbrowser.open("www.google.com")
            speak("opening google")
        
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

    elif 'search youtube' in query:
            speak("what would you like to search")
            content=takecommand()
            link="www.youtube.com/"+content
            webbrowser.open(link)
            speak("searching youtube")

    elif 'open visualstudio' in query:
            codepath="C:\\Users\\AKASH RAJPUT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            speak("opening Visualstudio")

    elif 'open spotify' in query:
            codepath1="C:\\Users\\AKASH RAJPUT\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(codepath1)
            speak("opening spotify")

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

    elif 'say' or 'speak'in query:
            if 'say' in query:
              query=query.replace('say','') 
              speak(query)
            elif 'speak' in query:
              query=query.replace('speak','')
              speak(query)

    elif 'beautiful' in query:
            speak("You are too beautiful like a rose")

    elif 'like you' in query:
            speak(" Oh My God ! You like me, Tripper likes you too")
   
    else:
            speak("You said something that i could not recognise as a command")

            
   
