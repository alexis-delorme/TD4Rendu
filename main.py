import math

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
                print(Mprim)
                print(D[idx], idx)
                Mprim -= valeur
                D[idx] -= 1
                T[idx] += 1
    print(Mprim)
    QOptimal = sum(T)
    if tolerance == 100:
        return f"Insuffisament des billets/pièces... Montant rendu = {M-Mprim}, Tuple : {T}"
    return f"Tuple des pièces : {T}, Nombre des billets/pièces optimal : {QOptimal}"


def Monnaie_Gloutonne_Modifie2(S,M,D):
    Total=0
    Mprim = M
    T=[0]*len(S)
    for idx, valeur in reversed(list(enumerate(S))):
         if valeur <= Mprim and D[idx] != 0:
             print(valeur)
             break
    for ind, v in enumerate(S[:idx+1]):
        print(v, D[ind])
        Total += v*D[ind]
        print(Total)
    if Total < M:
        return f"Insuffisament des billets/pièces... Total = {Total}"
    while Mprim != 0:
        for idx, valeur in reversed(list(enumerate(S))):
            while valeur <= Mprim and D[idx] != 0:
                print(Mprim)
                print(D[idx], idx)
                Mprim -= valeur
                D[idx] -= 1
                T[idx] += 1
    print(Mprim)
    QOptimal = sum(T)
    return f"Tuple des pièces : {T}, Nombre des billets/pièces optimal : {QOptimal}"

S=[1,2,5,10,22] 
D=[3,0,0,1,0]
test2 = Monnaie_Gloutonne_Modifie2(S,15,D)
print(test2)


print(test2)

print(test2)

print(test2)