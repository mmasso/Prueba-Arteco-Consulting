from lorem_convert import text_to_string, quitar_puntuacion
from contar import contar_frase, contar_parrafos, contar_palabras, contar_palindromos, contar_palabras_repetidas, contar_tuplas_repetidas


def main():
    lorem_ipsum = text_to_string()
    lorem_sin_puntuacion = quitar_puntuacion(lorem_ipsum)
    n_parrafos = contar_parrafos(lorem_ipsum)
    n_frases = contar_frase(lorem_ipsum)
    n_palabras = contar_palabras(lorem_sin_puntuacion)
    n_palindromos = contar_palindromos(lorem_sin_puntuacion)
    n_palabras_repetidas = contar_palabras_repetidas(lorem_sin_puntuacion)
    n_tuplas_repetidas = contar_tuplas_repetidas(lorem_ipsum)
    return n_parrafos + "\n" +  n_frases + "\n" + n_palabras + "\n" + n_palindromos + "\n" + n_palabras_repetidas + "\n" + n_tuplas_repetidas


if __name__ == "__main__":
    print(main())

