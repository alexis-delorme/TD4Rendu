import math
from graphviz import Digraph

graph = Digraph(comment='Arbre',format='png')       ##Prepation de la graphe avec Digraph qui vient de graphviz
graph.attr(size='50,50!')

##La fonction de la méthode Gloutonne
#En entrée : la liste des valeurs S, le montant M
#Conditions initiales : - Pour avoir une solution pour chaque montant M il faut que S commence à 1.
#                       - Le montant M doit être un nombre entier
def Monnaie_Gloutonne(S,M):
    Mprim = M
    T=[0]*len(S)
    while Mprim != 0:    #Condition pour ne pas arrêter avant que le montant est rendu
        for idx, valeur in reversed(list(enumerate(S))):    #On parcourt l'inverse de la liste S
            if valeur <= Mprim:                             #Condition pour arrêter à la valeur de la pièce maximale
                T[idx] = Mprim // valeur                    #On garde le quotient de la division euclidienne dans la liste T
                Mprim = Mprim % valeur                      #On soustrait le reste depuis le montant Mprim
    QOptimal = sum(T)
    return f"Montant à rendre : {M}, Liste des pièces utilisées : {T}, Nombre des billets/pièces optimal : {QOptimal}"

##La fonction de la méthode Gloutonne modifié pour tenir compte de la disponibilité
#En entrée: la liste des valeurs S, le montant M et la liste des disponibilités D
#Conditions initiales : - Le montant M doit être un nombre entier
#                       - La liste D doit être de la même taille que la liste S
def Monnaie_Gloutonne_Modifie(S,M,D):
    Mprim = M
    T=[0]*len(S)
    Total = 0                               
    for idx, valeur in list(enumerate(S)):  #On parcourt l'inverse de la liste S
        Total += valeur*D[idx]
    if Total < M:                           #Condition pour arrêter si le montant est trop élevé
        return f"Insuffisament des billets/pièces... Montant total = {Total}"

    while Mprim != 0 and D[0] > 0:  #On rajoute la condition D[0]>0 pour arrêter si il n'y a plus de pièces pour la valeur minimale
        for idx, valeur in reversed(list(enumerate(S))):
                dispo = D[idx]
                nbBillets = Mprim // valeur
                if nbBillets <= dispo:          #Le cas où on supprime que le nombre de pièces utilisé
                    Mprim = Mprim % valeur
                    T[idx] = nbBillets          #On garde combien de fois de la valeur a été utilisé dans la liste T
                    D[idx] = dispo - nbBillets  
                else:                           #Sinon, on supprime le dispo entièrement dans la liste D
                    T[idx] = dispo
                    Mprim = Mprim - valeur*dispo
                    D[idx] = 0
    QOptimal = sum(T)
    if Mprim != 0 and D[0] == 0:    #Lorsque D[0]=0 on sorte du loop while et on vérifie si tout le montant a été rendu
        return f"Rendu impossible, aucune combinaison des billets trouvé pour ce montant"
    return f"Liste des pièces : {T}, Nombre des billets/pièces optimal : {QOptimal}, Disponibilité de pièces : {D}"


## La fonction de la méthode du chemin minimale d'arbre
#En entrée : la liste des valeurs S, le montant M
#Conditions initiales : - Pour avoir une solution pour chaque montant M il faut que S commence à 1.
#                       - Le montant M doit être un nombre entier
def Monnaie_Graphe(S,M):
    FileF = []          #Création de la file d'attente
    FileF.append(M)
    Noeuds = [M]       
    ArbreA = [[M,[]]]       #Création de l'arbre
    while FileF != []:      #Condition pour arrêter si la file d'attente est vide
        Parent = FileF[0]
        for valeur in S:
            noeud = Parent - valeur     #Chaque noeud représent un montant Mprim < M
            if valeur < Parent:
                if noeud not in Noeuds:
                    Noeuds.append(noeud)
                    ArbreA.append([noeud, [Parent]])
                    FileF.append(noeud)
                else:
                    index = [y[0] for y in ArbreA].index(noeud)
                    ArbreA[index][1].append(Parent)
            if noeud == 0:                      #Si on a trouvé un chemin qui vient d'arriver au montant Mprim=0 on arrête
                ArbreA.append([0,[Parent]])
                return ArbreA, Noeuds
        FileF.pop(0)                        #"Réinitialisation" de la file d'attente
    return (ArbreA, Noeuds)

