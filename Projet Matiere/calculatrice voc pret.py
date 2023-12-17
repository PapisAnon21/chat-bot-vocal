#le programme marche a 100 pour cent
import speech_recognition as sr
import pyttsx3
import math
reconnaitre = sr.Recognizer()
parleur = pyttsx3.init()
demarrer = 'o'

while demarrer == 'o' or demarrer == 'O':
  print(30*'_')
  print("Calculatrice Vocale a demarré\n Parlez maintenant")
  with sr.Microphone() as son:
    audio = reconnaitre.listen(son)
    try:
    	texte = reconnaitre.recognize_google(audio , language ="fr-FR")
    	print(texte)
    	texte = texte.replace('x','*')
    	resultat = eval(texte)
    	parleur.say(resultat)
    	parleur.runAndWait()
    	print(resultat)
    except:
    	parleur.say("je n'ai pas compris, reessayez encore s'il vous plait!")
    	parleur.runAndWait()
    	print("je n'ai pas compris")
    	reessayez = input("Voulez vous reessayez: 'O' ou 'N'")	
    	if reessayez == 'O' or reessayez == 'o':
    		demarrer ='o'
    	else:
    		demarrer = 'n'
print('\t\t\t\tfin du programme ')	  


'''
Dans cette partie je ne savais pas encore l'existence de la fonction eval qui permet de calculer les 
chaine de caractères
import math
chaine = '2+85-24*36-45'
prod = []
chaine = chaine.replace('-','+-')
chaine = chaine.split('+')
print(chaine)
liste_pour_prod = []
for nombre_intrus in chaine:
  if '*' in nombre_intrus:
  	c = nombre_intrus
  	chaine.remove(nombre_intrus)
  	#print(c)
  	f = nombre_intrus.split("*")
  	for les_facteur in f:
  		liste_pour_prod.append(float(les_facteur))
  		resultat = math.prod(liste_pour_prod)
  	chaine.append(resultat)	
  
liste_entier = []
for d in chaine:
	c = int(d)
	liste_entier.append(c)
  		

liste_entier.append(resultat)
print(liste_entier) 


    		

#d = math.fsum(chaine)
#print(d) 		


#resultat = math.fsum(chaine)
#print(resultat)
#for w in range(0,len(chaine)):
  #if chaine[w] == '*':
'''
			  		  	
