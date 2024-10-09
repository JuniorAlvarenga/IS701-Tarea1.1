def contar_vocales(frase):
    vocales = "aeiouAEIOU"
    contador = 0

    for letra in frase:
        if letra in vocales:
            contador += 1

    return contador

frase = input("Ingrese una frase: ")
numero_vocales = contar_vocales(frase)
print(f"Número total de vocales: {numero_vocales}")
