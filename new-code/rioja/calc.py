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
    return numeros[0] - sum(numeros[1:])

def multiplicacion(numeros):
    return math.prod(numeros)

def division(numeros):
    resultado = numeros[0]
    for num in numeros[1:]:
        resultado /= num
    return resultado

def potenciacion(base, exponente):
    return base ** exponente

def raiz_cuadrada(numero):
    return math.sqrt(numero)

def logaritmo(base, numero):
    return math.log(numero, base)

def raiz_cubica(numero):
    return numero ** (1/3)

def factorial(numero):
    return math.factorial(numero)

def mostrar_menu():
    print("\nSelecciona la operación que deseas realizar:")
    print("1. Suma\n2. Resta\n3. Multiplicación\n4. División")
    print("5. Potenciación\n6. Raíz cuadrada\n7. Logaritmo\n8. Raíz cúbica")
    print("9. Factorial\n10. Salir")

def mostrar_historia(opcion):
    historias = {
        "1": "La suma es la operación más básica de todas.",
        "2": "La resta nos ayuda a encontrar la diferencia entre números.",
        "3": "La multiplicación acelera las sumas repetidas.",
        "4": "La división distribuye cantidades equitativamente.",
        "5": "La potenciación eleva un número a la grandeza de su exponente.",
        "6": "La raíz cuadrada deshace la multiplicación en parejas.",
        "7": "El logaritmo descompone el crecimiento exponencial.",
        "8": "La raíz cúbica revela el volumen de un cubo.",
        "9": "El factorial multiplica una serie de números descendentes."
    }
    print(historias.get(opcion, ''))

def ejecutar_operacion(opcion):
    if opcion in ["1", "2", "3", "4"]:
        cantidad_numeros = int(input("¿Cuántos números deseas ingresar? "))
        numeros = obtener_numeros(cantidad_numeros)
        operaciones = {
            "1": suma(numeros),
            "2": resta(numeros),
            "3": multiplicacion(numeros),
            "4": division(numeros)
        }
        print(f"El resultado es: {operaciones[opcion]}")
    elif opcion == "5":
        base = float(input("Ingrese la base: "))
        exponente = float(input("Ingrese el exponente: "))
        print(f"La potenciación es: {potenciacion(base, exponente)}")
    elif opcion == "6":
        numero = float(input("Ingrese el número: "))
        print(f"La raíz cuadrada es: {raiz_cuadrada(numero)}")
    elif opcion == "7":
        base = float(input("Ingrese la base del logaritmo: "))
        numero = float(input("Ingrese el número: "))
        print(f"El logaritmo es: {logaritmo(base, numero)}")
    elif opcion == "8":
        numero = float(input("Ingrese el número: "))
        print(f"La raíz cúbica es: {raiz_cubica(numero)}")
    elif opcion == "9":
        numero = int(input("Ingrese el número (entero): "))
        print(f"El factorial es: {factorial(numero)}")
    elif opcion == "10":
        print("¡Hasta luego!")
    else:
        print("Opción no válida. Por favor, elige una opción válida.")

def calculadora():
    while True:
        mostrar_menu()
        opcion = input("Ingresa el número de la operación (1-10): ")
        if opcion == "10":
            break
        mostrar_historia(opcion)
        ejecutar_operacion(opcion)

# Llamar a la función para que se ejecute
calculadora()
