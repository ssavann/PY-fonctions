'''
Fonction Lambda

syntaxe --> lambda <arg1>, <arg1>,... : instruction

'''
'''
def carre(x):
    return x * x

#au lieu de définir une fonction normale, on procède au lambda
'''


#faut le mettre dans une variable
carre = lambda x : x * x    

print(carre(4))

print("----------------")

addition =  lambda nb1, nb2 : nb1 + nb2

print(addition(10,11))


