import speech_recognition as sr
reconnaitre = sr.Recognizer()
"""import speech_recognition as sr
#import pyttsx3
import math

#from pydub import AudioSegment
#from pydub.silence import split_on_silence
#import pyaudio


with sr.Microphone as son:
	son_recuperer = reconnaitre.listen(son)
	son_recuperer.play()
"""

def record_sound():
	"""
	Cette fonction ecoute le son de l'utiilisateur
	et nous renvoi ce son sous format objet python
	bon objet python ou tout ce q vous voulez
	"""
	with sr.Microphone() as son:
		son_recuperer = reconnaitre.listen(son)
		return son_recuperer


A = record_sound()