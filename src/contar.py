from collections import Counter, defaultdict


def contar_parrafos(texto):
    n_parrafos = len(texto.split(".  "))
    return "El número de parrafos es de: " + str(n_parrafos)


def contar_frase(texto):
    n_frases = len(texto.split(". "))
    return "El número de frases es de: " + str(n_frases)


def contar_palabras(texto):
    n_palabras = len(texto.split())
    return "El número de palabras es de: " + str(n_palabras)


def contar_palindromos(texto):
    lista_lorem = texto.split()
    contador_palindromos = 0
    lista_palindromos = list()
    for palabra in lista_lorem:
        if _es_palindromo(palabra) and len(palabra) > 1:
            contador_palindromos += 1
            lista_palindromos.append(palabra)
    return "El número de palíndromos es de: " + str(contador_palindromos) + " siendo ellos: " + str(lista_palindromos)


def _es_palindromo(palabra):
    return palabra.lower() == palabra.lower()[::-1]


def representar_lista_valores(dicc_lorem, lista_keys_repetidas):
    string_final = "Las palabras más repetidas són:"
    for key in lista_keys_repetidas:
        string_final +=  "\n" + "'" + key + "' con " + \
            str(dicc_lorem.get(key)) + " repeticiones"
    return string_final


def lista_llaves_mas_repetidas(dicc_lorem):
    i = 0
    lista_mas_repetidas = list()
    dicc_lorem_copy = dicc_lorem.copy()
    while i < 5:
        lista_mas_repetidas.append(
            max(dicc_lorem_copy, key=dicc_lorem_copy.get))
        dicc_lorem_copy.pop(max(dicc_lorem_copy, key=dicc_lorem_copy.get))
        i += 1
    return lista_mas_repetidas


def crear_dict_repetidas(texto):
    lista_palabras = tratar_lista(texto)
    dicc_lorem = dict()
    for palabra in lista_palabras:
        if palabra in dicc_lorem:
            dicc_lorem[palabra] += 1
        else:
            dicc_lorem[palabra] = 1
    return dicc_lorem


def contar_palabras_repetidas(texto):
    dicc_lorem = crear_dict_repetidas(texto)
    lista_keys_repetidas = lista_llaves_mas_repetidas(dicc_lorem)
    string_lista_valores = representar_lista_valores(
        dicc_lorem, lista_keys_repetidas)
    return string_lista_valores

###CONTAR_TUPLAS_DE_DOS_A_MAS_PALABRAS


def count_secuencias(lista_palabras, n):

    count_dict = defaultdict(int)
    for i in range(len(lista_palabras)-n+1):
        key = tuple(lista_palabras[i:i+n])
        count_dict[key] += 1
    return count_dict


def contar_mas_repetidas(lista_palabras, texto):
    dict_total = dict()
    contador = int(len(texto.split()) / len(texto.split(". "))) + 1
    while contador >= 2:
        n = contador
        count_dict = count_secuencias(lista_palabras, n)
        dict_total.update(count_dict)
        contador -= 1
    return Counter(dict_total).most_common(5)


def tratar_lista(texto):
    lista_lorem = texto.split()
    tratada_lista_lorem = list()
    for palabra in lista_lorem:
        palabra = palabra.strip()
        palabra = palabra.strip(".")
        palabra = palabra.strip(",")
        palabra = palabra.lower()
        tratada_lista_lorem.append(palabra)
    return tratada_lista_lorem


def representar_lista_tuplas(list_total):
    string_final = "Las tuplas más repetidas són:"
    for element in list_total:
        string_final += "\n" + \
            str(element[0]) + "' con " + str(element[1]) + " repeticiones"
    return string_final


def contar_tuplas_repetidas(texto):
    lista_palabras = tratar_lista(texto)
    list_mas_repetidas = contar_mas_repetidas(lista_palabras, texto)
    string_lista_tuplas = representar_lista_tuplas(list_mas_repetidas)
    return string_lista_tuplas
