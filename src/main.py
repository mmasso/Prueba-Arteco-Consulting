from lorem_convert import text_to_string
from contar import contar_frase, contar_parrafos, contar_palabras, contar_palindromos


def main():
    lorem_ipsum = text_to_string()
    n_parrafos = contar_parrafos(lorem_ipsum)
    n_frases = contar_frase(lorem_ipsum)
    n_palabras = contar_palabras(lorem_ipsum)
    n_palindromos = contar_palindromos(lorem_ipsum)
    ### n_palabras_repetidas = contar_palabras_repetidas(lorem_ipsum)
    ### n_tuplas_repetidas = contar_tuplas_repetidas(lorem_ipsum)
    return n_parrafos, n_frases, n_palabras, n_palindromos


if __name__ == "__main__":
    print(main())
