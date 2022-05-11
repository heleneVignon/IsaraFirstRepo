from tkinter import *
from tkinter.messagebox import *
def calculate():
    Fact = 1
    N = input()
    try :
        if N<= -1 :
            print("Impossible d'afficher une valeur négative")
            N = input()
        Resultat = ""
    #i = 1
        for i in range(1,N+1):
            Fact = Fact * i
        Resultat = str(Fact)
        print("La factorielle de " + str(N) + " est " + Resultat)
        print("la valeur de N est " + str(N))
        print(type(N))
    except :
        print("Impossible de rentrer du texte")
        N = input()
fenetre = Tk()
label = Label(fenetre, text="Entrer un nombre entier")
label.pack()
value = StringVar() 
value.set("texte par défaut")
entree = Entry(fenetre, textvariable=str(), width=30)
entree.pack()
calculate_bouton=Button(fenetre, text="Exécuter", command=calculate)
calculate_bouton.pack()
fenetre.mainloop()
