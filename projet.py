def moyenne (T):
    S=0
    for t in T:
        S++=t
        return S
Data=[1,3,5]
Moy=statistics.mean(Data)
print("La moyenne est :", Moy)
