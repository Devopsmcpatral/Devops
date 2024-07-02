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
                print("\033[91mError: Debes ingresar un número válido.\033[0m")
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

def logaritmo(base, numero):
    return math.log(numero, base)

def raiz_cubica(numero):
    return numero ** (1/3)

def factorial(numero):
    return math.factorial(numero)

def mostrar_menu():
    print("\n\033[94mSelecciona la operación que deseas realizar:\033[0m")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potenciación")
    print("6. Raíz cuadrada")
    print("7. Logaritmo")
    print("8. Raíz cúbica")
    print("9. Factorial")
    print("10. Salir")

def mostrar_historia(opcion):
    historias = {
        "1": "La suma es la operación más básica de todas, ¿cuántas veces la has usado en tu vida diaria?",
        "2": "La resta nos ayuda a encontrar la diferencia entre números, ¡esencial en las compras!",
        "3": "La multiplicación acelera las sumas repetidas, una herramienta poderosa en matemáticas.",
        "4": "La división distribuye cantidades equitativamente, ¡muy útil en la cocina!",
        "5": "La potenciación eleva un número a la grandeza de su exponente, ¡una explosión de crecimiento!",
        "6": "La raíz cuadrada deshace la multiplicación en parejas, revelando sus bases.",
        "7": "El logaritmo descompone el crecimiento exponencial en términos comprensibles.",
        "8": "La raíz cúbica revela el volumen de un cubo en sus dimensiones básicas.",
        "9": "El factorial multiplica una serie de números descendentes, ¡perfecto para combinaciones!",
    }
    print(f"\033[93m{historias.get(opcion, '')}\033[0m")

def ejecutar_operacion(opcion, historial):
    if opcion in ["1", "2", "3", "4"]:
        cantidad_numeros = int(input("¿Cuántos números deseas ingresar? "))
        if cantidad_numeros < 2:
            print("\033[91mError: Debes ingresar al menos dos números para esta operación.\033[0m")
            return
        numeros = obtener_numeros(cantidad_numeros)
        if opcion == "1":
            resultado = suma(numeros)
            print("La suma es:", resultado)
        elif opcion == "2":
            resultado = resta(numeros)
            print("La resta es:", resultado)
        elif opcion == "3":
            resultado = multiplicacion(numeros)
            print("La multiplicación es:", resultado)
        elif opcion == "4":
            resultado = division(numeros)
            if isinstance(resultado, str):
                print("\033[91m" + resultado + "\033[0m")
            else:
                print("La división es:", resultado)
        historial.append(resultado)
    elif opcion == "5":
        base = float(input("Ingrese la base: "))
        exponente = float(input("Ingrese el exponente: "))
        resultado = potenciacion(base, exponente)
        print("La potenciación es:", resultado)
        historial.append(resultado)
    elif opcion == "6":
        numero = float(input("Ingrese el número: "))
        resultado = raiz_cuadrada(numero)
        print("La raíz cuadrada es:", resultado)
        historial.append(resultado)
    elif opcion == "7":
        base = float(input("Ingrese la base del logaritmo: "))
        numero = float(input("Ingrese el número: "))
        resultado = logaritmo(base, numero)
        print("El logaritmo es:", resultado)
        historial.append(resultado)
    elif opcion == "8":
        numero = float(input("Ingrese el número: "))
        resultado = raiz_cubica(numero)
        print("La raíz cúbica es:", resultado)
        historial.append(resultado)
    elif opcion == "9":
        numero = int(input("Ingrese el número (entero): "))
        if numero < 0:
            print("\033[91mError: El factorial no está definido para números negativos.\033[0m")
            return
        resultado = factorial(numero)
        print("El factorial es:", resultado)
        historial.append(resultado)
    else:
        print("\033[91mOpción no válida. Por favor, elige una opción válida.\033[0m")

def calculadora():
    historial = []
    while True:
        mostrar_menu()
        opcion = input("Ingresa el número de la operación: ")
        if opcion == "10":
            print("¡Hasta luego!")
            break
        mostrar_historia(opcion)
        ejecutar_operacion(opcion, historial)
        continuar = input("¿Deseas realizar otra operación? (s/n): ")
        if continuar.lower() != "s":
            print("Historial de operaciones:", historial)
            print("¡Hasta luego!")
            break

# Llamar a la función para que se ejecute
calculadora()
