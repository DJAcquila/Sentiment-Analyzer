#!/usr/bin/env python
import sys
import pickle
from Modules.SentAnalyzer.sentiment import SentAnalyzer
import speech_recognition as sr 

import os

def main():
    a = SetPersistentClassifier()
    print("Welcome to SentAnalyzer\nDescribe your feelings to me, and I will tell you if it's bad or good")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            while True :
                audio = r.listen(source)
                try:
                    sentence = r.recognize_google(audio)
                    print('You said: {}'.format(sentence))
                    if sentence.strip().lower() in ['exit', 'quit']:
                        break

                    sentiment = a.analyze(sentence)
                    if sentiment == 'pos':
                        print("\tThis is good")
                    elif sentiment == 'neg':
                        print ("\tThis is bad")
                 
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
