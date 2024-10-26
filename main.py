import speech_recognition as sr
import webbrowser
import pyttsx3
import music
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsApi = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=6274ebd5ac4345188c08afd764b1079d"


def processReq(command):
    print(command)
    if "open google" in command.lower():
        webbrowser.open("https://www.google.com") 
    if "open youtube" in command.lower():
        webbrowser.open("https://www.youtube.com") 
    if "open facebook" in command.lower():
        webbrowser.open("https://www.facebook.com") 
    if "open instagram" in command.lower():
        webbrowser.open("https://www.instagram.com")
    if "open linkedin" in command.lower():
        webbrowser.open("https://www.linkedin.com")

    if command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        webbrowser.open(music.music[song])

    if "news" in command.lower():
        req = requests.get(newsApi)
        if req.status_code == 200:
            data = req.json()
            articles = data.get('articles',[])
            for article in articles:
                speak(article['title'])



def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Nova...")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=3)
            
            word = recognizer.recognize_google(audio)
            print("Recognizing...")
            if(word.lower() == "hey nova" or word.lower() == "hay nova" or word.lower() == "nova"):
                speak("Heyyyy !! How can I help you?")
                try:
                    with sr.Microphone() as source:
                        print("Nova is active and listening for your command...")
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        command = recognizer.recognize_google(audio)
                        processReq(command)
                except sr.WaitTimeoutError:
                    print("Timeout: No command detected.")
                except sr.UnknownValueError:
                    print("Sorry, I didn't catch that. Please try again.")
                except sr.RequestError:
                    print("Could not request results from Google Speech Recognition.")


        
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected within the time limit.")
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
