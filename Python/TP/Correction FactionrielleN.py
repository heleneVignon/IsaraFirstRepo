# correction
Fact = 1
N = -1
#un contrôle de saisie : boucler tant que N est strictement négatif
while (N < 0) :
    # récupérer la valeur de N
    ch_N = input("Quelle est la factorielle que vous vous calculez ?\n")
    N = int(ch_N)
    # tester si N=0
    if  N < 0 :
        print("Impossible d'afficher une valeur négative\n")
#tester si N > 0
if N > 0 :
    #boucler
    for i in range(1, N+1):
        Fact = Fact * i    
#afficher le résultat 
print("La factorielle de " + str(N) + " est " + str(Fact))
