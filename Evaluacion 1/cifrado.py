#Evaluación 1. Cifrado * 5 módulo 27.
#Matemáticas Discretas.
#Universidad del Istmo
#Diego Vallejo. Carné 2020-1283

abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];
#valor_numero: 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25

#Hola =    7, 14, 11, 0
#Hola*5 = 35, 70, 55, 0
#mod27 =   8, 16, 1,  0
#cifrado = iqba

msg = input("Mensaje a cifrar: \n")
clave = int(input("Clave de cifrado: \n"))
msg_cifrado = ""

#funcion para aceptar mayusculas
def lowerChar(char): 
    return char.lower()

#lista utilizada para guardar los valores despues de hacer la operacion de cifrado
arr2 = []

#operacion
for i in msg:
    lowerCase = i.lower()
    arr2.append(((abecedario.index(lowerCase) * clave)%27))

#lista que tendrá los valores en letra
arr3= []

#traducción de números a letras en lista
for i in arr2: 
    arr3.append(abecedario[i])

#traduccion de lista a string
for i in arr3: 
    msg_cifrado += i

print (msg_cifrado.upper())



