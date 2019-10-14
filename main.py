#!/usr/bin/env python
import sys
import pickle
from Modules.SentAnalyzer.sentiment import SentAnalyzer
import speech_recognition as sr 
import pyaudio
import os

def main():
    a = SetPersistentClassifier()
    print("Welcome to SentAnalyzer\nDescribe your feelings to me, and I will tell you if it's bad or good")
    r = sr.Recognizer()

    with sr.Microphone() as source:
        try:
            while True :
                audio = r.listen(source,timeout=3, phrase_time_limit=3)
                try:
                    sentence = r.recognize_google(audio)
                    print('You said: {}'.format(sentence))
                    if sentence.strip().lower() in ['exit', 'quit']:
                        break

                    if sentence.strip().lower() not in ["hello", "hi", "what's up", "hey", "what's your name", "your name", "name", "how are you"]:
                        sentiment = a.analyze(sentence)
                        if sentiment == 'pos':
                            print("Psychorobot: This is good\n")
                        elif sentiment == 'neg':
                            print("Psychorobot: This is bad\n")

                    elif sentence.strip().lower() in ["hello", "hi", "what's up", "hey"]:
                        print("Psychorobot: Hey!\n")

                    elif sentence.strip().lower() in ["what's your name", "your name", "name"]:
                        print("Psychorobot: My name is Psychorobot\n")

                    elif sentence.strip().lower() in ["how are you"]:
                        print("Psychorobot: I am angry and tired\n")

                 
                except Exception as e:
                    pass
        except KeyboardInterrupt:
            pass       


def SetPersistentClassifier():
    try:
        with open('SentAnalyzer.classifyer', 'rb') as file:
            a = pickle.load(file)
    except (IOError, pickle.PickleError):
        print ("First use of the analyzer\nPlease wait until the classifier is trained")
        a = SentAnalyzer()
        a.train()
        print("Training concluded with {} of accuracy".format(a.accuracy()))
        with open('SentAnalyzer.classifyer', 'wb') as file:
            pickle.dump(a, file)
    return a

if __name__ == '__main__':
    main()
