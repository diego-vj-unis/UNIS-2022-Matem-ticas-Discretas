#Evaluación 5
#Matemáticas Discretas.
#Universidad del Istmo
#Diego Vallejo. Carné 2020-1283

import math

entrada_a = int(input("Ingrese un número: \n"))
entrada_b = int(input("Ingrese otro número: \n"))
i = 1; 

lista1 = [entrada_b, entrada_a]
lista2 = [1,0]
lista3 = [0,1]
lista4 = [0,0]

while lista1[i] != 0: 
    lista4.append(math.floor(lista1[i-1] / lista1[i]))
    lista1.append(lista1[i-1] - lista4[i+1]*lista1[i])
    lista2.append(lista2[i-1] - lista4[i+1]*lista2[i])
    lista3.append(lista3[i-1] - lista4[i+1]*lista3[i])
    i = i + 1

vi_1 = lista3[i-1]

if vi_1 < 0:
   vi_1 = lista3[i-1] + lista1[0]
   
x = vi_1

print("El inverso es:", x)


