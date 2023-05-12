#creation d'un design hash en faisant en sorte d'implementer le SET 
# on a pu faire ça car le dictionnaire ne prend

class myHashSet:
    def __init__(self): # on ajoute aucun paramètre car ces add qui se servira de cette fonctionnalité
        self.hash = {}  

    def add(self,key):
        self.hash[key] = None # None est facultatif c'est juste pour utiliser la propriété des dictionnaire 

        # elle est très efficae dans le sens où le dictionnaire ne contient pas de doublon de clé
    
    def contains(self,key):
        return key in self.hash # return True si la clé exise et False si la clé n'existe pas 

    def remove(self,key):
        if key in self.hash:
            del self.hash[key]
    
    def __str__(self):
        return str(list(self.hash.keys())) # affiche uniquement les clés qui representent les valeurs ajouter au hashset
        

aj1 = myHashSet()
aj1.add(1)
aj1.add(2)
aj1.add(1) # quand la valeur que l'on veut ajouter est similaire à un élémemt du dictionnaire il retourne rien 
print(aj1.remove(5))

print(aj1)