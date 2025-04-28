def decimal_a_binario(decimal):
    if type(decimal) == int:
        # Inicializamos la variable donde construiremos el número binario
        binario = ""

        # Convertimos el número decimal a binario
        while decimal > 0:
            # Obtenemos el residuo y lo añadimos al principio de la cadena
            binario = str(decimal % 2) + binario
            # Dividimos el número entre 2 (división entera) para seguir con el siguiente dígito
            decimal = decimal // 2

        return binario
    else:
        print("Ingreso no valido")

#############################################################################################

def binario_a_decimal(binario):
    #if binario == "1" and binario == "0":

        # Empezamos desde el último exponente (posición más alta)
            exponente = len(binario) - 1

            nroDecimal = 0  # Acumulador del número decimal

        # Recorremos cada dígito binario
            for bit in binario:
                digito = int(bit) * (2 ** exponente)  # Convertimos ese dígito a su valor en decimal
                nroDecimal += digito  # Lo sumamos al total
                exponente -= 1  # Bajamos el exponente para el siguiente dígito

            return nroDecimal
    #else:
    #   print("El número ingresado no es binario")
        
#############################################################################################
# Pedimos al usuario un número en base 10
decimal = int(input("Ingresa un número en base 10: "))
# Mostramos el resultado
print(f"El número {decimal} en base 10 convertido a base 2 es: {decimal_a_binario(decimal)}")

#############################################################################################
# Pedimos al usuario un número en base 2 (como cadena)
binario = input("Ingresa un número en base 2: ")
# Mostramos el resultado final
print(f"El número en decimal es: {binario_a_decimal(binario)}")
