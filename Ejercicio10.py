import random

def generar_contrasena(longitud):
    if longitud < 8:
        print("La longitud minima de la contraseña debe ser de 8 caracteres.")
        return None

    contrasenia = []
    
    for _ in range(longitud):
        #caracteres imprimibles en ASCII 33 - 126
        codigo_ascii = random.randint(33, 126)
        contrasenia.append(chr(codigo_ascii)) 
    return ''.join(contrasenia)

longitud = int(input("Ingrese la longitud de la contraseña (minimo 8 caracteres): "))
contrasenia_generada = generar_contrasena(longitud)

if contrasenia_generada:
    print(f"Contraseña generada: {contrasenia_generada}")
