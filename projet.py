def moyenne (T):
    S=0
    for t in T:
        S++=t
        return S
Data=[1,3,5]
Moy=statistics.mean(Data)
print("La moyenne est :", Moy)
if Data :
    print("La moyenne est :", Moy(Data))
    print("Le min est :", Min(Data))
    print("Le max est :", Max(Data))
else:
    print("Dossier vide")
