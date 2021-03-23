#Escribir una función que convierta un número decimal en binario y otra que convierta
#  un número binario en decimal.

#Numeros Binarios
def menorQueNumero(numero):
    numeroMenor =0
    binarios =[128,64,32,16,8,4,2,1]
    for i in binarios:
        if numero > i:
            numeroMenor = i 
            break
        elif numero == i :
            numeroMenor = i
            break
    return numeroMenor
def binarios(numero):#15
    listabinarios=[]
    binarios =[128,64,32,16,8,4,2,1]
    numeroLimite =numero
    while not (sum(listabinarios) == numeroLimite) :
        numeroMenor = menorQueNumero(numero)
        listabinarios.append(numeroMenor)
        resta = numero - numeroMenor         
        numero = resta     
    binarios2=[0,0,0,0,0,0,0,0]
  
    for i in  listabinarios:  
        indice = binarios.index(i) 
        binarios2[indice] = 1
    print(binarios2)

numero = int(input("Ingrese un numero: "))
binarios(numero)
