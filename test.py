### imports ###
from main import*

####    Méthode Gloutonne   #####

S=[1,2,5,10,20,50,100,200,500,1000,2000,5000,10000]     ##Liste, valeur de pièces
T=[]                                                    ##Liste, pièces à rendre
M=0                                                     ##Integer, montant à rendre
D=[3,4,3,5,3,2,5,6,7,11,2,12,1]                         ##Liste, disponibilité de chaque valeur 
Q=0
QOptimal=0

print('~~~ Tests pour vérifier la fonctionnement de la méthode Gloutonne ~~~')
S = [1,2,5,10,20,50,100,200,500,1000,2000,5000,10000]     ##Liste, valeur de pièces
M = 23665                                                 ##Int, montant à rendre
test1=Monnaie_Gloutonne(S,M)
print(test1)

print('\n')
print('Test du cas où la méthode Gloutonne n\'est pas optimale')
S = [1,7,23]
M = 28
test2 = Monnaie_Gloutonne(S,M)
print(test2)

print('n')
print('~~~ Tests pour vérifier la fonctionnement de la méthode Gloutonne modifié ~~~')
print('Test d\'un cas où la disponibilité limite le choix qu\'on pourrait faire')
S = [4,7,23] 
D = [3,5,0]
M = 28
test3 = Monnaie_Gloutonne_Modifie(S,M,D)
print(test3)

print('\n')
print('Test d\'un cas où le montant est trop élevé')
S = [1,2,3,4] 
D = [0,1,1,1]
M = 12
test4 = Monnaie_Gloutonne_Modifie(S,M,D)
print(test4)


print('\n')
print('Test d\'un cas où il n\'y a pas assez des pièces disponible')
S = [100,300,450,646,1500] 
D = [0,10,6,5,3]
M = 12001
test5 = Monnaie_Gloutonne_Modifie(S,M,D)
print(test5)


print('\n')
print('~~~ Tests pour vérifier la fonctionnement de la méthode de l\'arbre ~~~')
S = [1,10,200,300,4000]
M = 4654
test6 = Monnaie_Graphe(S,M)
print(Q_Optimal(test6,S,M))

print('\n')
print('Test du cas où la méthode Gloutonne a échouée')
S = [1,7,23]
M = 28
test7 = Monnaie_Graphe(S,M)
print(Q_Optimal(test7,S,M))

print('\n')
print('Test de la méthode Graph_arbre qui dessine l\'arbre')
#   Enlève le # pour sauvegarder et afficher l'arbre soius fichier .png
#Graph_Arbre(test7)


print('\n')
print('~~~ Tests pour vérifier la fonctionnement de la méthode Programmation Dynamique ~~~')
S = [1,7,23]
M = 28
test8 = Monnaie_dynamique(S,M)
print(test8)

print('Test d\'un cas avec un nombre des combinaisons important')
S = [1,2,5,10,20,50,100,200,500,1000,2000,5000,10000]
M = 23665
test9 = Monnaie_dynamique(S,M)
print(test9)


print('~~~ Tests pour vérifier la fonctionnement de la méthode Programmation Dynamique modifié ~~~')
S = [1,10,200,300,4000]
M = 4654
test10 = Monnaie_dynamique_modifie(S,M)
#print('Matrice finale : ',test10[0])
print('Combinaison optimale (QOpt) :', test10[1])
print('Liste des pièces utilisées :', test10[2])
complexite = Complexite(test10[0])
print(complexite)
