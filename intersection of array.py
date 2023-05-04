# creer une liste de trois listes contenant 3 nombres entiers 

def solution(listes):
    nums_1 = set(listes[0])
    for i in range(len(listes)-1):
        nums_1 =nums_1.intersection(set(listes[i]),set(listes[i+1]))
    return sorted(list(nums_1))
listes = [[7,34,45,10,12,27,13],[27,21,45,10,12,13]] 
print(solution(listes))
