__author__ = 'miguel'

palabras=["abc","xd","crm","zl","xb"]
listax=[]
listas=[]

for letra in palabras:
    if letra[0] =="x":
        listax.append(letra)
    else:
        listas.append(letra)
lista_final= sorted(listax) + sorted(listas)
print lista_final