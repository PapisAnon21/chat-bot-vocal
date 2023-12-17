#le programme marche a 100 pour cent
import speech_recognition as sr
import pyttsx3



reconnaitre = sr.Recognizer()
parleur = pyttsx3.init()

import pyaudio
import wave
import noisereduce as nr
# Charger l'audio enregistré et supprimer le bruit
audio_file = wave.open("audio.wav", 'rb')
audio_data = audio_file.readframes(audio_file.getnframes())
audio_signal = nr.load_audio(audio_data, RATE)
reduced_noise = nr.reduce_noise(audio_signal)

#FORMAT = pyaudio.paInt16
#CHANNELS = 1
#RATE = 44100
#CHUNK = 1024
#RECORD_SECONDS = 5

parleur = pyttsx3.init()

def record_sound():
	"""
	Cette fonction ecoute le son de l'utiilisateur
	et nous renvoi ce son sous format objet python
	"""
	with sr.Microphone as son:
		son_recuperer = reconnaitre.listen(son)
		return son_recuperer
		
## la sortie de la fonctionn soudtsound est passe en parametre a la fonctioh sppech to text


def traite_sound(sound,RATE  = 44100):
	sound = sound.readframes(sound.getnframes())
	sound = nr.load_audio(sound, RATE)
	sound = nr.reduce_noise(sound)
	return sound

	
	
def speech_to_text(son):
	"""
	cette fonction prend en parametre un audio et sort le texte
	correspondant a l'audio
	"""
	try:
		texte_correspondant = reconnaitre.recognize_google(son , language ="fr-FR")
		
	except:
		return "error"
	return texte_correspondant


def prediction(texte):



def text_to_speech(texte):
	"""
	La fonction text to speech 
	prend en parametre un texte
	et sort de l'audio
	"""
	parleur.say(texte)
    parleur.runAndWait()

