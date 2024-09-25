# Variables globales para almacenar las tarifas y registros
tarifa_general = [0, 0]
registros_automoviles = []
registros_motocicletas = []
vehiculos = []
hora_inicial = [0, 0]

def menu():
    opc = 1
    while opc > 0 and opc < 8:
        print(" 1. Tarifas")
        print(" 2. Ingresar vehículo")
        print(" 3. Buscar vehículo")
        print(" 4. Mostrar registros")
        print(" 5. Salida de vehículo")
        print(" 6. Buscar factura")
        print(" 7. Cuadre de caja")
        print(" 8. Salir")

        opc = int(input("\n\tDigite una opción: "))

        if opc == 1:
            menu_tarifas()
        if opc == 2:
            factura = 1
            ingresar_vehiculo(factura)
        if opc == 3:
            buscar_vehiculos()
        if opc == 4:
            mostrar_registros()
        if opc == 5:
            salida_vehiculos()
        if opc == 6:
            buscar_factura(vehiculos)
        if opc == 7:
            cuadre_caja(vehiculos)
        else:
            print("Ingrese una opción valida \n")
            menu()

def menu_tarifas():
    opc = 1
    while opc > 0 and opc < 5:
        print(" 1. Ingresar tarifas")
        print(" 2. Mostrar tarifas")
        print(" 3. Modificar tarifas")
        print(" 4. Regresar al menú principal")

        opc = int(input("\n\tDigite una opción: "))
        if opc == 1:
            ingresar_tarifas()
        if opc == 2:
            print('Valor por minuto auto:', tarifa_general[0])
            print('Valor por minuto moto:', tarifa_general[1])
        if opc == 3:
            modificar_tarifas()
        if opc == 4:
            menu()
        else:
            print("Ingrese una opción valida \n")
            menu_tarifas()

def ingresar_tarifas():
    opc = 1
    while opc > 0 and opc < 4:
        print(" 1. Ingresar tarifa de automóvil")
        print(" 2. Ingresar tarifa de motocicleta")
        print(" 3. Regresar al subMenú Tarifas")

        opc = int(input("\n\tDigite una opción: "))

        if opc == 1:
            tarifa_auto = int(input('Ingresa el valor a cobrar por minuto para automóviles: '))
            tarifa_general[0] = tarifa_auto
        if opc == 2:
            tarifa_moto = int(input('Ingresa el valor a cobrar por minuto para motocicletas: '))
            tarifa_general[1] = tarifa_moto
        if opc == 3:
            menu_tarifas()

def modificar_tarifas():
    opc = 1
    while opc > 0 and opc < 4:
        print('1. Modificar tarifa de automóvil.')
        print('2. Modificar tarifa de motocicleta.')
        print('3. Regresar al submenú tarifas.')

        opc = int(input('\n\tDigite una opción: '))

        if opc == 1:
            tarifa_auto = int(input('Ingresa el nuevo valor a cobrar por minuto para automóviles: '))
            tarifa_general[0] = tarifa_auto
        if opc == 2:
            tarifa_moto = int(input('Ingresa el nuevo valor a cobrar por minuto para motocicletas: '))
            tarifa_general[1] = tarifa_moto
        if opc == 3:
            menu_tarifas()

def ingresar_vehiculo(factura):
    tipo_vehiculo = input("Tipo de vehículo (a: automóvil, m: motocicleta): ").lower()
    if tipo_vehiculo != 'a' and tipo_vehiculo != 'm':
        print("Tipo de vehículo no válido.")
        return
    placa = input("Número de la placa: ").upper()
    if not placa:
        print("Placa no válida.")
        return
    hora = input("Hora (formato de 24 horas - hhmm): ")
    if len(hora) != 4 or not hora.isdigit():
        print("Hora no válida.")
        return
    nombre_cliente = input("Nombre del cliente: ")
    if not nombre_cliente:
        print("Nombre no válido.")
        return

    hh = int(hora[:2])
    mm = int(hora[2:])
    hora_inicial[0] = hh
    hora_inicial[1] = mm
    if (hh >= 0 and hh <= 23) and (mm >= 0 and mm <= 59):
        if tipo_vehiculo == 'a':
            for registro in registros_automoviles:
                factura += 1
                if registro[1] == placa:
                    print("La placa ya está registrada")
                    return
            registro_automovil = [factura, placa, hora, nombre_cliente, '', 0, 0, tipo_vehiculo]
            registros_automoviles.append(registro_automovil)
            vehiculos.append(registro_automovil)
        elif tipo_vehiculo == 'm':
            for registro in registros_motocicletas:
                if registro[1] == placa:
                    print("La placa ya está registrada")
                    return
            registro_motocicleta = [factura, placa, hora, nombre_cliente, '', 0, 0, tipo_vehiculo]
            registros_motocicletas.append(registro_motocicleta)
            vehiculos.append(registro_motocicleta)
    else:
        print("Formato de hora incorrecto.")

