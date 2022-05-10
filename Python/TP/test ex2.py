Fact = 1
N = 6
if N<= -1 :
    print("Impossible d'afficher une valeur négative")
    N = input()
Resultat = ""
#i = 1
for i in range(1,7):
    Fact = Fact * i
Resultat = str(Fact)
print("La factorielle de " + str(N) + " est " + Resultat)
print(N)
print(type(N))