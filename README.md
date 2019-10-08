# Sentiment-Analyzer
A text sentiment Analyzer written in Python 3
## Dependencies
- ```Python 3.6.8```
- The Natural Language Processing library ```NLTK 3.4``` 
## Instalation Guide
Install python3:
```bash 
  $ sudo apt-get update
  $ sudo apt-get install python3.6
```
If you are using Ubuntu 14.04 or 16.04, Python 3.6 is not in the Universe repository, and you need to get it from a Personal Package Archive (PPA):
```bash
  $ sudo add-apt-repository ppa:deadsnakes/ppa
  $ sudo apt-get update
  $ sudo apt-get install python3.6
```
Install pip:
```bash
  $ sudo apt-get install python3-pip
```
Install NLTK: 
```bash 
  $ pip install --user -U nltk 
```
Install numpy:
```bash 
  $ pip install --user -U numpy 
```
For the instalation testing run ```python3``` on terminal and insert ```import nltk```

To download the needed data, type the following on terminal:
```bash 
 $ python -m nltk.downloader movie_reviews punkt
```
## Running the code
To run the script you can type ```python3 main.py``` on terminal and follow the instructions during the execution.
