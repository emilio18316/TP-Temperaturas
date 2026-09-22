def ordenar_temperaturas(temperaturas):
    if len(temperaturas) == 0:
        print("No hay temperaturas cargadas.")
    else:
        cantidad = len(temperaturas)

        for i in range(cantidad - 1):
            for j in range(cantidad - 1 - i):
                if temperaturas[j] > temperaturas[j + 1]:
                    auxiliar = temperaturas[j]
                    temperaturas[j] = temperaturas[j + 1]
                    temperaturas[j + 1] = auxiliar

        print("Temperaturas ordenadas:", temperaturas)
