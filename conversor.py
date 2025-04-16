# Pedimos al usuario un número en base 10
decimal = int(input("Ingresa un número en base 10: "))

# Guardamos el número original para mostrarlo al final
original = decimal

# Inicializamos la variable donde construiremos el número binario
binario = ""

# Convertimos el número decimal a binario
while decimal > 0:
    # Obtenemos el residuo y lo añadimos al principio de la cadena
    binario = str(decimal % 2) + binario
    # Dividimos el número entre 2 (división entera) para seguir con el siguiente dígito
    decimal = decimal // 2

# Mostramos el resultado
print(f"El número {original} en base 10 convertido a base 2 es: {binario}")

###############################################################################################

# Pedimos al usuario un número en base 2 (como cadena)
binario = input("Ingresa un número en base 2: ")

# Empezamos desde el último exponente (posición más alta)
exponente = len(binario) - 1

nroDecimal = 0  # Acumulador del número decimal

# Recorremos cada dígito binario
for bit in binario:
    digito = int(bit) * (2 ** exponente)  # Convertimos ese dígito a su valor en decimal
    nroDecimal += digito  # Lo sumamos al total
    exponente -= 1  # Bajamos el exponente para el siguiente dígito

# Mostramos el resultado final
print(f"El número en decimal es: {nroDecimal}")
