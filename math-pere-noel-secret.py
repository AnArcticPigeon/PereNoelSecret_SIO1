import random

def tirage():
    nb_persone = int(input("Saisir le nombre de personne présente a la soirée: "))
    print("Il y a",nb_persone-1,"possibilitées possible")
    print("Le nombre de possibilitée totale est de",(nb_persone-1),"possibilitées")



def permutation():
    nb_persone = int(input("Saisir le nombre de personne présente a la soirée: "))
    nb_permutation = 1
    for i in range(nb_persone):
        print(nb_permutation,"x",i+1)
        nb_permutation = nb_permutation * (i+1)


    print("Il y a",nb_permutation,"possible")

permutation()


def tirage_compliquer():
    nb_persone = int(input("Saisir le nombre de personne présente a la soirée: "))

    nb = 1
    l_personne = [1,2,3,4,5,6]
    l_cadeau_tire = []
    for c in l_personne:
        p = True
        while(nb == c or p == True):
            nb = random.randrange(1,nb_persone)
            if nb in l_cadeau_tire:
                p = True
            else:
                p = False
                print(nb)
        print(c,"a obtenue le cadeau de",nb)
        l_cadeau_tire.append(nb)
        




    

