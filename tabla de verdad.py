verdad = [True, False]


# Aplique el Uso de la IA para que me ayude no tener tantas lineas de codigo y hacer que visualmente la tabla se vea mucho mejor

while (True):
    eleccion = int(input(f"{"-" * 5} Eliga la Opcion para la Tabla de Verdad {"-" * 5}\nOpcion 1 - Tabla de Conjucion (AND)\nOpcion 2 - Tabla de Disyuncion (OR)\nOpcion 3 - Tabla de Negacion (NOT)\nOpcion 4 - SALIR\nOpcion: "))

    if (eleccion not in [1, 2, 3]):
        print("Hasta Luego!")
        break
    elif (eleccion == 1):
        print("")
        print(" A   |   B   | A AND B")
        print("--------------------------")
        for a in verdad:
            for b in verdad:
                result = a and b
                print(f"{a} | {b}  |  {result}")
                print("\t")
    elif (eleccion == 2):
        print("")
        print(" A    |   B    |  A OR B")
        print("------------------------")
        for a in verdad:
            for b in verdad:
                result = a or b
                print(f"{a}  |  {b}  |  {result}")
                print("\t")
    elif (eleccion == 3):
        print("")
        print(" A   |  NOT A")
        print("----------------")
        for a in verdad:
            result = not a
            print(f"{a} | {result}")
            print("\t")