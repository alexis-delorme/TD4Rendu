import time
from main import*


###  Définitions des variables ###
#   S = Liste des valeurs disponible (en centimes). ex : 
S = [1,2,5,10,20,50,100,200,500]  # les valeurs sont 1 centimes, 2 centimes... jusqu'à 500 centimes

#   T = Combinaison des valeurs utilisé. ex :
T = [0, 2, 4, 5, 6]     #la valeur S[0] est utilisée 0 fois, S[1] deux fois, S[3] quatre fois etc.

#   M = Montant que l'on cherche à rendre. Uniquement des nombres entiers. ex :
M = 1045    #1045 centimes --> 10euros 45 centimes

#   D = Liste des disponibilités corréspondant à des valeurs dans la liste S
D = [1, 3, 4, 12, 4]     #il en reste 1 pièce de la valeur S[0], 3 de la valeur S[1], 12 de la valeur S[3] etc.

####    Méthode Gloutonne   #####

M=0                                                    
D=[3,4,3,5,3,2,5,6,7,11,2,12,1]                         
Q=0
QOptimal=0

print('~~~ Tests pour vérifier la fonctionnement de la méthode Gloutonne ~~~')
S = [1,2,5,10,20,50,100,200,500,1000,2000,5000,10000]     
M = 23665                                                 
test1=Monnaie_Gloutonne(S,M)
print(test1)

print('\n')
print('Test du cas où la méthode Gloutonne n\'est pas optimale')
S = [1,7,23]
M = 28
test2 = Monnaie_Gloutonne(S,M)
print(test2)

print('\n')
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
print('Test d\'un cas où il n\'y a aucune combinaison possible pour le montant M')
S = [100,300,450,646,1500] 
D = [0,10,6,5,3]
M = 12001
test5 = Monnaie_Gloutonne_Modifie(S,M,D)
print(test5)


print('\n')
print('~~~ Tests pour vérifier la fonctionnement de la méthode de l\'arbre ~~~')
S = [1,10,200,300,4000]
M = 4654
start = time.time()
test6 = Monnaie_Graphe(S,M)
Qopt = Q_Optimal(test6,S,M)
end = time.time()
print('Temps écoulé = ', end - start, 'seconds')
print(Qopt)

print('\n')
print('Test du cas où la méthode Gloutonne a échouée')
S = [1,7,23]
M = 28
test7 = Monnaie_Graphe(S,M)
print(Q_Optimal(test7,S,M))

##  print('\n')
##  print('Test de la méthode Graph_arbre qui dessine l\'arbre')
##  #   Enlève les ## pour sauvegarder et afficher l'arbre sous fichier .png
##  #Graph_Arbre(test7)


print('\n')
print('~~~ Tests pour vérifier la fonctionnement de la méthode Programmation Dynamique ~~~')
S = [1,10,200,300,4000]
M = 4654
start1 = time.time()
test8 = Monnaie_dynamique(S,M)
end1 = time.time()
print('Temps écoulé = ', end1 - start1, 'seconds')
print('Combinaison optimale (QOpt) :', test8)

print('\n')
print('Test d\'un cas avec un nombre des combinaisons important')
S = [1,2,5,10,20,50,100,200,500,1000,2000,5000,10000]
M = 23665
start2 = time.time()
test9 = Monnaie_dynamique(S,M)
end2 = time.time()
print('Temps écoulé = ', end2 - start2, 'seconds')
print('Combinaison optimale (QOpt) :', test9)

print('\n')
print('~~~ Tests pour vérifier la fonctionnement de la méthode Programmation Dynamique modifié ~~~')
S = [1,10,200,300,4000]
M = 4654
start3 = time.time()
test10 = Monnaie_dynamique_modifie(S,M)
end3 = time.time()
print('Temps écoulé = ', end3 - start3, 'seconds')
#print('Matrice finale : ',test10[0])
print('Combinaison optimale (QOpt) :', test10[1])
print('Liste des pièces utilisées :', test10[2])
complexite = Complexite(test10[0])
print(complexite)


