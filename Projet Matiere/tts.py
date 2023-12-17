import pyttsx3
parleur = pyttsx3.init()



def text_to_speech(texte):
	"""
	La fonction text to speech 
	prend en parametre un texte
	et sort de l'audio
	"""
	parleur.say(texte)
    parleur.runAndWait()