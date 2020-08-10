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


def contar_palabras_repetidas(lorem_ipsum):
    dicc_lorem = crear_dict_repetidas(lorem_ipsum)
    i = 0
    lista_mas_repetidas = list()
    while i < 5:
        lista_mas_repetidas.append(max(dicc_lorem, key=dicc_lorem.get))
        dicc_lorem.pop(max(dicc_lorem, key=dicc_lorem.get))
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