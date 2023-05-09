# creer une liste de trois listes contenant 3 nombres entiers 

#permet de trouver l'intersection de trois liste afin de pouvoir determiner les éléments communm au deux liste
def solution(listes):
    nums_1 = set(listes[0])
    for i in range(len(listes)-1):
        nums_1 =nums_1.intersection(set(listes[i]),set(listes[i+1])) # methode avec les sets qui permet l'intersection d'une liste avec deux autres

    return sorted(list(nums_1)) #creation de la liste trié contenant l'intersection des listes
listes = [[7,34,45,10,12,27,13],[27,21,45,10,12,13]] 
print(solution(listes))
