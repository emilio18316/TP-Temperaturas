def buscar_menor(temperaturas):
    if len(temperaturas) == 0:
        print("No hay temperaturas cargadas.")
    else:
        menor = temperaturas[0]

        for temperatura in temperaturas:
            if temperatura < menor:
                menor = temperatura

        print("La temperatura menor es:", menor)
