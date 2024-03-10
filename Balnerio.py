# Definimos el valor del IVA
iva = 0.13


# Muestra los paquetes disponibles y permite al usuario seleccionar uno.
# Solicita al usuario su nombre.
def compra_paquete():
    print("Paquetes: ")
    print("1. Principiante - 8 Sesiones - Costo: 22000")
    print("2. Intermedio - 8 Sesiones - Costo: 24000")
    print("3. Avanzado - 8 Sesiones - Costo: 26000")
    print("4. Clase Adicional - 1 Sesion - Costo: 3500")
    print("Todos los paquetes pueden disfrutarse en 4 semanas máximo")
    opcion = int(input("Por favor, seleccione el paquete que desea comprar: "))

    if opcion == 1:
        paquete_nombre = 'Principiante'
        paquete_sesiones = 8
        paquete_costo = 22000
    elif opcion == 2:
        paquete_nombre = 'Intermedio'
        paquete_sesiones = 8
        paquete_costo = 24000
    elif opcion == 3:
        paquete_nombre = 'Avanzado'
        paquete_sesiones = 8
        paquete_costo = 26000
    elif opcion == 4:
        paquete_nombre = 'Clase Adicional'
        paquete_sesiones = 1
        paquete_costo = 3500
    nombre = input("Por favor, ingrese su nombre: ")
    return nombre, paquete_nombre, paquete_sesiones, paquete_costo

# Permite al usuario hacer una reservación si antes se compró un paquete.
# El usuario puede seleccionar el dia y el horario de la reservación.
# También actualiza las reservaciones restantes hasta llegar a 8.

def reservaciones_f(paquete_nombre, paquete_sesiones):
    if paquete_nombre == '':
        print("Por favor, primero compre un paquete para hacer la reservacion.")
        return paquete_nombre, paquete_sesiones
    print("Dias disponibles")
    print("1. Lunes")
    print("2. Martes")
    print("3. Miercoles")
    print("4. Jueves")
    print("5. Viernes")
    print("6. Sabado")
    dia = int(input("Por favor, seleccione el dia para su reservacion: "))

    if dia == 1:
        dia_reservado = 'Lunes'
    elif dia == 2:
        dia_reservado = 'Martes'
    elif dia == 3:
        dia_reservado = 'Miercoles'
    elif dia == 4:
        dia_reservado = 'Jueves'
    elif dia == 5:
        dia_reservado = 'Viernes'
    elif dia == 6:
        dia_reservado = 'Sabado'
    else:
        print("Opcion no disponible")

    print("Horarios disponibles: ")
    print("1. Manana")
    print("2. Tarde")
    print("3. Noche")
    horario = int(input("Por favor, seleccione el horario para su reservacion"))

    if horario == 1:
        horario_reservado = 'Manana'
    elif horario == 2:
        horario_reservado = 'Tarde'
    elif horario == 3:
        horario_reservado = 'Noche'
    else:
        print("Opcion no disponible")

    paquete_sesiones -= 1
    print("Reservacion realizada para el dia", dia_reservado, "en la", horario_reservado)
    print("Sesiones restantes en su paquete:", paquete_sesiones)
    return paquete_nombre, paquete_sesiones

# Genera una factura con los datos ingresados por el usuario.
# Muestra el nombre del usuario, los detalles del paquete y el total, incluyendo el IVA.

def genera_factura(nombre, paquete_nombre, paquete_costo):
    
    if not nombre or not paquete_nombre:
        print("Por favor, primero realice una compra para obtener una factura.")
        return
    print("Factura")
    print("Nombre del cliente:", nombre)
    print("Paquete:", paquete_nombre)
    print("Precio del paquete:", paquete_costo)
    iva_m = paquete_costo * iva
    print("IVA:", iva_m)
    total = paquete_costo + iva_m
    print("Total a pagar:", total)

# Es la función principal que ejecuta el programa
# Imprime el menú de opciones al usuario y llama las funciones dependiendo la opción seleccionada.
# El programa se ejecuta en bucle hasta que el usuario use la opción para salir.

def main():
    nombre, paquete_nombre, paquete_sesiones, paquete_costo = '', '', 0, 0
    reservaciones = 0
    while True:
        print("1. Compra de paquetes")
        print("2. Reservaciones")
        print("3. Genera factura")
        print("4. Salir")
        opcion = int(input("Por favor, seleccione una opcion:"))

        if opcion == 1:
            nombre, paquete_nombre, paquete_sesiones, paquete_costo = compra_paquete()
        elif opcion == 2:
            if reservaciones < 8:
                paquete_nombre, paquete_sesiones = reservaciones_f(paquete_nombre, paquete_sesiones)
                reservaciones += 1
            else:
                print("Ya ha realizado el maximo de 8 reservaciones")
        elif opcion == 3:
            genera_factura(nombre, paquete_nombre, paquete_costo)
        elif opcion == 4:
            print("Gracias por usar nuestro programa, adios.")
            break
main()
    
