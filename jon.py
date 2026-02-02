
def calcularventaspromedioporplataforma(datos: list):
    """
    Funcion que calcula el promedio de ventas divididos en plataforma

    :param datos: Lista de diccionarios con datos de videojuegos
    :return: Un diccionario donde tienes el promedio de ventas totales por plataforma
    """
    ventas = {}
    wii = 0
    gb = 0
    nes = 0
    for dato in datos:
        if ventas.__contains__(dato.plataforma):
            ventas[dato.plataforma] += dato
        else:
            ventas[dato.plataforma] = dato

        if dato.plataforma == "wii":
            wii += 1
        elif dato.plataforma == "nes":
            nes += 1
        else:
            gb += 1

    ventas["wii"] = ventas["wii"]/wii
    ventas["gb"] = ventas["gb"]/wii
    ventas["nes"] = ventas["nes"]/wii
    return ventas

def filtrarporrangosanios(datos: list, anio_inicio: int, anio_fin: int):
    """
    Funcion que filtra la lista de juegos a que esten dentro de un cierto rango de años
    :param datos: Lista de diccionarios con datos de videojuegos
    :param anio_inicio: Año inicial del rango (inclusive)
    :param anio_fin: Año final del rango (inclusive)
    :return: Lista filtrada de videojuegos que cumplen con el rango de años
    """

    listafiltrada = []

    for dato in datos:
        if anio_inicio < dato.anio < anio_fin:
            listafiltrada.append(dato)

    return listafiltrada
