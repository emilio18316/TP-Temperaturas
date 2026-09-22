def contar_temperatura(temperaturas):
    if len(temperaturas) == 0:
        print("No hay temperaturas cargadas.")
    else:
        buscada = float(input("Ingresá la temperatura que querés contar: "))
        cantidad = 0

        for temperatura in temperaturas:
            if temperatura == buscada:
                cantidad = cantidad + 1

        print("La temperatura", buscada, "se repite", cantidad, "veces.")