##Fonction pour calculer la combinaison optimale
#En entrée : Le tuple avec l'arbre et les noeuds produit avec la fonction Monnaie_Graphe, S et M
#Conditions initiales : même que pour Monnaie_Graphe
def Q_Optimal(arbre_noeuds, S, M):
    arbre = arbre_noeuds[0]
    temp=0
    T = [0]*len(S)
    while M != 0:           #Parcours de l'arbre
        temp1 = temp
        index = [y[0] for y in arbre].index(temp)
        if index == 0:
            return f"Liste des pièces utilisées optimale : {T}"
        temp = arbre[index][1][0]
        M -= temp
        valeur = S.index(temp - temp1)
        T[valeur] += 1
    return f"Liste des pièces utilisées optimale : {T}"


##Fonction pour dessiner l'arbre
#En entrée : Le tuple avec l'arbre et les noeuds produit avec la fonction Monnaie_Graphe
def Graph_Arbre(arbre_noeuds):
    arbre = arbre_noeuds[0]
    for liens in arbre:     #On parcourt chaque lien dans l'arbre
        Parents = liens[1]      #On identifie les noeuds et les parents
        noeud = str(liens[0])   
        for parent in Parents:
            graph.edge(str(parent), noeud, label=str(parent - int(noeud)))      #Création avec graphviz
    print(graph.source)
    graph.render('Arbre.gv', view=True)     #Nom de la sauvegarde, view=true affiche l'arbre


##Fonction de la méthode de Programmation Dynamique
#En entrée : la liste des valeurs S, le montant M
#Conditions initiales : - Pour avoir une solution pour chaque montant M il faut que S commence à 1.
#                       - Le montant M doit être un nombre entier
def Monnaie_dynamique(S,M):
    Szero=S
    Szero.insert(0,0)
    w, h = M+1, len(Szero)
    mat = [[0 for x in range(w)] for y in range(h)]         #Création de la matrice mat[S][M]
    for i in range(len(Szero)):
        for m in range(M+1):
            temp = []
            if i == 0:
                mat[i][m] = float('inf')
            elif m == 0:
                mat[i][m] = 0
            else:
                if m - Szero[i] >= 0:
                    temp.append(1 + mat[i][m - Szero[i]])
                else:
                    temp.append(float('inf'))
                if i >= 1:
                    temp.append(mat[i-1][m])
                else:
                    temp.append(float('inf'))
                mat[i][m] = min(temp)
    return mat[i][m]           #La combinaison minimale pour le montant M se trouve en bas à droite dans la matrice

##Fonction de la méthode de Programmation Dynamique modifiée
#En entrée : la liste des valeurs S, le montant M
#Conditions initiales : - Pour avoir une solution pour chaque montant M il faut que S commence à 1.
#                       - Le montant M doit être un nombre entier
def Monnaie_dynamique_modifie(S,M):
    T = [0]*len(S)
    w, h = M+1, len(S)+1
    mat = [[0 for x in range(w)] for y in range(h)] 
    for i in range(len(S)+1):
        for m in range(M+1):
            temp = []
            if i == 0:
                mat[i][m] = float('inf')
            elif m == 0:
                mat[i][m] = 0
            else:
                if m - S[i-1] >= 0:
                    temp.append(1 + mat[i][m - S[i-1]])
                else:
                    temp.append(float('inf'))
                if i >= 1:
                    temp.append(mat[i-1][m])
                else:
                    temp.append(float('inf'))
                mat[i][m] = min(temp)    
    matmodi = mat[1:]           #Partie rajoutée
    while M != 0:               #Parcours de la matrice matmodi pour trouver le chemin minimale
        k = len(S) - 1
        while k > 0 and matmodi[k][M] == matmodi[k-1][M]:
            k -= 1
        T[k] += 1
        M -= S[k]
    return [mat, mat[i][m], T]

##Fonction pour calculer la complexité en espace/temps
#En entrée : La matrice mat fournie par la fonction Monnaie_dynamique_modifie
def Complexite(mat):
    matList = list((j for i in mat for j in i)) 
    return f"La complexité en espace/temps = {len(matList)}"
    