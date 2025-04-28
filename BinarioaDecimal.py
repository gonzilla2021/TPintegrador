# Binario a Decimal
def restaNumero(num):
    return num - 1


def BinarioDecimal(numeroBinario):
    count = 0
    for i in range(len(numeroBinario)):
        potencia = restaNumero(len(numeroBinario) - i)
        numBinario = int(numeroBinario[i])
        count += numBinario * (2 ** potencia)
    return count


# Prueba del código
numeroBinario = input("Por favor Ingrese un Numero Binario: ")
print(f"El Decimal de {numeroBinario} es: {BinarioDecimal(numeroBinario)}")

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
