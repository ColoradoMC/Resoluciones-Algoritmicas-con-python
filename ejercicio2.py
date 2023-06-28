while True:
    numero = input("Ingrese un número entero (o '*' para salir): ")
    if numero == '*':
        break
    numero = int(numero)
    if numero < 0:
        print("El número es negativo")
    elif numero > 0:
        print("El número es positivo")
    else:
        print("El número es igual a cero")
