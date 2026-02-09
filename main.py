import chema, jon, adri
funcional = True
datos = chema.leerDatosVentas()

while(funcional):
    print("Analisis de Ventas de Videojuegos")

    print("1. Ver reporte completo")
    print("2. Top ventas por region")
    print("3. Analisis por genero")
    print("4. Ventas promedio por plataforma")
    print("5. Filtrar por rango de años")
    print("6. Calcular ventas totales")
    print("7. Ver todos los datos")
    print("0. salir")

    opcion = int(input("Seleccione una opcion (0-7): "))

    if opcion == 1:
        adri.GenerarReporteCompleto(datos)
    elif opcion == 2:
        region = input("Escoge la región (na, eu, jp, otros o global): ").strip().lower()
        n = int(input("¿Cuántos juegos quieres ver en el ranking?: "))
        try:
            resultado = chema.calcularVentasPorRegion(datos, region, n)
            print(f"\nTop {n} ventas en región:", region)
            for nombre, ventas in resultado:
                print(f"- {nombre}: {ventas}")
        except ValueError as e:
            print("Error:", e)
    elif opcion == 3:
        print(adri.AnalizarPorGenero(datos))
    elif opcion == 4:
        jon.calcularventaspromedioporplataforma(datos)
    elif opcion == 5:
        inicio = int(input("Introduce el año de inicio para filtrar: "))
        fin = int(input("Introduce el año de fin para filtrar: "))
        print(jon.filtrarporrangosanios(datos, inicio, fin))
    elif opcion == 6:
        print(chema.calcularVentas(datos))
    elif opcion == 7:
        print(chema.leerDatosVentas())
    elif opcion == 0:
        funcional = False
    else:
        print("Opcion no valida")