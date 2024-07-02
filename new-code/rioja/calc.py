import math

def obtener_numeros(cantidad):
    numeros = []
    for i in range(cantidad):
        while True:
            try:
                num = float(input(f"Ingrese el número {i+1}: "))
                numeros.append(num)
                break
            except ValueError:
                print("Error: Debes ingresar un número válido.")
    return numeros

def suma(numeros):
    return sum(numeros)

def resta(numeros):
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado -= num
    return resultado

def multiplicacion(numeros):
    resultado = 1
    for num in numeros:
        resultado *= num
    return resultado

def division(numeros):
    resultado = numeros[0]
    try:
        for num in numeros[1:]:
            resultado /= num
        return resultado
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero."

def potenciacion(base, exponente):
    return base ** exponente

def raiz_cuadrada(numero):
    return math.sqrt(numero)

def mostrar_menu():
    print("\nSelecciona la operación que deseas realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potenciación")
    print("6. Raíz cuadrada")
    print("7. Salir")

def ejecutar_operacion(opcion):
    if opcion in ["1", "2", "3", "4"]:
        cantidad_numeros = int(input("¿Cuántos números deseas ingresar? "))
        if cantidad_numeros < 2:
            print("Error: Debes ingresar al menos dos números para esta operación.")
            return
        numeros = obtener_numeros(cantidad_numeros)
        if opcion == "1":
            print("La suma es:", suma(numeros))
        elif opcion == "2":
            print("La resta es:", resta(numeros))
        elif opcion == "3":
            print("La multiplicación es:", multiplicacion(numeros))
        elif opcion == "4":
            resultado = division(numeros)
            if isinstance(resultado, str):
                print(resultado)
            else:
                print("La división es:", resultado)
    elif opcion == "5":
        base = float(input("Ingrese la base: "))
        exponente = float(input("Ingrese el exponente: "))
        print("La potenciación es:", potenciacion(base, exponente))
    elif opcion == "6":
        numero = float(input("Ingrese el número: "))
        print("La raíz cuadrada es:", raiz_cuadrada(numero))
    else:
        print("Opción no válida. Por favor, elige una opción válida.")

def calculadora():
    while True:
        mostrar_menu()
        opcion = input("Ingresa el número de la operación: ")
        if opcion == "7":
            print("¡Hasta luego!")
            break
        ejecutar_operacion(opcion)
        continuar = input("¿Deseas realizar otra operación? (s/n): ")
        if continuar.lower() != "s":
            print("¡Hasta luego!")
            break

# Llamar a la función para que se ejecute
calculadora()