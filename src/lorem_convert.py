def text_to_string():
    file = open("src/lorem_ipsum.txt")
    lorem_string = file.read().replace("\n", " ")
    file.close()
    lorem_sin_comas = quitar_comas(lorem_string)
    return lorem_sin_comas


def quitar_comas(lorem_ipsum):
    lorem_sin_comas = lorem_ipsum.replace(",", "")
    return lorem_sin_comas
