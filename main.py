import math
from graphviz import Digraph

graph = Digraph(comment='Arbre',format='png')
graph.attr(size='50,50!')

S=[1,2,5,10,20,50,100,200,500,1000,2000,5000,10000]     ##Tuple, valeur de pièces
T=[]                                                    ##Tuple, pièces à rendre
M=0                                                     ##Integer, montant à rendre
D=[3,4,3,5,3,2,5,6,7,11,2,12,1]                         ##Tuple, disponibilité de chaque valeur 
Q=0
QOptimal=0

def Monnaie_Gloutonne(S,M):
    Mprim = M
    T=[0]*len(S)
    while Mprim != 0:
        for idx, valeur in reversed(list(enumerate(S))):
            if valeur <= Mprim:
                T[idx] = Mprim // valeur
                Mprim = Mprim % valeur
    QOptimal = sum(T)
    return f"Tuple des pièces : {T}, Nombre des billets/pièces optimal : {QOptimal}"


test=Monnaie_Gloutonne(S,23665)
#print(test)


def Monnaie_Gloutonne_Modifie1(S,M,D):       ##Avec Tolérance pour itérations de while
    Mprim = M
    T=[0]*len(S)
    tolerance = 0
    while Mprim != 0 and tolerance < 100:
        tolerance += 1
        for idx, valeur in reversed(list(enumerate(S))):
            while valeur <= Mprim and D[idx] != 0:
                Mprim -= valeur
                D[idx] -= 1
                T[idx] += 1
    QOptimal = sum(T)
    if tolerance == 100:
        return f"Insuffisament des billets/pièces... Montant rendu = {M-Mprim}, Tuple : {T}"
    return f"Tuple des pièces : {T}, Nombre des billets/pièces optimal : {QOptimal}"

S=[1,2,5,10,22] 
D=[3,0,0,1,0]
test2 = Monnaie_Gloutonne_Modifie1(S,12,D)
#print(test2)

def Monnaie_Gloutonne_Modifie2(S,M,D):
    tolerance = 0
    Mprim = M
    T=[0]*len(S)
    Total = 0
    for idx, valeur in reversed(list(enumerate(S))):
        if Mprim <=valeur:
            break
    for ind,v in enumerate(S[:idx-1]):
        Total += v*D[ind]
    if Total < M:
        return f"Insuffisament des billets/pièces... Montant total = {Total}"

    while Mprim != 0 and tolerance < 100:
        tolerance += 1
        for idx, valeur in reversed(list(enumerate(S))):
                dispo = D[idx]
                nbBillets = Mprim // valeur
                if nbBillets <= dispo:
                    Mprim = Mprim % valeur
                    T[idx] = nbBillets
                    D[idx] = dispo - nbBillets
                else:
                    T[idx] = dispo
                    Mprim = Mprim - valeur*dispo
                    D[idx] = 0
    QOptimal = sum(T)
    if tolerance == 100:
        return f"Rendu impossible, aucune combinaison des billets trouvé"
    return f"Tuple des pièces : {T}, Nombre des billets/pièces optimal : {QOptimal}, Disponibilité de pièces : {D}"

S=[1,2,5,10,20] 
D=[0,2,1,0,0]
test3 = Monnaie_Gloutonne_Modifie2(S,6,D)
#print(test3)



## Chemin minimal dans un arbre

def Monnaie_Graphe(S,M):
    FileF = []
    FileF.append(M)
    Noeuds = [M]
    ArbreA = [[M,[]]]
    while FileF != []:
        Parent = FileF[0]
        for valeur in S:
            noeud = Parent - valeur
            if valeur < Parent:
                if noeud not in Noeuds:
                    Noeuds.append(noeud)
                    ArbreA.append([noeud, [Parent]])
                    FileF.append(noeud)
                else:
                    index = [y[0] for y in ArbreA].index(noeud)
                    ArbreA[index][1].append(Parent)
            if noeud == 0:
                ArbreA.append([0,[Parent]])
                return ArbreA, Noeuds
        FileF.pop(0)
    return (ArbreA, Noeuds)
    #return T, QOptimal

S=[1,7,14,23]
M=28
Test4 = Monnaie_Graphe(S,M)

def Q_Optimal(arbre_noeuds, S, M):
    arbre = arbre_noeuds[0]
    temp=0
    T = [0]*len(S)
    while M != 0:
        temp1 = temp
        index = [y[0] for y in arbre].index(temp)
        if index == 0:
            return T
        temp = arbre[index][1][0]
        M -= temp
        valeur = S.index(temp - temp1)
        T[valeur] += 1
    return T

print(Q_Optimal(Test4,S,M))

def Graph_Arbre(arbre_noeuds):
    arbre = arbre_noeuds[0]
    for liens in arbre:
        Parents = liens[1]
        noeud = str(liens[0])
        for parent in Parents:
            graph.edge(str(parent), noeud, label=str(parent - int(noeud)))
    print(graph.source)
    #graph.render('Arbre.gv', view=True)

#Graph_Arbre(Test4)
