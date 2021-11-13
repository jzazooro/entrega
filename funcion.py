def juego(a):
    import random
    numero=random.randint(0,a)
    intento=int(input("Por favor introduzca un numero entre 0 y a : "))
    intentosrealizados=0
    maximointentos=0.5*a
    while intento!=numero:
        if maximointentos==intentosrealizados: 
            break
            while intento<0 or intento>a:
                print("el numero escogido no es valido")
                intentosrealizados=intentosrealizados+1
                intento=int(input("Por favor introduzca un nuevo numero: "))
            while numero>intento:
                print("El numero escogido es demasiado pequeño")
                intentosrealizados=intentosrealizados+1
                intento=int(input("Por favor introduzca un nuevo numero: "))
            while numero<intento:
                print("El numero escogido es demasiado grande")
                intentosrealizados=intentosrealizados+1
                intento=int(input("Por favor introduzca un nuevo numero: "))
    if intento == numero:
        print("¡Has ganado!")
        intentosrealizados=intentosrealizados+1
        print("El numero era el", numero)
        print("Has necesitado", intentosrealizados, "intentos")
        nombre=input("introduce tu nickname: ")