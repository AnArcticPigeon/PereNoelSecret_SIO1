import random,math



nb_personne = int(input("Saisir le nombre de personne présente a la soirée: "))
nb_test = int(input("Saisir le nombre de test a faire:"))



def tirage(nb_personne):
    print("Il y a",nb_personne-1,"possibilitées possible")
    print("Le nombre de possibilitée totale est de",(nb_personne-1),"possibilitées")



#merci google
def derangement(n):
    if n == 0:
        return 1
    elif n == 1:
        return 0
    else:
        return (n-1) * (derangement(n-1) + derangement(n-2))

#print(derangement(6))





def permutation(nb_personne):
    nb_permutation = 1

    for i in range(nb_personne):
        nb_permutation = nb_permutation * (i+1)
    return nb_permutation

def aleatoire(permutations,nb_personne):
    l_cadeau2 = []
    l_cadeau_tire = [0]

    #boucle donant un cadeau unique a chaque persone
    for i in range(nb_personne,):
        nb = 0
        l_cadeau = []
        
        #boucle tant que le cadeau tire est celui de la persone ou un deja tire
        if(permutations == "oui"):
            while(nb in l_cadeau_tire):
                nb = random.randrange(1,nb_personne+1)
        else:
            while(nb in l_cadeau_tire or nb == i+1):
                if(nb == nb_personne and nb_personne == i+1):
                    return aleatoire(permutations,nb_personne)
                else:
                    nb = random.randrange(1,nb_personne+1)

        l_cadeau_tire.append(nb)
        l_cadeau.append(i+1)
        l_cadeau.append(nb)
        l_cadeau2.append(l_cadeau)
        #print(i+1,"a obtenue le cadeau de",nb)
        i=i+1
    return l_cadeau2

def tirage_compliquer(nb_personne,nb_permutation):
    permutations = input("Voulez vous créer une liste de toute les permutation possible: oui/non: ")
    l_permutation = []
    l_derangement = []
    numTour=1
    
    #boucle tant que l'on a pas fait toute les possibilitée de permutation possible
    while(numTour < nb_test):
        
        print("tour:",numTour,"/",nb_test)
        l_cadeau2 = aleatoire(permutations,nb_personne)
            
        if(l_cadeau2 not in l_permutation):
            l_permutation.append(l_cadeau2)
        if(l_cadeau2 not in l_derangement):
            l_derangement.append(l_cadeau2)
        numTour = numTour + 1
        
    #print("Il y a ",len(l_permutation),"permutation possible")
    print(l_derangement)
    print("Il y a",nb_permutation,"permutations possible pour ",nb_personne,"invitées")
    print("L'algorithme a trouver",len(l_derangement),"derangements possible avec",nb_personne,"personnes presente lors de ses",nb_test,"tests")
    print("Il y a ",derangement(nb_personne),"derangements possible")
    
tirage_compliquer(nb_personne,permutation(nb_personne))



