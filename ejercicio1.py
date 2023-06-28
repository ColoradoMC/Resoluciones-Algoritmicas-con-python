# Función para contar el número de ocurrencias de cada letra en una frase
def contar_ocurrencias(frase):
    # Para que no haya diferencia de mayusculas o minusculas
    frase = frase.lower()

    # Diccionario
    ocurrencias = {}

    
    for caracter in frase:
        
        if caracter.isalpha():
            
            ocurrencias[caracter] = ocurrencias.get(caracter, 0) + 1

    return ocurrencias

def mostrar_ocurrencias(ocurrencias):
    for letra in "abcdefghijklmnopqrstuvwxyz":
        if letra in ocurrencias:
            print(f"La letra '{letra}' aparece {ocurrencias[letra]} veces.")
        else:
            print(f"La letra '{letra}' no aparece en la frase.")

def main():
    while True:
        print("\n--- MENU ---")
        print("1. Contar ocurrencias de letras en una frase")
        print("2. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            frase = input("Ingresa una frase: ")
            ocurrencias = contar_ocurrencias(frase)
            mostrar_ocurrencias(ocurrencias)
        elif opcion == "2":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elige una opción válida.")

main()