from jon import calcularventaspromedioporplataforma
from chema import calcularVentas, calcularVentasPorRegion, leerDatosVentas


def AnalizarPorGenero(datos):
    """
    Función que analiza las ventas agrupadas por género de videojuegos
    :param datos: Es una lista de diccionario con los datos de los videojuegos
    :return: Un diccionario con los datos de ventas por genero
    """
    analisis = {}
    for juego in datos:
        g = juego['genero']
        if g not in analisis:
            analisis[g] = {
                'cantidad_juegos': 0,
                'ventas_global': 0.0,
                'ventas_na': 0.0,
                'ventas_eu': 0.0,
                'ventas_jp': 0.0
            }
        analisis[g]['cantidad_juegos'] += 1
        analisis[g]['ventas_global'] += juego['ventas_global']
        analisis[g]['ventas_na'] += juego['ventas_na']
        analisis[g]['ventas_eu'] += juego['ventas_eu']
        analisis[g]['ventas_jp'] += juego['ventas_jp']
    return analisis

def GenerarReporteCompleto(datos):
    """
    Muestra en un reporte completo en base al archivo json.
    :param datos: Una lista de diccionarios con datos de videojuegos
    :return: Imprime el informe directamente en consola
    """
    print("\n--- INFORME FINAL DE VENTAS ---")
    totales = calcularVentas(datos)
    print(f"Juegos analizados: {len(datos)}")
    print(f"Ventas Globales: {totales['globales']:.2f}M")
    
    print("\nTOP 5 POR REGIÓN (GLOBAL):")
    for nombre, venta in calcularVentasPorRegion(datos, 'global', 5):
        print(f"- {nombre}: {venta}M")
        
    print("\nVENTAS MEDIAS POR CONSOLA:")
    promedios = calcularventaspromedioporplataforma(datos)
    for plat, media in sorted(promedios.items(), key=lambda x: x[1], reverse=True):
        print(f"* {plat}: {media:.2f}M")
    print("-------------------------------\n")


