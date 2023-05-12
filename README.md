# leetCodeCompetion

- Quand tu as des lacunes , il faut chercher à les ameliorés , j'ai quelques lacunes en algorithmes et du coup leetCode me permettra de m'ameliorer 


# COMMENT FONCTIONNNE LE HASHSET EN PYTHON : 

Un ensemble en Python est implémenté à l'aide d'une structure de données appelée une table de hachage (hash table). Une table de hachage est une structure de données qui associe des clés à des valeurs en utilisant une fonction de hachage. Dans le cas d'un ensemble, les éléments de l'ensemble sont utilisés comme clés dans la table de hachage, sans qu'il y ait de valeurs associées.

Voici comment un ensemble fonctionne en interne :

Lorsque vous ajoutez un élément à un ensemble à l'aide de la méthode add(), Python calcule d'abord le hachage de l'élément à l'aide de la fonction de hachage appropriée. Le hachage est un entier unique qui est utilisé pour identifier l'emplacement de stockage de l'élément dans la table de hachage.

Ensuite, Python utilise le résultat du hachage pour déterminer l'emplacement où l'élément sera stocké dans la table de hachage. Si cet emplacement est déjà occupé par un autre élément, il se produit ce qu'on appelle une collision de hachage.

Pour gérer les collisions, Python utilise généralement une technique appelée "adressage ouvert" (open addressing) ou "adressage fermé" (closed addressing). Lorsqu'une collision se produit, Python recherche un autre emplacement libre dans la table de hachage en utilisant une stratégie spécifique, telle que le "probing linéaire" ou le "probing quadratique".

Une fois qu'un emplacement libre est trouvé, l'élément est inséré dans la table de hachage à cet emplacement. Si l'élément est déjà présent dans l'ensemble (c'est-à-dire qu'il y a une collision de hachage avec un élément existant), il n'est pas ajouté à nouveau.

Lorsque vous vérifiez si un élément appartient à l'ensemble en utilisant l'opérateur in, Python calcule également le hachage de l'élément et recherche cet élément dans la table de hachage à l'emplacement correspondant. Si l'élément est trouvé, cela signifie qu'il appartient à l'ensemble.

Lorsque vous supprimez un élément de l'ensemble à l'aide de la méthode remove(), Python calcule le hachage de l'élément et le recherche dans la table de hachage. S'il est trouvé, il est supprimé de l'ensemble.

La structure de table de hachage utilisée pour implémenter les ensembles en Python garantit que les opérations de recherche, d'ajout et de suppression ont une complexité en temps en moyenne proche de O(1), ce qui en fait un choix efficace pour la gestion de collections d'éléments uniques