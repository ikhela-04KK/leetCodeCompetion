liste = ['a', 'b', 'c', 'd', 'e']
n = len(liste)
arr = [None]*(n*2)   # creer une liste de n valeur n. 

for i, x in enumerate(liste):
    arr[i] = x
    arr[i+n] = x

print(arr)