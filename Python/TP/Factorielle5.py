# la factorielle est 5! = 5 x 4 x 3 x 2 x 1
# 1 : boucle for car on connait le nb de tours de la boucle
Fact = 1
N = 0
Resultat = ""
#i = 1
for i in range(1,6,1):
    Fact = Fact * i
Resultat = str(Fact)
print("La factorielle de " + str(N) + " est " + Resultat)

#exercice 2