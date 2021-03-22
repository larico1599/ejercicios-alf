#Escribir una función que reciba una muestra de números en una lista y devuelva un 
# diccionario con su media, varianza y desviación típica.

def Media(lista):
    suma = 0
    for i in range(len(lista)):        
        suma = suma + int(lista[i]) 
        media = suma/len(lista)  
    return media        
def VarianzaYDesviacion (calculaMedia,lista):
    var = 0
    desv = 0
    for i in range(len(lista)):
        var = var + (int(lista[i]) - calculaMedia)**2        
    var = var / len(lista)    
    desv = var **(1/2) 
    return var,desv
    
def Verificar():
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
            lista = Verificar()
            break
    return lista

dic={}
while True :                           
    listaVerificada = Verificar()
    calculaMedia = Media(listaVerificada)
    varianza,desviacion = VarianzaYDesviacion(calculaMedia,listaVerificada)

    
    StrListaVerificada = " ".join(listaVerificada) # convierte a strin una lista 
    dic[StrListaVerificada] = [round(varianza,2),round(desviacion,2)]

    print (dic)

    #print(f'La media de los numeros {listaVerificada} es : {calculaMedia:.{5}}')
    #print(f'La varianza es: {varianza:.{5}} y la desviacion es: {desviacion:.{5}}')


