# Sentiment-Analyzer
A Sentiment Analyzer for texts using the [Naive-Bayes Classifier](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)
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

## License
MIT License

Copyright (c) 2019 Acquila Santos Rocha

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
