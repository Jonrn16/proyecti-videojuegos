import chema
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

    opcion = input("Seleccione una opcion (0-7): ")

    if opcion == 1:
        generarReporteCompleto(datos)
    elif opcion == 2:
        region = input("Escoge la region a ver (eu,na,jp): ")
        topVentasPorRegion(datos, region, n)
    elif opcion == 3:
        analizarPorGenero(datos)
    elif opcion == 4:
        calcularVentasPromedioPorPlataforma(datos)
    elif opcion == 5:
        filtrarPorRangoAnyos(datos, anyo_inicio, anyo_fin):
    elif opcion == 6:
        calcularVentasTotales(datos)
    elif opcion == 7:
        leerDatosVentas()
    elif opcion == 0:
        funcional = False
    else:
        print("Opcion no valida")
