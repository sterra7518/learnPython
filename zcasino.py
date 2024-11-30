#Insertion des modules

import random
from math import ceil



#Valeurs de départ

partie = True
somme = 1000

print("Vous vous installez à la table de roulette avec", somme, "$.")


#Déroulement du jeu 

while partie == True:


	# Vérification du montant à miser

	mise_somme = -1
			
	while mise_somme < 0 or mise_somme > somme :
	
		mise_somme = int(input("Veuillez choisir le montant a miser  : "))

		try : 
			print ("Vous avez miser {} dollars !".format(mise_somme))

		except ValueError :
			print("On a une abscence de valeur")
			continue
			
		except TypeError:
			print("On a une erreur de compatibilite")
			continue
					
		if mise_somme < 0:
			print("Ce nombre est negatif")			
        
		if mise_somme > somme :
			print("La mise est supérieur au montant de porte feuille")





	#Vérification du numéro de mise

	mise = -1

	while mise < 0 or mise > 50 :

		mise = int(input("Veuillez choisir un numero : "))

		try : 
			print ("Vous avez miser le numéro {}.".format(mise))

		except ValueError :
			print("On a une erreur de mise")
			continue 

		except TypeError:
			print("On a une erreur de compatibilite")
			continue

		if mise < 0:
			print("Ce nombre est negatif")

		if mise > 49:
			print("Ce nombre est superieur à 49")
			





#Le numéro gagnant 

	num_gagnant = random.randint(0,49)

	print("La roulettre tournee ... et le numero gagnant est {}".format(num_gagnant))

	if mise == num_gagnant : 
		somme += (mise_somme * 3)
		print("Vous avez trouver le bon numero ! La somme est de {} dollars ! ".format(somme))
		
	elif mise%2 == num_gagnant%2 :
		somme += ceil(mise_somme*0.5)
		print("Vous avez trouver la meme couleur ! La somme est de {} dollars ! ".format(somme))

	else :
	    somme -= mise_somme 
	    print("Je suis désoler, vous avez perdu ! Il vous reste {} dollars !".format(somme))




#Si le montant est nulle ou négatif?

	if somme <= 0 :		
		partie = False
		break
		print("Desoler ! Vous ne pouvez plus continuer a jouer ! Il vous reste {} dollars".format(somme))



#Si volonter à jouer en continue

	print("On a {} dollars dans votre poche ! ".format(somme))
	suite = input("Souhaitez-vous continuer a jouer ? (o/n) : ")
	if suite == 'N' or suite == "n":
		print("Vous quittez la partie avec {} dollars".format(somme))
		partie = False 
		break

print("Fin de jeu ! Merci de votre participation !")