def buscar_vehiculos():
    opc = 1
    while opc > 0 and opc < 4:
        print('1. Buscar motocicletas.')
        print('2. Buscar automóviles.')
        print('3. Regresar al menú principal')

        opc = int(input('\n\tDigite una opción: '))

        if opc == 1:
            buscar_moto()
        if opc == 2:
            buscar_auto()
        if opc == 3:
            menu()

def buscar_moto():
    placa = input("Ingresa la placa de la motocicleta: ").upper()
    for registro in registros_motocicletas:
        if registro[1] == placa:
            print('Factura N:', registro[0])
            print("Placa:", registro[1])
            print("Hora de ingreso:", registro[2])
            print("Hora de salida:", registro[4])
            print("Nombre:", registro[3])
            print("Número minutos:", registro[5])
            print("Total:", registro[6])
            return
    print('La placa ingresada no está registrada en el sistema.')

def buscar_auto():
    placa = input("Ingresa la placa del automóvil: ").upper()
    for registro in registros_automoviles:
        if registro[1] == placa:
            print('Factura N:', registro[0])
            print("Placa:", registro[1])
            print("Hora de ingreso:", registro[2])
            print("Hora de salida:", registro[4])
            print("Nombre:", registro[3])
            print("Número minutos:", registro[5])
            print("Total:", registro[6])
            return
    print('La placa ingresada no está registrada en el sistema.')

def mostrar_registros():
    opc = 1
    while opc > 0 and opc < 4:
        print('1. Mostrar todos los automóviles.')
        print('2. Mostrar todas las motocicletas.')
        print('3. Regresar al menú principal')

        opc = int(input('\n\tDigite una opción: '))

        if opc == 1:
            print('Tipo de búsqueda: AUTOMÓVILES.')
            mostrara()
        if opc == 2:
            print('Tipo de búsqueda: MOTOCICLETAS.')
            mostrarm()
        if opc == 3:
            menu()

def mostrara():
    n = len(registros_automoviles)
    print("FACTURA PLACA INGRESO NOMBRE SALIDA MINUTOS TOTAL")
    for i in range(n):
        for j in range(7):
            print(registros_automoviles[i][j], end="   ")
        print()

def mostrarm():
    n = len(registros_motocicletas)
    print("FACTURA PLACA INGRESO NOMBRE SALIDA MINUTOS TOTAL")
    for i in range(n):
        for j in range(7):
            print(registros_motocicletas[i][j], end="   ")
        print()

def salida_vehiculos():
    print('Si desea regresar al menú principal escriba la palabra "salir"')
    tipo_vehiculo = input('Ingresa el tipo de vehículo: ').lower()
    if tipo_vehiculo == 'salir':
        menu()
    elif tipo_vehiculo == 'a':
        salida_automovil()
    elif tipo_vehiculo == 'm':
        salida_motocicleta()
    else:
        print("Tipo de vehículo no válido.")

