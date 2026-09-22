from funciones.agregar import agregar_temperatura
from funciones.ver import ver_temperaturas
from funciones.promedio import calcular_promedio
from funciones.mayor import buscar_mayor
from funciones.menor import buscar_menor
from funciones.contar import contar_temperatura
from funciones.ordenar import ordenar_temperaturas


temperaturas = []
opcion = 0

while opcion != 8:
    print("\n--- MENÚ DE TEMPERATURAS ---")
    print("1. Agregar temperatura")
    print("2. Ver temperaturas")
    print("3. Calcular promedio")
    print("4. Buscar mayor")
    print("5. Buscar menor")
    print("6. Contar temperatura")
    print("7. Ordenar temperaturas")
    print("8. Salir")

    opcion = int(input("Elegí una opción: "))

    if opcion == 1:
        agregar_temperatura(temperaturas)

    elif opcion == 2:
        ver_temperaturas(temperaturas)

    elif opcion == 3:
        calcular_promedio(temperaturas)

    elif opcion == 4:
        buscar_mayor(temperaturas)

    elif opcion == 5:
        buscar_menor(temperaturas)

    elif opcion == 6:
        contar_temperatura(temperaturas)

    elif opcion == 7:
        ordenar_temperaturas(temperaturas)

    elif opcion == 8:
        print("Programa finalizado.")

    else:
        print("Opción incorrecta.")
