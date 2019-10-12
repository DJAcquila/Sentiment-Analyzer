import speech_recognition as sr 
from queue import Queue
import threading
import time
from multiprocessing.pool import ThreadPool


class Listener:
	def __init__(self):
		self.r = sr.Recognizer()
		self.hello = False
		self.audio = None
		self._output = ''

	def getHello(self):

		print ('\nSay hello to start a conversation\n')
		while True:
			if self.hello is False:
				#audio = self.audio_queue.get()
				#self.audio_queue.task_done()
				audio = self.audio
				self.audio = None
				try:
					text = self.r.recognize_google(audio)
					print('getHello - You said: {}'.format(text))
					if text == 'hello' and self.hello is False:
						self.hello = True
				except Exception as e:
					pass

	def captureSentence(self):
		
		while True:
			if self.hello is True:
				audio = self.audio
				self.audio = None
				try:
					text = self.r.recognize_google(audio)
					print('captureSentence - You said: {}'.format(text))
					if (text == 'bye' or text == 'bye-bye' or text == 'goodbye'):
						self.hello = False
					else:
						self._output = text
				except Exception as e:
					pass
	
	def start(self):
		pool = ThreadPool(processes=2)
		r_getHello = pool.apply_async(self.getHello, ())
		r_captureSentence = pool.apply_async(self.captureSentence, ())


		with sr.Microphone() as source:
			try:
				while True:
					self.audio = self.r.listen(source)
					
			except KeyboardInterrupt:
				pass
	
	def getOutput(self):
		output = self._output
		self._output = ''
		return output

if __name__ == '__main__':
	lis = Listener()
	lis.start()