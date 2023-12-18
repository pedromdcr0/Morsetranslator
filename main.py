import json


texto_input = input("Qual texto você quer em código morse?\n")


def traduzir(texto):
    texto_separado = []
    texto_traduzido = []

    with open("language.json", "r") as morse_file:
        morse_data = json.load(morse_file)

    for letra in texto:
        texto_separado.append(letra)

    for traducao in morse_data:
        for letra in texto_separado:
            if traducao["letra"] == letra.lower():
                texto_traduzido.append(traducao["traducao"])
    texto_revertido = texto_traduzido[::-1]

    resultado = ' '.join(texto_revertido)
    print(resultado)


traduzir(texto_input)
