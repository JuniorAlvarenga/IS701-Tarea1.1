import random

numero_a_adivinar = random.randint(1, 100)
intentos = int(0)
adivinado = False

print("Adivina el numero entre 1 y 100!")

while not adivinado:
    intento = int(input("Ingresa tu intento: "))
    intentos += 1
    
    if intento < numero_a_adivinar:
        print("El numero es mayor.")
    elif intento > numero_a_adivinar:
        print("El numero es menor.")
    else:
        adivinado = True
        print(f"¡Felicitaciones! Has adivinado el numero en {intentos} intentos.")
