def test_chain():
    # on cree une fonction qui demande à l'utilisateur de rentrer sa chaine de parenthese,
    s = input("Entrez une chaîne de parenthèses : ")
    #  creation une liste vide qui va permettre de stocker l'entrée
    parenthesis = []
    for char in s:
        if char == '(':
            parenthesis.append(char)
        elif char == ')':
            if not parenthesis:
                return False
                parenthesis.pop()
        else:
            return False
    return len(parenthesis) == 0


print(test_chain())


# on parcours avec une boucle for, pour chaque parenthese on ajoute dans la liste, puis on verifie si le retour de parenthèse est bien presents dans la lsite
# si non alors return false si oui alors true. on print le resultat de la fonction

# fonction trouvant la longeur max d'une sous-chaine bien formé
def find_wellformed_subchain():
    subchain = input("Entrez une chaîne de parenthèses : ")
    # Calcule la longueur de la chaîne entrer par l'utilisateur
    n = len(subchain)
    # Initialise une liste vide
    chaine = []
    # se place à la position -1 de la chaine pour le debut de la liste
    chaine.append(-1)

    # Initialise la variable pour stocker la longueur maximale trouvée
    result = 0

    # boucle for pour parcourir la chaîne de parenthèses
    for i in range(n):

        # on verifie dans la liste subchain si il y a bien une parenthèse ouvrante
        if subchain[i] == '(':
            chaine.append(i)

        # sinon la parenthèse est fermente alors :
        else:

            # on verifie si la chaine n'est pas vide, si oui on pop la parenthese ouvrante correspondante à la chaine
            if len(chaine) != 0:
                chaine.pop()

            # on verifie si la chaine n'est pas vide pour
            #  calculer la longueur de la sous-chaîne bien formée
            if len(chaine) != 0:
                result = max(result,
                             i - chaine[len(chaine) - 1])

            # Si la liste est vide, ajoute l'index actuel pour une autre sous-chaîne
            else:
                chaine.append(i)
    # on retourne et print le resultat de la longueur de la sous-chaine
    return result


print(find_wellformed_subchain())
# si on a une trop grande chaine avec beaucoup des parenthèses ouvrante,
# la taille maximum de notre liste peut etre atteinte avant d'avoir pu compter les parenthèses fermante
# comme on est avec une bocle for, la fonction parcourt chaque caractère de la chaine une fois.


# Question 3 :
# Un programme qui s’exécute de façon parallèle= une tâche q découpée en plusieurs morceaux
# pour être réalisée par plusieurs acteurs en même temps, la plupart du temps pour qu’elle se termine plus vite.
# un programme synchrone : programme qui attend qu'une tache soit fini pour en commencer une autre != asyncrone qui essaie
# d'éviter d'attendre un temps sans rien faire.
# Ainsi pour travailler de façon parallele et asynchrnone, nous pouvons distribuer les taches en divisant les sous-chaines et
# distribuer ces sous-chaines aux differentes machines afin qu'ils traitent séparément les sous-chaines de leurs côtés.
# Donc  chaque machine traite une ou plusieurs sous chaine selon sa capacité, les resultats sont collecté et combinées pour obtenir un resultat total
# La complexité en terme de temps et de mémoire : cela dependra du nombre machines disponible et de comment les taches sont distribuées + la taille de la sous-chaine pour chaque machine
# en terme de performance : comme on utilise plusieurs machines à la fois pour traiter une chaine, cela peut réduire le temps total pour traiter la totalité de la chaine,
# chaque machine sera plus performante avec une chaine plus petite et donc plus rapide.
#
