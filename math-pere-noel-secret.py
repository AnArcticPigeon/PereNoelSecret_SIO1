import random,math



nb_personne = int(input("Saisir le nombre de personne présente a la soirée: "))
permutations = input("Voulez vous créer une liste de toute les permutation possible: oui/non: ")




def tirage(nb_personne):
    print("Il y a",nb_personne-1,"possibilitées possible")
    print("Le nombre de possibilitée totale est de",(nb_personne-1),"possibilitées")

#merci google
def countDer(n):
     
    # Base cases
    if (n == 1): return 0
    if (n == 2): return 1
     
    #countDer(n) = (n-1)[countDer(n-1) + der(n-2)]
    return (n - 1) * (countDer(n - 1) +
                      countDer(n - 2))
 
# Driver Code
n = 4
#print("Count of Derangements is ", countDer(nb_personne))


#merci chatGPT
def subfactorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 0
    else:
        return (n-1) * (subfactorial(n-1) + subfactorial(n-2))

#print(subfactorial(6))









def permutation(nb_personne):
    nb_permutation = 1

    for i in range(nb_personne):
        nb_permutation = nb_permutation * (i+1)
    print("Il y a",nb_permutation,"permutation possible pour ",nb_personne,"invitées")
    return nb_permutation


def tirage_compliquer(nb_personne,nb_permutation,permutations):
    l_permutation = []
    l_derangement = []
    numTour=1
    
    #boucle tant que l'on a pas fait toute les possibilitée de permutation possible
    while(len(l_derangement) < nb_permutation):
        
        print("tour:",numTour)
        print("nombre actuelle de derangements trouvée:",len(l_derangement))
        print(nb_permutation)
        l_cadeau2 = []
        l_cadeau_tire = [0]
        
        

        #boucle donant un cadeau unique a chaque persone
        for i in range(nb_personne):
            nb = 0
            l_cadeau = []
            
            #boucle tant que le cadeau tire est celui de la persone ou un deja tire
            if(permutations == "oui"):
                while(nb in l_cadeau_tire):
                    nb = random.randrange(1,nb_personne+1)
            else:
                while(nb in l_cadeau_tire or nb == i+1):
                    nb = random.randrange(1,nb_personne+1)


                '''
                if(nb == nb_personne and nb not in l_cadeau_tire):
                    y = True
                    break
                else:
                    y = False
                '''

            l_cadeau_tire.append(nb)
            l_cadeau.append(i+1)
            l_cadeau.append(nb)
            l_cadeau2.append(l_cadeau)
            print(i+1,"a obtenue le cadeau de",nb)
            i=i+1
            
        if(l_cadeau2 not in l_permutation):
            l_permutation.append(l_cadeau2)

        numTour = numTour + 1

    print(l_derangement)
    print("Il y a ",len(l_permutation),"permutation possible")
    print("Il y a ",len(l_derangement),"derangement possible")
    
tirage_compliquer(nb_personne,permutation(nb_personne),permutations)



