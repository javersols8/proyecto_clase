carro = {"marca":"Porsche",
        "Modelo":"Carrera ",
        "color":"Rojo y Blanco",
        "Año":"2026"}

input("ingrese el dato que desea saber: ").capitalize()

def dato(input):
    dato = input.get()
    
if dato == "marca":
    print(carro["marca"])
else:
    print("Dato no valido")