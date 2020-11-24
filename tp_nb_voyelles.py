'''
TP2: Réaliser une fonction qui affiche le nombre de voyelles dans une chaine
de caractère, peu importe la casse (Majuscule Minuscule)



'''

voyelles = "aeiouyAEIOUY"

def nbVoy(chaine):
    compteur = 0
    for lettre in chaine:
        if lettre in voyelles : compteur += 1

    return compteur

print(nbVoy("Bonjour TOI !"))    #donc 5 voyelles dans cette phrase

print("---------------------")

print(nbVoy("Aujourd'hui il neige dehors!")) 