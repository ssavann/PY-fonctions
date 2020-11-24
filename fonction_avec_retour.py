'''
Les fonctions avec retour
-------------------------
2 types de fonctions :
	print()-->ne retourne rien (procédure)
	input()-->retourne une valeur que l'on peu stocker dans une variable

mot clé : def (define)---> def <nomFonction>:
return : renvoyer des valeurs et sortir de la fonction

'''

def addition(nb1, nb2):		#je peux mettre autant d'argument nb1, nb2
	return nb1 + nb2
	

print(addition(10,2))


print("-------------------------")

def additionSoustraction(nb3, nb4):
	return(nb3 + nb4, nb3 -  nb4)


print(additionSoustraction(13, 7))


print("-------------------------")

(add , sous) = additionSoustraction(15,10)

print(f"addition:{add}   soustraction:{sous}")

print("-------------------------")


#si une des valeurs est vrai, ça sort de la fonction
def pgq10(nb):
	if nb > 10: return "c'est vrai"
	elif nb < 10: return "c'est faux"
	else: return "égal à 10"


print(pgq10(11))