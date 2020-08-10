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