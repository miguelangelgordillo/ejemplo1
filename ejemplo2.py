__author__ = 'miguel'

numeros=[1,23,67,67,8,8,5,9,5,3,0,12,12,23,45]
for elemento in numeros:
    posicion=numeros.index(elemento)
    if posicion !=len(numeros)-1:
        if elemento== numeros[posicion + 1]:
            numeros.remove(elemento)
print numeros