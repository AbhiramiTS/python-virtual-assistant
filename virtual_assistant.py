import os
import speech_recognition as sr 
import pyttsx3 
import smtplib
import datetime
import wikipedia 
import webbrowser
import calendar

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Abhi!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hi, I am your personal assistant. I can answer your questions through Google, Open Youtube, Stackoverflow, wikipedia, Play songs, Send email, Tell you date and time and Open VS Code")

def getDate():

    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]

    _month = now.month
    _day = now.day

    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August','Spetember',
                    'October','November','December']

    ordinalNumbers = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th',
                        '14th','15th','16th','17th','18th','19th','20th','21st','22nd','23rd','24th',
                        '25th','26th','27th','28th','29th','30th','31st']

    speak('Today is ' + weekday + ', ' + ordinalNumbers[_day - 1] + ' of ' + month_names[_month - 1] + '.')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print("Sorry, I couldn't understand. Please say that again?")  
        return "None"
    return query



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('YOUR-EMAIL-ID', 'PASSWORD')
    server.sendmail('YOUR-EMAIL-ID', to, content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'C:\Users\User\Music\Abhi\Songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\bin\\code.exe"
            os.startfile(codePath)

        elif 'email to abhi' in query:
            try:
                speak("What should I send?")
                content = takeCommand()
                to = "abhiramits1@gmail.com"    
                sendEmail(to, content)
                speak("Your Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry! Unable to send the mail. Please try again later.")    
