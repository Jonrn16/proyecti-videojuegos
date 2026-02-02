
def calcularVentasPromedioPorPlataforma(datos):
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

def filtrarPorRangosAnios(datos, anio_inicio, anio_fin):
    listaFiltrada = []

    for dato in datos:
        if anio_inicio < dato.anio < anio_fin:
            listaFiltrada.append(dato)

    return listaFiltrada
