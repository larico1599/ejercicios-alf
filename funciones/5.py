#Escribir una función que calcule el área de un círculo y otra que calcule el volumen de
#  un cilindro usando la primera funcion
import math
import sys 
def calculaAreaCirculo(radio):
    area = math.pi * radio**2    
    return area 

def calculaVolumenCilindro(area):
    longitud = float(input("Ingresela longitud del cilindro: "))
    volumen = longitud*area
    return volumen

def salir (radio):
    if radio.lower().startswith("s"):
        sys.exit()

print("Calculo de area y volumen ")
while True:
    radio = input("Ingrese el radio del circulo, o escriba (s) para salir : ")
    salir(radio)
        
    if radio.isdigit():
        radio = float(radio)
        area = calculaAreaCirculo(radio)
        print(f'El area es: {area:.{4}}')

        volumen = calculaVolumenCilindro(area) 
        print(f'El volumen es: {volumen:.{4}}')
    else :
        print("Introdusca un numero")
