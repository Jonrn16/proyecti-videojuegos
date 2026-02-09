import json

def leerDatosVentas():
    """
    function para leer los datos de los juegos
    :return: devuelve un reporte completo con todos los datos del archivo.json
    """
    try:
        with open("ventas_videojuegos.json", "r", encoding="utf-8") as fichero:
            datos = json.load(fichero)
        return datos["videojuegos"]
    except FileNotFoundError as e: print("Error: archivo no encontrado.", e)


#Función que recibe la lista de diccionarios con los datos de ventas y calcula las ventas totales agregadas por cada región.
def calcularVentas(datos):
    """
        function para calcular las ventas totales de videojuegos
        :param: datos del archivo ventas_videojuegos.json
        :return: Función que recibe la lista de diccionarios con los datos de ventas y calcula las ventas totales agregadas por cada región.
    """

    total_regiones = {"eu" : 0, "na" : 0, "jp" : 0, "otros" : 0, "globales" : 0}

    for juegos in datos:

        total_regiones["eu"] += juegos["ventas_eu"]
        total_regiones["na"] += juegos["ventas_na"]
        total_regiones["jp"] += juegos["ventas_jp"]
        total_regiones["otros"] += juegos["ventas_otros"]
        total_regiones["globales"] += juegos["ventas_global"]

    return total_regiones

def calcularVentasPorRegion(datos, region, n):
    """
        function que encuentra los n videojuegos con más ventas en una región específica.
        :param: pasamos como parámetro las ventas y los datos del archivo json y se ordenan en un ranking con un índice n
        :return: devuelve que encuntra los viedojuegos mas vendidos por región y los muestra ordenados por pantalla.
    """

    regiones_validas = ["eu", "na", "jp", "otros", "global"]
    if region not in regiones_validas:
        raise ValueError(f"Región inválida. Debe ser una de: {regiones_validas}")
    ventasTotales = []
    for juego in datos:
        clave = "ventas_" + region
        ventasTotales.append((juego["nombre"], juego[clave]))

    juegosOrdenados = sorted(ventasTotales, key=lambda x: x[1], reverse=True)

    return juegosOrdenados[:n]
