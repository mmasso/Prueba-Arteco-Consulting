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
    return palabra == reversed(palabra)
