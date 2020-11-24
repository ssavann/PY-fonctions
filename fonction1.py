'''
Les fonctions en python qui n'envoie rien

print() input() type() float() str() etc... -> fonction native de python

def -> define

'''



def table2():
	for i in range(11):
		print(f"{i} * 2 = {i*2}")

table2()

print("---------------")

def table(x):
	for i in range(11):
		print(f"{i} * {x} = {i*x}")

table(5)	#ici on donne 5 à x. On peut remplacer 5 par n'importe quelle valeur

print("---------------")

def ditBonjour(nom, prenom, age):
	print(f"Bonjour je suis {nom} {prenom}, j'ai {age} ans")


ditBonjour("Tremblay", "Martin", 45)

print("---------------")

def ditSalut(nom="Roy", prenom="Patrick", age=25):
	print(f"Salut je suis {nom} {prenom}, j'ai {age} ans")


ditSalut("Bois", "Robin")

print("---------------")
ditSalut(age=55, nom="Bowi", prenom="David")


print("---------------")


def affiche(*mots):		#le "*mots" permet de passer plusieurs paramètres
	for m in mots:
		print(m)

affiche("voiture", "maison", "avion", "train")