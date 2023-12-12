Luhn
====

# Instructions

La [formule de Luhn](https://fr.wikipedia.org/wiki/Formule_de_Luhn) est une opération de somme de contrôle utilisée dans différents domaines, notamment dans le milieu bancaire.

Le but de cet exercice est d'implémenter une fonction `is_valid` de validation de numéro de carte bancaire.

## Données

Les numéros de cartes bancaires acceptés ici doivent être composés de quatre groupes de quatre chiffres, séparés par des espaces. Tous les autres caractères sont interdits.

**Exemple :** `1234 5678 9012 3456`

## Algorithme

### 1. Suppression des espaces

Les espaces de séparation des groupes de chiffres doivent être supprimés.

**Exemple :** `1234567890123456`

### 2. Doubler un chiffre sur deux

Doubler la valeur de tous les chiffres dont la position est paire dans la chaîne de chiffres en commençant par la droite.

Si le doublement du chiffre donne un nombre supérieur à 9, il faut alors soustraire 9 du produit.

**Exemple :** On double les chiffres `1_3_5_7_9_1_3_5_`, ce qui donne `2_6_1_5_8_2_6_1_`, soit `2264165880226416` au final

### 3. La somme des chiffres doit être divisible par 10

Additionner l'ensemble des chiffres obtenus :
 - Si le résultat est divisible par 10, le numéro de carte bancaire est valide.
 - Sinon, il est invalide.

**Exemple :** `2 + 2 + 6 + 4 + 1 + 6 + 5 + 8 + 8 + 0 + 2 + 2 + 6 + 4 + 1 + 6 = 63`, le numéro de carte bancaire est donc invalide.

## Erreurs

En cas de numéros de cartes bancaires malformés ou autre événement inattendu, une erreur doit être remontée par la fonction `is_valid` :

### Exemples :

Présence de caractères non-numériques :
```
12E4 5678 9012 3456
```

Absence d'espace de séparation des groupes de chiffres :
```
1234567890123456
```


# Implémentation

La signature de la fonction `is_valid` est initiée dans le fichier [./luhn/lib.py](./luhn/lib.py).

Des tests d'intégration sont là pour valider l'implémentation de la librairie. Ils sont également là pour guider et faciliter la compréhension du problème.

Les indications `TODO` en commentaire attendent qu'on les remplace !

Libre à vous ensuite de compléter et d'organiser le code et les tests comme bon vous semble.

Enfin, n'hésitez pas à segmenter votre travail en différentes étapes, Git est là pour ça...

Quelques commandes utiles:

 - Exécuter les tests : `python -m unittest discover -v -s tests`
 - Vérifier le style : `python -m pylint luhn/ tests/`


### Bonne chance et soyez vous-même !
