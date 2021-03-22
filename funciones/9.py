#Escribir una función que calcule el máximo común divisor de dos números y otra que 
#calcule el mínimo común múltiplo.

def generaNumerosPrimos(numero):
    """Calcula los numeros primos anteriores a numero
        Un numero primo es disible por el mismo y por la unidad
    Args:
        numero (int): un numero 
    Returns:
        lista: lista de numeros primos
    """
    modulo =0
    primos =[]       
    for i in range(2,numero+1):
        contador = 0
        for j in range(1,i+1):
            modulo = i % j
            if modulo == 0:
                contador += 1
        if contador == 2: # si contador es 2 es un numero primo
            primos.append(i)         
    return primos

def desconponeNumero(numero,listaPrimos):
    """Descompone un numero es sus numeros primos

    Args:
        numero (int): un numero a descomponer
        listaPrimos (list): lista de numeros primos anterios o igual a numero

    Returns:
        primos [list]: numeros primos
        lisPotencia [list] : potencias de los numeros primos
        dic [dictionary]   : numeroPrimo : potencia
    """
    desconpone=[]    
    primos=[]
    lisPotencia=[]
    dic={}
    iterator = 0
    modulo  = 0
    primoAnterior = 1
    potencia = 1
    while numero > 1 and iterator < len(listaPrimos):
        modulo = numero % listaPrimos[iterator]
        if modulo  == 0:
            div = numero // listaPrimos[iterator]
            if listaPrimos[iterator] == primoAnterior :
                potencia += 1           
            else:
                primos.append(primoAnterior)
                lisPotencia.append(potencia)
                dic[primoAnterior]=potencia
                potencia = 1

            primoAnterior = listaPrimos[iterator]
            numero = div
            iterator = 0
            continue
        iterator += 1
    if numero ==1 :
            primos.append(primoAnterior)
            lisPotencia.append(potencia)
            dic[primoAnterior] = potencia    
    primos.remove(1)
    lisPotencia.remove(1)
    dic.pop(1)
    return primos, lisPotencia,dic


def calculaMCD(primo,potPrimos):
    resultados =[]
    for key in range(0, len(primo[1])):
        count =1
        for value in range(2,len(primo)+1):
            if primo[1][key] in  primo[value]:
                count +=1 
                if count == len(primo):
                    resultados.append(primo[1][key])
    mult = 1
    for i in resultados:       
        if i in potPrimos:
            recibe=potPrimos[i]
            mult = mult * (i**min(recibe))
            
    return  mult
def calculaMCM(potPrimos):
    mult =1
    for key ,value in potPrimos.items():
        maximo = max(value)
        mult = mult *( key**maximo)
    return mult

print(5*"-" + "MCD" + 5*"-")
numero = 0
numeros=[]
dicPrimos={}
dicPotenciasPrimos={}
ListaNumerosDesconpuestos = []
s = 's'
n=1
while  numero >= 0 and s =='s' : 
    numero = int(input("Ingrese un numero: "))
    numeros.append(numero)
    listaNumerosPrimos = generaNumerosPrimos(numero)
    listaPrimos,listaPotencia,dicPriKeyValue = desconponeNumero(numero,listaNumerosPrimos)
    dicPrimos[n] = listaPrimos #numeros descompuestos en primos, ordenados segun ingreso

    for key,value in dicPriKeyValue.items():
        dicPotenciasPrimos.setdefault(key,[]).append(value)

    s = input("Desea seguir agregando numeros,'n' para salir (s/n): ").lower()
    n+=1

mcd= calculaMCD(dicPrimos,dicPotenciasPrimos)
mcm= calculaMCM(dicPotenciasPrimos)

print(f' El MCD  de {numeros} es :{mcd}')
print(f' El MCM  de {numeros} es :{mcm}')
