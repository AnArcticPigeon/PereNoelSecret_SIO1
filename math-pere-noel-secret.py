import random



nb_personne = int(input("Saisir le nombre de personne présente a la soirée: "))





def tirage(nb_personne):
    print("Il y a",nb_personne-1,"possibilitées possible")
    print("Le nombre de possibilitée totale est de",(nb_personne-1),"possibilitées")

#merci google
def countDer(n):
     
    # Base cases
    if (n == 1): return 0
    if (n == 2): return 1
     
    # countDer(n) = (n-1)[countDer(n-1) + der(n-2)]
    return (n - 1) * (countDer(n - 1) +
                      countDer(n - 2))
 
# Driver Code
n = 4
print("Count of Derangements is ", countDer(nb_personne))



def permutation(nb_personne):
    nb_permutation = 1

    for i in range(nb_personne):
        nb_permutation = nb_permutation * (i+1)
    print("Il y a",nb_permutation,"possible")

permutation(nb_personne)


def tirage_compliquer(nb_personne):
    

    nb = 1
    l_cadeau_tire = []
    l_cadeau2 = []
    #boucle pour chaque persone
    for i in range(nb_personne):
        p = True
        l_cadeau = []
        l_cadeau.append(i+1)
        #boucle tant que le cadeau tire est celui de la persone ou un deja tire
        while(nb == i+1 or p == True):
            nb = random.randrange(1,nb_personne+1)
            if nb in l_cadeau_tire:
                p = True
            else:
                p = False

        l_cadeau.append(nb)
        l_cadeau2.append(l_cadeau)
        l_cadeau_tire.append(nb)
        print(i+1,"a obtenue le cadeau de",nb)
        i=i+1
    print(l_cadeau_tire)
    print(l_cadeau2)
tirage_compliquer(nb_personne)



