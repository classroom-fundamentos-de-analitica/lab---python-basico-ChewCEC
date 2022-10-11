"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
#Leer csv
import csv 
from operator import itemgetter
from pickletools import read_uint1

with open("data.csv", "r") as file:
    datos = file.readlines()
  


datos = [line.replace("\n", "") for line in datos]
datos = [line.split("\t") for line in datos]


def pregunta_01():
    with open("data.csv", "r") as file:
        datos = file.readlines()
    
    print(datos[0:2])

    datos = [line.replace("\n", "") for line in datos]
    datos = [line.split("\t") for line in datos]

    cont = 0
    for fila in datos:
        cont += int(fila[1])
        
    return cont
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    with open("data.csv", "r") as file:
        datos = file.readlines()
    
    datos = [line.replace("\n", "") for line in datos]
    datos = [line.split("\t") for line in datos]
 

    arreglo =[]
    for line in datos:
        arreglo.append(line[0])
    
    dict = []
    for elemento in arreglo:
        temp = arreglo.count(elemento)
        if (elemento,temp) not in dict:
            dict.append((elemento, int(temp)))
        

    return sorted(dict, key=lambda tup: tup[0])
            


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    with open("data.csv", "r") as file:
        datos = file.readlines()
    
    datos = [line.replace("\n", "") for line in datos]
    datos = [line.split("\t") for line in datos]
    
    arreglo1 = []
    dict = {}
    for line in datos:
        if line[0] not in arreglo1:     
            arreglo1.append(line[0])
            dict[line[0]] = line[1]
        elif line[0] in arreglo1:
            temp = int(dict.get(line[0])) + int(line[1])
            dict[line[0]] = temp
            
    resp = []
    for key in dict:
        resp.append( (key, int(dict.get(key))) )
    return sorted(resp, key=lambda tup: tup[0])
    

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open("data.csv", "r") as file:
        datos = file.readlines()
    
    datos = [line.replace("\n", "") for line in datos]
    datos = [line.split("\t") for line in datos]

    arreglo = []
    for line in datos:
        u = line[2].split("-")
        arreglo.append(u[1])
    
    tmp = set(arreglo.copy())
    
    resp = []
    for item in tmp:
        r = arreglo.count(item)
        resp.append((item, int(r)))
    
    return sorted(resp, key=lambda x: x[0])


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open("data.csv", "r") as file:
        datos = file.readlines()
    
    datos = [line.replace("\n", "") for line in datos]
    datos = [line.split("\t") for line in datos]

    column1 = sorted(set([line[0] for line in datos]))
    
    dictMenor = {}
    dictMayor = {}
    # (LETRA, NUMERO DE LAS LETRAS )

    for line in datos:
        letra = line[0]
        numero = int(line[1])
        if letra not in dictMenor:
            dictMenor[letra] = [numero]
            dictMayor[letra] = [numero]
        elif letra in dictMenor:
            if numero > dictMayor.get(letra):
                dictMayor[letra] = [numero]
            elif numero < dictMenor.get(letra):
                dictMenor[letra] = [numero]

    resp = []
    for letra in column1:
        resp.append( (letra, int(dictMayor.get(letra)), int(dictMenor.get(letra))) )
    
    return resp



def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado más pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]
    """
    with open("data.csv", "r") as file:
        datos = file.readlines()
    
    datos = [line.replace("\n", "") for line in datos]
    datos = [line.split("\t") for line in datos]

    lista = []
    set_a = []
    for line in datos:
        u = line[4].split(",")
        for dat in u:
            lista.append(dat)
            set_a.append(dat.split(":")[0])
    conj = sorted(set(set_a), key=lambda x: x)

    ans = []
    for elemento in conj:
        lista_temp = []
        for dato in lista:
            d = dato.split(":")
            if elemento == d[0]:
                lista_temp.append(int(d[1]))
        ans.append((elemento, min(lista_temp), max(lista_temp)))
    
    return ans

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    with open("data.csv", "r") as file:
        datos = file.readlines()
    
    datos = [line.replace("\n", "") for line in datos]
    datos = [line.split("\t") for line in datos]
    
    ans = []
    for i in range(10):
        lista_temp = []
        for linea in datos:
            if i == int(linea[1]):
                lista_temp.append(linea[0])
        ans.append((i,lista_temp))
    
    return ans



def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    with open("data.csv", "r") as file:
        datos = file.readlines()
    
    datos = [line.replace("\n", "") for line in datos]
    datos = [line.split("\t") for line in datos]
    
    ans = []
    for i in range(10):
        lista_temp = []
        for linea in datos:
            if i == int(linea[1]):
                lista_temp.append(linea[0])

        lista = set(lista_temp)
        ans.append((i, sorted(lista, key = lambda x : x) ))
    
    return ans
    


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    with open("data.csv", "r") as file:
        datos = file.readlines()
    
    datos = [line.replace("\n", "") for line in datos]
    datos = [line.split("\t") for line in datos]

    lista = []
    for line in datos:
        u = line[4].split(",")
        for elemento in u:
            lista.append(elemento.split(":")[0])

    lista_set = sorted(set(lista.copy()), key=lambda x: x)
    
    ans = {}
    for elemento in lista_set:
        ans[elemento] = lista.count(elemento) 

    return ans

        
    
def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]

    """
    with open("data.csv", "r") as file:
        datos = file.readlines()
    
    datos = [line.replace("\n", "") for line in datos]
    datos = [line.split("\t") for line in datos]

    ans = []
    for line in datos:
        ans.append( ( line[0], len(line[3].split(",")), len(line[4].split(","))  ))

    return ans

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }

    """
    with open("data.csv", "r") as file:
        datos = file.readlines()
    
    datos = [line.replace("\n", "") for line in datos]
    datos = [line.split("\t") for line in datos]
    
    letras = ["a", "b", "c", "d", "e", "f", "g"]
    ans = {}
    for elemento in letras:
        cont = 0 
        for line in datos:
            if elemento in line[3]:
                cont += int(line[1])
        ans[elemento] = cont
    return ans


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    with open("data.csv", "r") as file:
        datos = file.readlines()
    
    datos = [line.replace("\n", "") for line in datos]
    datos = [line.split("\t") for line in datos]

    letras = sorted (set([ line[0] for line in datos]), key=lambda x: x)

    ans = dict.fromkeys(letras, 0)
    for line in datos:
        if line[0] in letras:
            cont = 0
            u = line[4].split(",")
            for urg in u:
                cont += int(urg[4:])
        ans[line[0]] = cont + ans.get(line[0])
    
    return ans


