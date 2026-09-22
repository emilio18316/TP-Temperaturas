def buscar_mayor(temperaturas):
    if len(temperaturas) == 0:
        print("No hay temperaturas cargadas.")
    else:
        mayor = temperaturas[0]

        for temperatura in temperaturas:
            if temperatura > mayor:
                mayor = temperatura

        print("La temperatura mayor es:", mayor)
