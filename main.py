import math
from graphviz import Digraph

graph = Digraph(comment='Arbre',format='png')
graph.attr(size='50,50!')

def Monnaie_Gloutonne(S,M):
    Mprim = M
    T=[0]*len(S)
    while Mprim != 0:
        for idx, valeur in reversed(list(enumerate(S))):
            if valeur <= Mprim:
                T[idx] = Mprim // valeur
                Mprim = Mprim % valeur
    QOptimal = sum(T)
    return f"Montant à rendre : {M}, Liste des pièces utilisées : {T}, Nombre des billets/pièces optimal : {QOptimal}"

def Monnaie_Gloutonne_Modifie(S,M,D):
    Mprim = M
    T=[0]*len(S)
    Total = 0
    for idx, valeur in list(enumerate(S)):
        Total += valeur*D[idx]
    if Total < M:
        return f"Insuffisament des billets/pièces... Montant total = {Total}"
    while Mprim != 0 and D[0] > 0:
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
    if M != 0 and D[0] == 0:
        return f"Rendu impossible, aucune combinaison des billets trouvé pour ce montant"
    return f"Liste des pièces : {T}, Nombre des billets/pièces optimal : {QOptimal}, Disponibilité de pièces : {D}"


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

def Q_Optimal(arbre_noeuds, S, M):
    arbre = arbre_noeuds[0]
    temp=0
    T = [0]*len(S)
    while M != 0:
        temp1 = temp
        index = [y[0] for y in arbre].index(temp)
        if index == 0:
            return f"Liste des pièces utilisées optimale : {T}"
        temp = arbre[index][1][0]
        M -= temp
        valeur = S.index(temp - temp1)
        T[valeur] += 1
    return f"Liste des pièces utilisées optimale : {T}"

def Graph_Arbre(arbre_noeuds):
    arbre = arbre_noeuds[0]
    for liens in arbre:
        Parents = liens[1]
        noeud = str(liens[0])
        for parent in Parents:
            graph.edge(str(parent), noeud, label=str(parent - int(noeud)))
    print(graph.source)
    graph.render('Arbre.gv', view=True)


## Algorithme de Programmation Dynamique
def Monnaie_dynamique(S,M):
    Szero=S
    Szero.insert(0,0)
    w, h = M+1, len(Szero);
    mat = [[0 for x in range(w)] for y in range(h)] 
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
                if i >= 1:
                    temp.append(mat[i-1][m])
                mat[i][m] = min(temp)
    return mat[i][m]

def Monnaie_dynamique_modifie(S,M):
    T = [0]*len(S)
    w, h = M+1, len(S)+1;
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
    matmodi = mat[1:]
    while M != 0:
        k = len(S) - 1
        while k > 0 and matmodi[k][M] == matmodi[k-1][M]:
            k -= 1
        T[k] += 1
        M -= S[k]
    return [mat, mat[i][m], T]

def Complexite(mat):
    matList = list((j for i in mat for j in i)) 
    return f"La complexité en espace/temps = {len(matList)}"
    