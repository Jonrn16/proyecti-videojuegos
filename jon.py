
def calcularventaspromedioporplataforma(datos: list):
    """
    Funcion que calcula el promedio de ventas divididos en plataforma

    :param datos: Lista de diccionarios con datos de videojuegos
    :return: Un diccionario donde tienes el promedio de ventas totales por plataforma
    """
    ventas = {}
    conteos = {}
    for dato in datos:
        p = dato['plataforma']
        v = dato['ventas_globales']
        ventas[p] = ventas.get(p,0) + v
        conteos[p] = conteos.get(p, 0) + 1
        promedios = {p: ventas[p] / conteos[p] for p in ventas}
        return promedios

def filtrarporrangosanios(datos: list, anio_inicio: int, anio_fin: int):
    """
    Funcion que filtra la lista de juegos a que esten dentro de un cierto rango de años
    :param datos: Lista de diccionarios con datos de videojuegos
    :param anio_inicio: Año inicial del rango (inclusive)
    :param anio_fin: Año final del rango (inclusive)
    :return: Lista filtrada de videojuegos que cumplen con el rango de años
    """
    return [dato for dato in datos
            if anio_inicio <= dato['anio'] >= anio_fin]
