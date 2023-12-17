
# cette librairie comporte la fonction permettant d'enlever le bruit d'un signal

def traite_sound(sound,RATE  = 44100):
	"""
	la fonction traite soud
	prend en parametre l'objet son a traiter ainsi que 
	le RATE a vrai dire je ne sais meme pas ce que c 
	rate
	peut etre c la frequence
	en sortie elle retourne sound debruite
	"""
	sound = sound.readframes(sound.getnframes())
	sound = nr.load_audio(sound, RATE)
	sound = nr.reduce_noise(sound)
	return sound