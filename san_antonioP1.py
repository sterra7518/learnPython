#### IMPORTATIONS DES MODULES ###

import random

import json




#### VARIABLES DE DEPARTS ###


#Liste de citations
quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

#Liste de noms de livres
characters = [
    "alvin et les Chipmunks", 
    "Babar", 
    "betty boop", 
    "calimero", 
    "casper", 
    "le chat potté", 
    "Kirikou"
]

#Une varible réponse
user_answer = input('Tapez entrée pour découvrir une autre citation ou B pour quitter le programme : ')





### CONDITIONS ###

# Show random quote

if user_answer == "B": 
    pass # - leave the program
elif user_answer == "C":
    print("C pas la bonne réponse ! Et G pas d’humour, je C...")
else:
    # show another quote
    pass




### FONCTIONS ###


#Une fonction permet de choisir au hasard une citation

#**Une fontion pour afficher**

def get_random_quote(mylist):
       
    quote = mylist[0]# get a random number
    print(quote) # show the quote in the interpreter
   
get_random_quote(quotes) #exécution de fonction


#**Une fontion pour retourner**
def get_random_item_in(my_list):
    # TODO: get a random number
    item = my_list[0] # get a quote from a list
    return item # returned value


print(get_random_item_in(quotes))





### BOUCLE WHILE ###

while user_answer != 'B' :
    print(get_random_item_in(quotes))
    user_answer = input('Tapez entrée pour découvrir une autre citation ou B pour quitter le programme : ')
    #pour éviter pour les affichage à l'infini

print(get_random_item_in(quotes))





### BOUCLE FOR ###

#le but est de mettre en majuscule tous les premiers lettres des nom

for i in characters:
    a_list = i.capitalize() #i prend chaque élément de 'characters' pour mettre en majuscule
    print(a_list)



### CHAINE DE CARACTEREs  ###

print(" {} a dit : {}".format(characters[2],quotes[1]))







### DICTIONNAIRES

program = {"quotes": ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", "On doit pouvoir choisir entre s'écouter parler et se faire entendre."],
           "characters": ["alvin et les Chipmunks", "Babar", "betty boop", "balimero", "casper", "le chat potté", "Kirikou"]}

#Element de l'indice
print(program["characters"][0])


#Remplacement de valeur
program["characters"] = "Un nouveau nom"
print(program)


#Mettre a jour 
program.update({"characters" : ["Alvin", "Père Noël"],
                "quotes": ["Une citation unique qui sera sauvegardée"]})

print(program)


#Supprimer la clée
print(program.pop("quotes"))


#Afficher le dictionnaire
print(program)





### CITATIONS ####


def get_random_item_in(my_list):
    rand_numb = random.randint(0,len(my_list)-1)
    item = my_list[rand_numb] # get a quote from a list
    return item # returned value


print(get_random_item_in(quotes))
print(get_random_item_in(characters))






### MODULES "json" ###



#Pour lire le fichier JSON
def read_values_from_json(key):
    values = []
    with open("characters.json") as f:
        data = json.load(f)
        for entry in data:
            values.append(entry["character"])
    return values 



#Pour affichier la citation au hasard du fichier JSON
def random_character():
    all_values = read_values_from_json()
    return get_random_item_in(all_values)






