#Escribir una función que reciba una muestra de números en una lista y devuelva otra 
#lista con sus cuadrados.

def cuadrados(lista):
    suma = 0
    cuadrado = 1
    listaCuadradros = []
    for i in range(len(lista)):
        lista[i] = int(lista[i])
        cuadrado = lista[i] * lista[i]
        listaCuadradros.append(cuadrado)
    return listaCuadradros 


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
calcuCuadrados = cuadrados(listaVerificada)

print(f'Numero ingresados {listaVerificada}sus cuadrados: {calcuCuadrados}')