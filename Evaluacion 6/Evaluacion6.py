#Evaluación 6
#Matemáticas Discretas.
#Universidad del Istmo
#Diego Vallejo. Carné 2020-1283

entrada_a = int(input("Ingrese la base: \n"))
entrada_b = int(input("Ingrese el exponente: \n"))
entrada_n = int(input("Ingrese el modulo: \n"))

b_binary = bin(entrada_b)
b_clean = b_binary[2:len(b_binary)]


x = 1

for i in b_clean:
    if i == "1": 
        x = x**2*entrada_a % entrada_n
    
    else: 
        x = x**2 % entrada_n
        
    
print("El resultado es", x)
