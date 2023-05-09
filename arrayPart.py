#array of partition : consiste à faire une pair unique avec les nombres d'une liste de d'additioner le minimum d'une pair a une autre et l'addition qui a la pair la plus grande remporte 

# oubien il faut determiner les nombres de la liste qui sont à la position 2n et les additionné

class Solution:
    def arrayPart(self,nums):
        return sum(sorted(nums)[::2]) # ici [::2] est slice qui permet de selectionner que les éléments qui sont à la 2k positions

n1 = Solution()
print(n1.arrayPart([6,2,6,5,1,2]))

