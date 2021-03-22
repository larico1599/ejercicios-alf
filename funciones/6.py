#Escribir una función que reciba una muestra de números en una lista y devuelva
#  su media.

def media(lista):
    suma = 0
    for i in range(len(lista)):
        lista[i] = int(lista[i])
        suma = suma + lista[i] 
    return suma/len(lista)        

def verificar():
    lista = input("Ingrese los numero serados por espacios: ").split()
    while not len(lista)>= 1:
        lista = input("Ingrese los numero serados por espacios: ").split()
    count = 0    
    for i in range (len(lista)):
        if lista[i].isdigit():
            count +=1 
            if count == len(lista):
                return lista            
        else :
            lista = verificar()
            break
    return lista
                                
listaVerificada = verificar()
calculaMedia = media(listaVerificada)

print(f' La media de los numeros {listaVerificada} es : {calculaMedia:.{5}}')

