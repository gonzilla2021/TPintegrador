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
print(f"El Decima de {numeroBinario} es: {BinarioDecimal(numeroBinario)}")
