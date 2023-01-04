import random,math,time


"""
Le but de ce programe est de calculer le nombre de dérangement possible pour un nombre n d'element

Un dérangement d'un ensemble d'éléments est une permutation telle que aucun élément ne reste à sa place initiale.
"""



nb_personne = int(input("Saisir le nombre de personne présente a la soirée: "))
nb_test = int(input("Saisir le nombre de test a effectuer:"))
permu = input("Voulez vous calculez toute les permutations possible ?: oui/non: (Trés lemp!!!) ")


#merci google, algorithme recursif calculant le nombrede derangement pour n elements 
def derangement(n):
    if n == 0:
        return 1
    elif n == 1:
        return 0
    else:
        return (n-1) * (derangement(n-1) + derangement(n-2))


#algorithme reproduisant de maniere "plus naturel" le calcul de derangement, similaire au jeu du père Noël secret, le programe choisit qui recoit le cadeau de qui de maniere aléatoire



def tirage_compliquer(nb_personne,nb_permutation,permu):
    start_time = time.time()
    l_permutation = [] #liste contenant toute les permutation trouvée
    l_derangement = [] #liste contenant toute les derangements trouvée
    numTest=1
    
    while(numTest <= nb_test):

        print("Test:",numTest,"/",nb_test)
        l_derangement_u = aleatoire(permu,nb_personne)

        #si la permutation actuelle n'est pas deja presente dans la liste de tout les permutations, alors on l'ajoute
        if(l_derangement_u not in l_permutation):
            l_permutation.append(l_derangement_u)
            l_permutation.sort()

        #si le derangement actuelle n'est pas deja present dans la liste de tout les derangement, alors on l'ajoute
        if(l_derangement_u not in l_derangement):
            l_derangement.append(l_derangement_u)
            l_derangement.sort()


        numTest = numTest + 1

    #print(l_derangement)
    if(permu == "oui"):
        print("L'algorithme a trouver",len(l_permutation),"/",nb_permutation,"des permutations possible pour",nb_personne,"personnes lors de ses",nb_test,"tests")
    else:
        print("L'algorithme a trouver",len(l_derangement),"/",derangement(nb_personne),"des derangements possible pour",nb_personne,"personnes lors de ses",nb_test,"tests")
    print("        Temp d'éxecution")
    print("--- %s seconds ---" % (time.time() - start_time))


#algo calculant le nombre de permutation totale de maniere non aléatoire
def permutation(nb_personne):
    nb_permutation = 1

    for i in range(nb_personne):
        nb_permutation = nb_permutation * (i+1)
    return nb_permutation

#algo s'occupant de la partie "tirage au sort" du programe, executer a chaqu'un des tests
def aleatoire(permutations,nb_personne):
    l_derangement_u = [] #liste_derangement_unitaire , contient le derangement trouver ce test
    l_cadeau_tire = [0] #liste_cadeau_tire, contient les numero ayant deja etait tirée dans ce test ("les cadeaux ayant deja etait donnée a une autre personne")

    #boucle donant un cadeau unique a chaque persone
    for i in range(nb_personne): 
        nb = 0
        
        #si on active le calcul de toute les permutations le code retire un nouveau cadeau uniquement si le cadeau a deja etait tirée
        if(permutations == "oui"):
            #boucle tant que le cadeau tire a deja etait tirée
            while(nb in l_cadeau_tire):
                nb = random.randrange(1,nb_personne+1)

        else:
            #boucle tant que le cadeau tire est celui de la persone ou un deja tire
            while(nb in l_cadeau_tire or nb == i+1):
                if(nb == nb_personne and nb_personne == i+1):
                    return aleatoire(permutations,nb_personne) #relance le test si jamais on arrive a la "derniere personne de la liste" mais que le seule cadeau restant est celui de cette meme personne
                else:
                    nb = random.randrange(1,nb_personne+1)

        l_cadeau_tire.append(nb)
        l_derangement_u.append(nb)
        #print(i+1,"a obtenue le cadeau de",nb)
        i=i+1
    l_derangement_u = int("".join(map(str,l_derangement_u)))
    return l_derangement_u
        

      
tirage_compliquer(nb_personne,permutation(nb_personne),permu)



