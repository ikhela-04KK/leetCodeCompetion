from memory_profiler import profile
import sys 

@profile
def ma_fonction():
    # Votre implémentation de la fonction
    num = [1, 2, 3, 4, 5]
    num.__contains__(1)

if __name__ == "__main__":
    ma_fonction()

# Mesure de la consommation de mémoire totale de la fonction
taille_totale = sys.getsizeof(ma_fonction) + sys.getsizeof([1, 2, 3, 4, 5])
print("La fonction utilise une taille totale de {} octets de mémoire.".format(taille_totale/1048576))
