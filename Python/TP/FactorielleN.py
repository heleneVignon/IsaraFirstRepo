try :
    Fact = 1
    N = blabla
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
