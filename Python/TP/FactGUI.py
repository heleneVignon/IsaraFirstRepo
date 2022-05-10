try :
    Fact = 1
    N = 5
    N = int(N)
    if N<= -1 :
        print("Impossible d'afficher une valeur négative")
        N = input()
    Resultat = ""
    #i = 1
    for i in range(1,6):
        Fact = Fact * i
    Resultat = str(Fact)
    print("La factorielle de " + str(N) + " est " + Resultat)
    print("la valeur de N est " + str(N))
    print(type(N))
except :
    print("Impossible de rentrer du texte")
    N = input()

from tkinter import * 
fenetre = Tk()
label = Label(fenetre, text="Entrer un nombre entier")
label.pack()
value = StringVar() 
value.set("texte par défaut")
entree = Entry(fenetre, textvariable=str(), width=30)
entree.pack()
bouton=Button(fenetre, text="Exécuter")
bouton.pack()
fenetre.mainloop()
