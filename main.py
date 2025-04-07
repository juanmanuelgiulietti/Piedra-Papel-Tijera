import random

def finDelJuego(contadorJugador, contadorComputadora, nombre):
    if (contadorJugador == 5) and (contadorComputadora < 5):
        print(f"El ganador es: {nombre}")
    elif (contadorJugador < 5) and (contadorComputadora == 5):
        print(f"El ganador es: Computadora")

def determinarResultado(eleccion, eleccionRobot, nombre):
    jugador1 = nombre
    jugador2 = "Computadora"
    
    contadorJugador = 0
    contadorComputadora = 0
    
    if eleccion == eleccionRobot:
        print("Empate")
    elif (eleccion == "piedra") and (eleccionRobot == "tijera"):
        print(f"{jugador1} gana!")
        contadorJugador += 1
        print()
        print("Marcador: ")
        print()
        print(f"Computadora: {contadorComputadora}")
        print(f"{nombre}: {contadorJugador}")
    elif (eleccion == "papel") and (eleccionRobot == "piedra"):
        print(f"{jugador1} gana!")
        contadorJugador += 1
        print()
        print("Marcador: ")
        print()
        print(f"Computadora: {contadorComputadora}")
        print(f"{nombre}: {contadorJugador}")
    elif (eleccion == "tijera") and (eleccionRobot == "papel"):
        print(f"{jugador1} gana!")
        contadorJugador += 1
        print()
        print("Marcador: ")
        print()
        print(f"Computadora: {contadorComputadora}")
        print(f"{nombre}: {contadorJugador}")
    elif (eleccion == "piedra") and (eleccionRobot == "papel"):
        print(f"{jugador2} gana!")
        contadorComputadora += 1
        print()
        print("Marcador: ")
        print()
        print(f"Computadora: {contadorComputadora}")
        print(f"{nombre}: {contadorJugador}")
    elif (eleccion == "papel") and (eleccionRobot == "piedra"):
        print(f"{jugador2} gana!")
        contadorComputadora += 1
        print()
        print("Marcador: ")
        print()
        print(f"Computadora: {contadorComputadora}")
        print(f"{nombre}: {contadorJugador}")
    elif (eleccion == "tijera") and (eleccionRobot == "papel"):
        print(f"{jugador2} gana!")
        contadorComputadora += 1
        print()
        print("Marcador: ")
        print()
        print(f"Computadora: {contadorComputadora}")
        print(f"{nombre}: {contadorJugador}")
    return contadorJugador, contadorComputadora

def eleccionComputadora():
    opciones = ["piedra", "papel", "tijera"]
    eleccionRobot = random.choice(opciones)
    return eleccionRobot

def eleccionUsuario():
    nombre = str(input("Ingrese su nombre para iniciar el juego: "))
    print(f"Bienvenidx, {nombre}!")
    eleccion = str(input("Ingrese su eleccion: ").lower())
    
    while (eleccion != "piedra") and (eleccion != "papel") and (eleccion != "tijera"):
        print("Por favor ingrese una respuesta valida.")
        eleccion = str(input("Ingrese su eleccion (piedra, papel o tijera): "))
    return eleccion, nombre
    
def main():
    eleccion, nombre = eleccionUsuario()
    eleccionRobot = eleccionComputadora()
    print()
    print(f"Usuario: {eleccion}")
    print(f"Computadora: {eleccionRobot}")
    contadorJugador, contadorComputadora = determinarResultado(eleccion, eleccionRobot, nombre)
    finDelJuego(contadorJugador, contadorComputadora, nombre)
main()