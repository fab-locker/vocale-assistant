import asyncio
import json
import os

import pyttsx3
import speech_recognition as sr
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle

recognizer = sr.Recognizer()
speak = pyttsx3.init()
speak.setProperty('voice', 'french')
rate = speak.getProperty('rate')
speak.setProperty('rate', rate - 50)
volume = speak.getProperty('volume')
speak.setProperty('volume', volume + 0.50)
voices = speak.getProperty('voices')
speak.setProperty('voice', voices[0].id)


def talk(text):
    speak.say(text)
    speak.runAndWait()


def command():
    action = ""
    try:
        with sr.Microphone() as mic:
            voice = recognizer.listen(mic)
            action = recognizer.recognize_google(voice)
            action = action.lower()
    except:
        pass
    return action


async def ask_bing():
    print("Ouverture de Bing AI")
    cookies = json.loads(open("./cookies.json", encoding="utf-8").read())
    while True:
        bot = await Chatbot.create(cookies=cookies)
        response = await bot.ask(prompt=input("Demande quelque chose à bing AI : "),
                                 conversation_style=ConversationStyle.creative)
        for message in response["item"]["messages"]:
            if message["author"] == "bot":
                bot_response = message["text"]
        print("Bot's reponse:", bot_response)
        await bot.close()


def run():
    talk("Hello, how can I help ?")
    print("Hello, how can I help ?")
    while True:
        action = command()
        print(action)
        if ("google chrome") in action:
            os.system("start chrome")
            talk("I open chrome")
        elif ("note pad") in action or ("notepad") in action:
            os.system("notepad")
            talk("I'm opening the notepad")
        elif ("chat") in action:
            asyncio.run(ask_bing())
        elif ("stop") in action:
            talk("Good bye")
            exit()
        else:
            print("I did not understand")


if __name__ == "__main__":
    run()
