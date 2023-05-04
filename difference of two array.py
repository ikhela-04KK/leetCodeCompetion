#creer une liste de trois valeurs 

all_r = []
liste1 = [1, 2, 3]
liste2 = [2,4,6]

ens1 = set(liste1)
ens2 = set(liste2)

r1 = list(ens1-ens2)
r2 = list(ens2-ens1)

# ajouter r1 et r2 dans la liste

all_r.append(r1)
all_r.append(r2)

print(all_r)
