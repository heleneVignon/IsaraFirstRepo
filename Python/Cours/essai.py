t = "une phrase "
# on récupère la taille de la chaine
taille_t = len(t)
mess = "Python, c'est cool!"
# # on récupère la taille de la chaine
taille = len(mess)
print("La chaîne est de taille " + str(taille))
print("Quel est ton prénom?")
prenom = input()
print("Bonjour" + prenom + "!")
print("entrer un nombre")
nombre = input()
print(nombre)
nombre2 = int(nombre) + 5
print(str(nombre2))
l1 = [1.2, 4.0, -5.1,8.6, -3.7]
i = 2
# on récupere l'élament d'indice 2 dans une variable elt
elt = l1[i]
# on affiche dans la console
print(elt)
#on affiche l'élément d'indice 0 dans la console
print(l1[0])
ch = "Une chaîne est une séquence"
premLettre = ch[0]
print("La première lettre est" + premLettre)
mot = "informatique"
debutMot = mot[:4]
milieuMot = mot[5:7]
finMot = mot[5:]
print(debutMot)
print(milieuMot)
print(finMot)
range(1,5,1)
interv = range(1,5)
list1 = ["titi","tata","tot"]
mot = "Python"
print(len(interv))
print(len(list1))
print(len(mot))
for i in range(1,5) :
    double = i*2
    print("Le double de " + str(i) + " est " + str(double))
rep = "O"
while (rep == "O") :
    nb = input("Donnez un nombre entier \n")
    double =int(nb) * 2
    print("Le double de " + str(nb) + " est " + str(double))
    rep = input("Voulez-vous continuer ? (O/N) \n")
    
    
    