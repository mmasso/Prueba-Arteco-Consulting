def text_to_string():
    file = open("src/lorem_ipsum.txt")
    lorem_string = file.read().replace("\n", " ")
    file.close()
    return lorem_string


def quitar_comas(lorem_ipsum):
    lorem_sin_comas = lorem_ipsum.replace(",", "")
    return lorem_sin_comas


def quitar_puntos(lorem_ipsum):
    lorem_sin_punto = lorem_ipsum.replace(".", "")
    return lorem_sin_punto


def quitar_signos_parrafo(lorem_ipsum):
    lorem_sin_parrafo = lorem_ipsum.replace("/", "")
    return lorem_sin_parrafo


def quitar_puntuacion(lorem_ipsum):
    lorem_sin_comas = quitar_comas(lorem_ipsum)
    lorem_sin_puntos_comas = quitar_puntos(lorem_sin_comas)
    lorem_sin_puntuacion = quitar_signos_parrafo(lorem_sin_puntos_comas)
    return lorem_sin_puntuacion
