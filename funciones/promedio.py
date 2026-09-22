def calcular_promedio(temperaturas):
    if len(temperaturas) == 0:
        print("No hay temperaturas cargadas.")
    else:
        suma = 0

        for temperatura in temperaturas:
            suma = suma + temperatura

        promedio = suma / len(temperaturas)
        print("El promedio es:", promedio)
