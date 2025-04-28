# ==================================================
# Conversor de bases numéricas (Decimal <-> Binario)
# ==================================================

# 🔹 Importamos el módulo sys, que nos da acceso a funciones del sistema.
# En este programa lo usamos para salir del programa con sys.exit()
import sys

# 🧾 Función para mostrar el menú principal en pantalla
def mostrar_menu():
    print("\n" + "="*50)  # Imprime una línea de separación
    print("CONVERSOR DE BASES NUMÉRICAS".center(50))  # Centra el título
    print("="*50)
    print("1. Decimal a Binario")  # Opción para convertir de decimal a binario
    print("2. Binario a Decimal")  # Opción para convertir de binario a decimal
    print("3. Salir")  # Opción para salir del programa
    print("="*50)

# 🔢 Función para convertir de decimal a binario (solo positivos)
def decimal_a_binario():
    while True:
        entrada = input("\nIngresa un número entero positivo: ")  # Solicitamos entrada

        # Intentamos convertir la entrada a entero
        try:
            decimal = int(entrada)
            if decimal < 0:
                # Si el número es negativo, mostramos error y pedimos otro
                print("❌ Error: Solo se permiten números positivos.")
                continue
            break  # Si es válido, salimos del bucle
        except ValueError:
            print("❌ Error: Debes ingresar un número entero válido.")

    original = decimal  # Guardamos el número original para mostrarlo después

    # Caso especial: si el número es 0, el binario es simplemente "0"
    if decimal == 0:
        binario = "0"
    else:
        binario = ""
        # Realizamos la conversión dividiendo por 2 y almacenando los restos
        while decimal > 0:
            binario = str(decimal % 2) + binario  # Agregamos el bit a la izquierda
            decimal = decimal // 2  # Dividimos entre 2

    return binario, original  # Devolvemos el binario y el número original

# 🧮 Función para convertir de binario a decimal (solo binarios simples)
def binario_a_decimal():
    while True:
        binario = input("\nIngresa un número binario (ej: 1010): ").strip()  # Solicitamos entrada

        # Validamos que solo contenga caracteres 0 o 1
        if not all(c in {'0', '1'} for c in binario):
            print("❌ Error: Solo se permiten dígitos 0 y 1.")
            continue
        
        # Validamos que haya al menos un dígito
        if len(binario) == 0:
            print("❌ Error: Debes ingresar al menos un dígito binario.")
            continue
        
        break  # Si pasa todas las validaciones, salimos del bucle

    exponente = len(binario) - 1  # Comenzamos desde el bit más significativo
    nroDecimal = 0  # Acumulador para el resultado

    # Recorremos cada bit y sumamos su valor en base 10
    for bit in binario:
        nroDecimal += int(bit) * (2 ** exponente)  # Valor del bit multiplicado por 2^posición
        exponente -= 1

    return nroDecimal, binario  # Devolvemos el número decimal y el binario original

# 🧠 Función principal que maneja el flujo del programa
def main():
    while True:
        mostrar_menu()  # Mostramos el menú
        opcion = input("\nSelecciona una opción (1-3): ")  # Leemos opción del usuario

        # Evaluamos la opción elegida
        if opcion == "1":
            binario, original = decimal_a_binario()  # Convertimos decimal a binario
            print(f"\nEl número {original} en decimal es {binario} en binario")
        elif opcion == "2":
            nroDecimal, binario = binario_a_decimal()  # Convertimos binario a decimal
            print(f"\nEl número binario {binario} es {nroDecimal} en decimal")
        elif opcion == "3":
            print("\n¡Gracias por usar el conversor! Hasta pronto.")
            sys.exit()  # Salimos del programa de forma segura
        else:
            print("❌ Opción no válida. Por favor ingresa 1, 2 o 3.")

        input("\nPresiona Enter para continuar...")  # Pausa antes de volver al menú

# 🚀 Ejecutamos la función principal 
main()
