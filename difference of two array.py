#creer une liste de trois valeurs 

#permet de determiner la difference de valeurs entre deux listes 
liste1 = [1, 2, 3]
liste2 = [2,4,6]

ens1 = set(liste1)
ens2 = set(liste2)

r1 = list(ens1-ens2)
r2 = list(ens2-ens1)

all_r = [r1, r2]
print(all_r)
