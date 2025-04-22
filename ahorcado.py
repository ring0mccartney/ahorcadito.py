import random

def jugar_ahorcado():
    palabras = ["manzana", "banana", "cereza", "datil", "uva", "kiwi", "limon", "mango", "naranja", "pera"]
    palabra_secreta = random.choice(palabras)
    letras_adivinadas = set()
    intentos_restantes = 6

    def mostrar_tablero():
        display = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                display += letra + " "
            else:
                display += "_ "
        print("\nPalabra: " + display)
        print("Letras adivinadas: " + ", ".join(sorted(list(letras_adivinadas))))
        print(f"Intentos restantes: {intentos_restantes}")

    while intentos_restantes > 0:
        mostrar_tablero()

        if all(letra in letras_adivinadas for letra in palabra_secreta):
            print("\n¡Felicidades! ¡Adivinaste la palabra:", palabra_secreta + "!")
            break

        intento = input("Ingresa una letra: ").lower()

        if len(intento) != 1 or not intento.isalpha():
            print("Por favor, ingresa una única letra válida.")
            continue

        if intento in letras_adivinadas:
            print("Ya intentaste esa letra. Intenta con otra.")
            continue

        letras_adivinadas.add(intento)

        if intento not in palabra_secreta:
            intentos_restantes -= 1
            print("Letra incorrecta.")

    else:
        mostrar_tablero()
        print("\n¡Perdiste! La palabra era:", palabra_secreta)

if __name__ == "__main__":
    jugar_ahorcado()
