## speech to texte


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