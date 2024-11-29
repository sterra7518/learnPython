"""Module de fonctions pour les nombres parfaits et chanceux."""
# fichier : parfait_chanceux_m.py
# auteur : Sofiane Terraf
# imports




from verif_m import verif


# fonctions


"""Retourne la somme des diviseurs propres de <n>."""

def somDiv(n):
	somme = 1
	for i in range(2, n//2+1):
		if n % i == 0:
			somme += i
	return somme


"""Teste si <n> est parfait."""

def estParfait(n):
	return True if somDiv(n) == n else False


"""Teste si <n> est premier."""
def estPremier(n):
	return True if somDiv(n) == 1 else False

"""Teste si <n> est chanceux."""
def estChanceux(n):
	for i in range(0, n-1):
		if not estPremier(n + i + i**2):
			return False
	return True


