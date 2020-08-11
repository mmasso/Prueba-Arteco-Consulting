def contar_parrafos(lorem_ipsum):
    return len(lorem_ipsum.split(".  "))


def contar_frase(lorem_ipsum):
    return len(lorem_ipsum.split(". "))


def contar_palabras(lorem_ipsum):
    return len(lorem_ipsum.split())


def contar_palindromos(lorem_ipsum):
    lista_lorem = lorem_ipsum.split()
    contador_palindromos = 0
    for palabra in lista_lorem:
        if es_palindromo(palabra) and len(palabra) > 1:
            contador_palindromos += 1
    return contador_palindromos


def es_palindromo(palabra):
    return palabra.lower() == palabra.lower()[::-1]

    

def representar_lista_valores(dicc_lorem, lista_keys_repetidas):
    string_final = "Las palabras más repetidas són:"
    for key in lista_keys_repetidas:
        string_final += " '" + key + "' con " + str(dicc_lorem.get(key)) + " repeticiones"
    return string_final


def lista_llaves_mas_repetidas(dicc_lorem):
    i = 0
    lista_mas_repetidas = list()
    dicc_lorem_copy = dicc_lorem.copy()
    while i < 5:
        lista_mas_repetidas.append(max(dicc_lorem_copy, key=dicc_lorem_copy.get))
        dicc_lorem_copy.pop(max(dicc_lorem_copy, key=dicc_lorem_copy.get))
        i += 1
    return lista_mas_repetidas


def crear_dict_repetidas(lorem_ipsum):
    lista_palabras = lorem_ipsum.split()
    dicc_lorem = dict()
    for palabra in lista_palabras:
        palabra = palabra.lower()
        palabra = palabra.strip()
        palabra = palabra.strip(".")
        palabra = palabra.strip(",")
        if palabra in dicc_lorem:
            dicc_lorem[palabra] += 1
        else:
            dicc_lorem[palabra] = 1
    return dicc_lorem


def contar_palabras_repetidas(lorem_ipsum):
    dicc_lorem = crear_dict_repetidas(lorem_ipsum)
    lista_keys_repetidas = lista_llaves_mas_repetidas(dicc_lorem)
    string_lista_valores = representar_lista_valores(dicc_lorem, lista_keys_repetidas)
    return string_lista_valores


def filtrar_palabras(dicc_lorem):
    lista_keys_repetidas_mismas_veces = list()
    for key in dicc_lorem.keys():
        if dicc_lorem[key] >= 2:
            lista_keys_repetidas_mismas_veces.append(key)
    return lista_keys_repetidas_mismas_veces

from collections import Counter
def comparar_repetidas_lorem(lista_palabras_repetidas, lista_lorem, dicc_lorem):
    lista_tuplas_repetidas = list()
    dict_lorem = dicc_lorem.copy()
    for palabra in lista_palabras_repetidas:
        contador = 1
        tupla = palabra
        while dict_lorem[palabra] > 0:
            posicion = lista_lorem.index(palabra)
            anterior = lista_lorem[posicion - contador]    
            posterior = lista_lorem[posicion + contador]
            if posicion - contador < 0:
                anterior = ""
            if posicion + contador > len(lista_lorem):
                posterior = ""

            if (posterior and anterior) in lista_palabras_repetidas and (dict_lorem[posterior] and dict_lorem[anterior]) > 0:
                tupla = anterior + " " +  tupla +  " "  + posterior
                dict_lorem[posterior] -= 1
                dict_lorem[anterior] -= 1
                lista_palabras_repetidas.pop(anterior)
            else:
                if anterior in lista_palabras_repetidas and dict_lorem[anterior] > 0:
                    tupla = anterior + " " + tupla
                    dict_lorem[anterior] -= 1
                if posterior in lista_palabras_repetidas and dict_lorem[posterior] > 0:
                    tupla = tupla + " " + posterior
                    dict_lorem[posterior] -= 1
                else:
                    break  
            contador += 1
            if len(tupla) > 1:
                lista_tuplas_repetidas.append(tupla)
    return Counter(lista_tuplas_repetidas).most_common(5)



def tratar_lista(lorem_ipsum):
    lista_lorem = lorem_ipsum.split()
    tratada_lista_lorem = list()
    for palabra in lista_lorem:
        palabra = palabra.strip()
        palabra = palabra.strip(".")
        palabra = palabra.strip(",")
        palabra = palabra.lower()
        tratada_lista_lorem.append(palabra)
    return tratada_lista_lorem


def contar_tuplas_repetidas(lorem_ipsum):
    dicc_lorem = crear_dict_repetidas(lorem_ipsum)
    lista_palabras_repetidas = filtrar_palabras(dicc_lorem)
    lista_lorem = tratar_lista(lorem_ipsum)
    lista_tuplas_repetidas = comparar_repetidas_lorem(lista_palabras_repetidas, lista_lorem, dicc_lorem)
    return lista_tuplas_repetidas