def salida_automovil():
    placa = input("Placa del automóvil: ").upper()
    for registro in registros_automoviles:
        if registro[1] == placa:
            if registro[4]:
                print("El vehículo ya ha registrado la salida.")
            else:
                hora_salida = input("Hora de salida (formato de 24 horas - hhmm): ")
                if len(hora_salida) != 4 or not hora_salida.isdigit():
                    print("Hora no válida.")
                    return
                hh_salida = int(hora_salida[:2])
                mm_salida = int(hora_salida[2:])
                if (hh_salida >= 0 and hh_salida <= 23) and (mm_salida >= 0 and mm_salida <= 59):
                    registro[4] = hora_salida
                    minutos = calcular_minutos(registro[2], hora_salida)
                    total_pagar = minutos * tarifa_general[0]
                    registro[5] = minutos
                    registro[6] = total_pagar
                    print("Salida registrada.")
                    print(f"Factura N: {registro[0]}")
                    print(f"Placa: {registro[1]}")
                    print(f"Hora de ingreso: {registro[2]}")
                    print(f"Hora de salida: {registro[4]}")
                    print(f"Nombre: {registro[3]}")
                    print(f"Número minutos: {registro[5]}")
                    print(f"Total: {registro[6]}")
                else:
                    print("Formato de hora incorrecto.")
            return
    print("La placa ingresada no está registrada en el sistema.")

def salida_motocicleta():
    placa = input("Placa de la motocicleta: ").upper()
    for registro in registros_motocicletas:
        if registro[1] == placa:
            if registro[4]:
                print("El vehículo ya ha registrado la salida.")
            else:
                hora_salida = input("Hora de salida (formato de 24 horas - hhmm): ")
                if len(hora_salida) != 4 or not hora_salida.isdigit():
                    print("Hora no válida.")
                    return
                hh_salida = int(hora_salida[:2])
                mm_salida = int(hora_salida[2:])
                if (hh_salida >= 0 and hh_salida <= 23) and (mm_salida >= 0 and mm_salida <= 59):
                    registro[4] = hora_salida
                    minutos = calcular_minutos(registro[2], hora_salida)
                    total_pagar = minutos * tarifa_general[1]
                    registro[5] = minutos
                    registro[6] = total_pagar
                    print("Salida registrada.")
                    print(f"Factura N: {registro[0]}")
                    print(f"Placa: {registro[1]}")
                    print(f"Hora de ingreso: {registro[2]}")
                    print(f"Hora de salida: {registro[4]}")
                    print(f"Nombre: {registro[3]}")
                    print(f"Número minutos: {registro[5]}")
                    print(f"Total: {registro[6]}")
                else:
                    print("Formato de hora incorrecto.")
            return
    print("La placa ingresada no está registrada en el sistema.")

def calcular_minutos(hora_ingreso, hora_salida):
    hh_ingreso = int(hora_ingreso[:2])
    mm_ingreso = int(hora_ingreso[2:])
    hh_salida = int(hora_salida[:2])
    mm_salida = int(hora_salida[2:])
    minutos_ingreso = hh_ingreso * 60 + mm_ingreso
    minutos_salida = hh_salida * 60 + mm_salida
    minutos = minutos_salida - minutos_ingreso
    if minutos < 0:
        minutos += 24 * 60  # Ajustar para cálculos de tiempo que cruzan la medianoche
    return minutos

def buscar_factura(vehiculos):
    factura = int(input("Ingrese el número de la factura: "))
    for registro in vehiculos:
        if registro[0] == factura:
            print("Factura encontrada:")
            print(f"Factura N: {registro[0]}")
            print(f"Placa: {registro[1]}")
            print(f"Hora de ingreso: {registro[2]}")
            print(f"Hora de salida: {registro[4]}")
            print(f"Nombre: {registro[3]}")
            print(f"Número minutos: {registro[5]}")
            print(f"Total: {registro[6]}")
            return
    print("Factura no encontrada.")

def cuadre_caja():
    total_automoviles = sum([vehiculo[6] for vehiculo in registros_automoviles if vehiculo[4] != ''])
    total_motocicletas = sum([vehiculo[6] for vehiculo in registros_motocicletas if vehiculo[4] != ''])
    print(f"\nTotal ingresos automóviles: {total_automoviles}")
    print(f"Total ingresos motocicletas: {total_motocicletas}")
    print(f"Total general: {total_automoviles + total_motocicletas}")

# Iniciar el programa
menu()
