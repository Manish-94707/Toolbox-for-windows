import pyttsx3 
import speech_recognition as sr 
import datetime
import os
## Music Player Module developed by me
from PyMusic_Player import Music_Player_GUI

## Initializing voice of Assistant
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

## Storing Playlist
playlist = []

## Speak module
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
# Bot answer
def bot_answer(answer):
    print("Assistant:" ,answer)

## Greetings from the bot
def greetings():
    global playlist
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Welcome to the Ultimate Music, I can Play Songs for you from the below list.")
    bot_answer("Say a playlist name to Play that Playlist")
    playlist = os.listdir('C:\\Users\HP\\Desktop\\Myproject(official)\\Songs')
    bot_answer(playlist)

## Speech recognition of user
def action_taker():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        command = r.recognize_google(audio, language='en-in')
        print(f"User: {command}\n")

    except Exception as e:
        # print(e)    
        bot_answer("Say that again please...")
        return "None"
    return command

greetings()

# Let's go infinitely
while True:
    command = action_taker().lower()
    song_playlist = list(map(str.lower,playlist))
    
    # With this condition it will ask for playing playlist from choice.
    # You need to say a playlist name from choice
    if any(command in s for s in song_playlist):
        get_ind = song_playlist.index(command)
        playlist_name = playlist[get_ind]
        playlist_dir = os.path.abspath("./Songs/" + playlist_name)
        bot_answer('Playing: '+playlist_name+' Playlist for you with PyMusic_Player!')
        speak('Playing: '+playlist_name+' Playlist for you with PyMusic_Player!')
        
        ## Calling the GUI of Music Player.
        Music_Player_GUI(playlist_dir)
    # If user asking for time
    elif 'the time' in command:
        str_ime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {str_ime}")
        bot_answer(f"Sir, the time is {str_ime}")
    # If use saying stop, it will break.
    elif 'stop' in command:
        speak('Good bye, See you again')
        bot_answer('Good bye, See you again')
        break
    else:
        bot_answer("Did not get the Playlist name, Please say from below names")
        speak("Did not get the Playlist name, Please say from below names")
        print(playlist)