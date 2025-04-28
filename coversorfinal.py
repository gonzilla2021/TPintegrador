def decimal_a_binario(decimal):
    if decimal == 0:
        return "0"

    binario = ""
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2

    return binario

# -------------------------------------------------------------------------------------------------------

def binario_a_decimal(binario):
    # Verificamos que solo tenga ceros y unos
    es_binario = True
    for caracter in binario:
        if caracter != "0" and caracter != "1":
            es_binario = False
            break

    if not es_binario:
        return "Error: El número ingresado no es un número binario válido."

    exponente = len(binario) - 1
    nroDecimal = 0

    for bit in binario:
        digito = int(bit) * (2 ** exponente)
        nroDecimal += digito
        exponente -= 1

    return nroDecimal

# -------------------------------------------------------------------------------------------------------

# VALIDACIÓN Y MANEJO DE ERRORES PARA DECIMAL
entrada_decimal = input("Ingresa un número en base 10: ")

if entrada_decimal.isdigit():
    decimal = int(entrada_decimal)
    print(f"{decimal} en binario es: {decimal_a_binario(decimal)}")
else:
    print("Error: Solo se permiten números enteros positivos en base 10.")

# -------------------------------------------------------------------------------------------------------

# VALIDACIÓN Y MANEJO DE ERRORES PARA BINARIO
binario = input("Ingresa un número en base 2: ")

if len(binario) > 0 and all(c in "01" for c in binario):
    resultado = binario_a_decimal(binario)
    print(f"{binario} en decimal es: {resultado}")
else:
    print("Error: El número ingresado no es binario (solo se permiten dígitos 0 y 1).")
