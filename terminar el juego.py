from funcion import juego
nivel=int(input("seleccione el nivel en el que desea jugar del 1 al 4: "))
while nivel<1 or nivel>4:
    print("el nivel seleccionado no existe")
    nivel=int(input("seleccione el nivel en el que desea jugar del 1 al 4: "))
if nivel==1:
    juego(100)
if nivel==2:
    juego(1000)
if nivel==3:
    juego(1000000)
if nivel==4:
    juego(1000000000000)