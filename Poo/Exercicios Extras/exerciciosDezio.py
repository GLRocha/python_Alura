# Dada uma lista de números, encontre o valor mínimo e máximo.

lista = [10,6,5,87,8,9,5,4,6,656,8,445,321,78]
lista = [2]

#Versao 1
min = 0
max = 0
for i in lista:
    if i >= max:
        max = i

min = max
for i in lista:
    if i < min:
        min = i



#Versao 2
min = 0
max = 0
count = 0
for i in lista:
    if i >= max:
        max = i

    if count == 0:
        min = i
    else:
        if i < min:
            min = i
    count += 1


#versao 3
min = lista[0]
max = 0
count = 0
for i in lista:
    if i >= max:
        max = i

    if i < min:
        min = i

print(max)
print(min)