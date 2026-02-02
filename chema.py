import json

#Funcion para leer los datos de los juegos;
def leerDatosVentas():
    try:
        with open("ventas_videojuegos.json","r") as fichero:
            datos = json.load(fichero)
        return datos['videojuegos']
    except FileNotFoundError as e:
        print(e)
#Función que recibe la lista de diccionarios con los datos de ventas y calcula las ventas totales agregadas por cada región.
def calcularVentas(datos):
    print()

    total_regiones = {"eu" : 0, "na" : 0, "jp" : 0, "otros" : 0, "globales" : 0}

    for juegos in datos:

        total_regiones["eu"] += juegos["ventas_eu"]
        total_regiones["na"] += juegos["ventas_na"]
        total_regiones["jp"] += juegos["ventas_jp"]
        total_regiones["otros"] += juegos["ventas_otros"]
        total_regiones["globales"] += juegos["ventas_globales"]

    return total_regiones

#Función que encuentra los n videojuegos con más ventas en una región especifica.
def calcularVentasPorRegion(datos, region, n):

    ventasTotales = []

    for viedojuegos in ventasTotales:
        juegos = (viedojuegos["nombre"], viedojuegos["ventas " + region])
        ventasTotales.append(juegos)

    juegosOrdenados = sorted(ventasTotales, key = lambda x: x[1], reverse=True)

    return  juegosOrdenados[:n]
