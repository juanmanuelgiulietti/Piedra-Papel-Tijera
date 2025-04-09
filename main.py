import random

def finDelJuego(contadorJugador, contadorComputadora, nombre):
    print("Marcador:")
    print(f"Computadora: {contadorComputadora}")
    print(f"{nombre}: {contadorJugador}")

def determinarResultado(eleccion, eleccionRobot, nombre, contadorJugador, contadorComputadora):
    if eleccion == eleccionRobot:
        print("Empate")
    else:
        if ((eleccion == "piedra" and eleccionRobot == "tijera") or (eleccion == "papel" and eleccionRobot == "piedra") or (eleccion == "tijera" and eleccionRobot == "papel")):
            print(f"{nombre} gana!")
            contadorJugador += 1
        else:
            print("Computadora gana!")
            contadorComputadora += 1
            
    finDelJuego(contadorJugador, contadorComputadora, nombre)
    return contadorJugador, contadorComputadora

def eleccionComputadora():
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)

def eleccionUsuario():
    eleccion = input("Ingrese su eleccion (piedra, papel o tijera): ").lower()
    
    while (eleccion != "piedra") and (eleccion != "papel") and (eleccion != "tijera"):
        print("Por favor ingrese una respuesta valida.")
        eleccion = input("Ingrese su eleccion (piedra, papel o tijera): ")
    return eleccion
    
def main():
    nombre = input("Ingrese su nombre para iniciar el juego: ")
    print(f"Bienvenidx, {nombre}!")
    
    contadorJugador = 0
    contadorComputadora = 0
    
    while contadorJugador < 5 and contadorComputadora < 5:
        eleccion = eleccionUsuario()
        eleccionRobot = eleccionComputadora()
        print(f"\nUsuario: {eleccion}")
        print(f"Computadora: {eleccionRobot}")
        
        contadorJugador, contadorComputadora = determinarResultado(eleccion, eleccionRobot, nombre, contadorJugador, contadorComputadora)
        
    if contadorJugador == 5:
        print(f"El ganador es: {nombre}")
    elif contadorComputadora == 5:
        print("El ganador es: Computadora")
main()