import json

def leerDatosVentas():
    try:
        with open("ventas_videojuegos.json","r") as fichero:
            datos = json.load(fichero)
        return datos['videojuegos']
    except FileNotFoundError as e:
        print(e)