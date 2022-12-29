import requests
from functions.online_ops import *
import pyttsx3
import speech_recognition as sr
from decouple import config
from datetime import datetime
from functions.os_ops import open_calculator, open_camera, open_cmd, open_notes, open_discord
from random import choice
from utils import opening_text
from pprint import pprint

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

#  Initialized an engine using the pyttsx3 module. 'sapi5' is a Microsoft Speech API that helps us use the voices.
engine = pyttsx3.init('nsss')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Enable the text_to_speach Function
def text_to_speach(text):
    """
    Used to text_to_speach whatever text is passed to it.
    :param text:
    :return:
    """

    engine.say(text)
    # Using the runAndWait() method, it blocks during the event loop and returns when the commands queue is cleared.
    engine.runAndWait()


# Greet the user
def greet_user():
    """
    Greets the user according to the time.
    :return:
    """

    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        text_to_speach(f"Good morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        text_to_speach(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        text_to_speach(f"Good evening {USERNAME}")
    text_to_speach(f"I am {BOTNAME}. How may I assist you?")


# Take input from the user
def take_user_input():
    """
    Takes user input, recognizes it using Speech Recognition module and converts it into text.
    :return:
    """

    speech_recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening the command...")
        speech_recognizer.pause_threshold = 1
        recording = speech_recognizer.listen(source)

        try:
            print("Transcribing...")
            query = speech_recognizer.recognize_google(recording, language="en-in")
            if 'stop' in query or not 'exit' in query:
                text_to_speach(choice(opening_text))
            else:
                hour = datetime.now().hour
                if 21 <= hour < 6:
                    text_to_speach(f"Good night {USERNAME}, take care!")
                else:
                    text_to_speach(f"Have a good day {USERNAME}")
                exit()
        except Exception:
            text_to_speach("Sorry, I couldn't understand that. Could you please say that again?")
            query = "None"
        return query


if __name__ == "__main__":
    greet_user()
    while True:
        query = take_user_input().lower()
        print(query)
        if 'open_notes' in query:
            open_notes()

        elif 'open discord' in query:
            open_discord()

        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()

        elif 'open camera' in query:
            open_camera()

        elif 'open calculator' in query:
            open_calculator()


        elif 'ip address' in query:
            ip_address = find_my_ip()
            text_to_speach(
                f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in query:
            text_to_speach('What do you want to search on Wikipedia, sir?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            text_to_speach(f"According to Wikipedia, {results}")
            text_to_speach("For your convenience, I am printing it on the screen sir.")
            print(results)

        elif 'youtube' in query:
            text_to_speach('What do you want to play on Youtube, sir?')
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'search on google' in query:
            text_to_speach('What do you want to search on Google, sir?')
            query = take_user_input().lower()
            search_on_google(query)

        elif "send whatsapp message" in query:
            text_to_speach('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            text_to_speach("What is the message sir?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            text_to_speach("I've sent the message sir.")

        elif "send an email" in query:
            text_to_speach("On what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            text_to_speach("What should be the subject sir?")
            subject = take_user_input().capitalize()
            text_to_speach("What is the message sir?")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                text_to_speach("I've sent the email sir.")
            else:
                text_to_speach("Something went wrong while I was sending the mail. Please check the error logs sir.")

        elif 'joke' in query:
            text_to_speach(f"Hope you like this one sir")
            joke = get_random_joke()
            text_to_speach(joke)
            text_to_speach("For your convenience, I am printing it on the screen sir.")
            pprint(joke)

        elif "advice" in query:
            text_to_speach(f"Here's an advice for you, sir")
            advice = get_random_advice()
            text_to_speach(advice)
            text_to_speach("For your convenience, I am printing it on the screen sir.")
            pprint(advice)

        elif "trending movies" in query:
            text_to_speach(f"Some of the trending movies are: {get_trending_movies()}")
            text_to_speach("For your convenience, I am printing it on the screen sir.")
            print(*get_trending_movies(), sep='\n')

        elif 'news' in query:
            text_to_speach(f"I'm reading out the latest news headlines, sir")
            text_to_speach(get_latest_news())
            text_to_speach("For your convenience, I am printing it on the screen sir.")
            print(*get_latest_news(), sep='\n')

        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            text_to_speach(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            text_to_speach(f"The current temperature is {temperature}, but it feels like {feels_like}")
            text_to_speach(f"Also, the weather report talks about {weather}")
            text_to_speach("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
