def main_menu():
    global nombre, paquete, costo, reserva_realizada
    reserva_realizada = False
    while True:
        print("\nBienvenido al sistema de reservaciones del Balneario Aguas Azules")
        print("1. Compra de paquete")
        print("2. Reservaciones")
        print("3. Genera factura")
        print("4. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            nombre, paquete, costo = compra_paquete()
        elif choice == '2':
            if 'paquete' not in locals():
                print("Primero debe comprar un paquete.")
                continue
            reserva_realizada = reservaciones(paquete, costo)
        elif choice == '3':
            if not reserva_realizada:
                print("Debe realizar al menos una reservación antes de generar la factura.")
                continue
            genera_factura(nombre, paquete, costo)
        elif choice == '4':
            print("Gracias por visitar Balneario Aguas Azules. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def compra_paquete():
    print("\nOpciones de paquete:")
    print("1. Principiante - 8 sesiones - Costo: 22000")
    print("2. Intermedio - 8 sesiones - Costo: 24000")
    print("3. Avanzado - 8 sesiones - Costo: 26000")
    print("4. Clase adicional - 1 sesión - Costo: 3500")
    paquete = input("Seleccione el paquete deseado (1/2/3/4): ")
    nombre = input("Ingrese su nombre: ")
    costo = 0
    if paquete == '1':
        costo = 22000
    elif paquete == '2':
        costo = 24000
    elif paquete == '3':
        costo = 26000
    elif paquete == '4':
        costo = 3500
    else:
        print("Opción no válida. Intente de nuevo.")
        return compra_paquete()
    return nombre, paquete, costo

def reservaciones(paquete, costo):
    global reservaciones_hechas
    sesiones = 8 if paquete != 'd' else 1
    reserva_realizada = False
    while sesiones > 0 and reservaciones_hechas < 8:
        print("\nDías disponibles: Lunes a Sábado")
        print("Horarios disponibles: Mañana, Tarde, Noche")
        dia = input("Seleccione el día para la reservación: ")
        horario = input("Seleccione el horario para la reservación: ")
        print(f"Reservación confirmada para el día {dia} en el horario de {horario}.")
        sesiones -= 1
        reservaciones_hechas += 1
        reserva_realizada = True
        if sesiones > 0 and reservaciones_hechas < 8:
            continuar = input(f"Le quedan {sesiones} sesiones. ¿Desea hacer otra reservación? (s/n): ")
            if continuar.lower() != 's':
                break
    return reserva_realizada

def genera_factura(nombre, paquete, costo):
    iva = costo * 0.13
    total = costo + iva
    print("\nBalneario Aguas Azules")
    print("Factura de Contado")
    print(f"Nombre: {nombre}")
    print(f"Paquete: {paquete}")
    print(f"Costo: {costo}")
    print(f"IVA (13%): {iva}")
    print(f"Monto final a pagar: {total}")

if __name__ == "__main__":
    main_menu()
    
    