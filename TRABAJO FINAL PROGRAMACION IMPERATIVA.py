# Variables globales para almacenar las tarifas y registros
tarifa_general = [0, 0]  # Lista que contiene las tarifas por minuto para automóviles y motocicletas
registros_automoviles = []  # Lista para registrar los automóviles
registros_motocicletas = []  # Lista para registrar las motocicletas
vehiculos = []  # Lista combinada para registrar todos los vehículos

def menu():
    """
    Función que muestra el menú principal y maneja la selección de opciones.
    """
    opc = 1  # Inicializa la opción del menú
    while opc > 0 and opc < 8:  # Mantiene el menú activo mientras la opción sea válida
        print(" 1. Tarifas")
        print(" 2. Ingresar vehículo")
        print(" 3. Buscar vehículo")
        print(" 4. Mostrar registros")
        print(" 5. Salida de vehículo")
        print(" 6. Buscar factura")
        print(" 7. Cuadre de caja")
        print(" 8. Salir")

        opc = int(input("\n\tDigite una opción: "))  # Solicita al usuario seleccionar una opción

        # Ejecuta la función correspondiente a la opción seleccionada
        if opc == 1:
            menu_tarifas()
        elif opc == 2:
            factura = 1
            ingresar_vehiculo(factura)
        elif opc == 3:
            buscar_vehiculos()
        elif opc == 4:
            mostrar_registros()
        elif opc == 5:
            salida_vehiculos()
        elif opc == 6:
            buscar_factura(vehiculos)
        elif opc == 7:
            cuadre_caja()
        else:
            print("Ingrese una opción válida \n")
            menu()  # Reinicia el menú si la opción no es válida

def menu_tarifas():
    opc = 1  # Inicializa la opción del submenú de tarifas
    while opc > 0 and opc < 5:  # Mantiene el submenú activo mientras la opción sea válida
        print(" 1. Ingresar tarifas")
        print(" 2. Mostrar tarifas")
        print(" 3. Modificar tarifas")
        print(" 4. Regresar al menú principal")

        opc = int(input("\n\tDigite una opción: "))  # Solicita al usuario seleccionar una opción

        # Ejecuta la función correspondiente a la opción seleccionada
        if opc == 1:
            ingresar_tarifas()
        elif opc == 2:
            print('Valor por minuto auto:', tarifa_general[0])
            print('Valor por minuto moto:', tarifa_general[1])
        elif opc == 3:
            modificar_tarifas()
        elif opc == 4:
            menu()  # Regresa al menú principal
        else:
            print("Ingrese una opción válida \n")
            menu_tarifas()  # Reinicia el submenú si la opción no es válida

def ingresar_tarifas():
    opc = 1  # Inicializa la opción del submenú para ingresar tarifas
    while opc > 0 and opc < 4:  # Mantiene el submenú activo mientras la opción sea válida
        print(" 1. Ingresar tarifa de automóvil")
        print(" 2. Ingresar tarifa de motocicleta")
        print(" 3. Regresar al subMenú Tarifas")

        opc = int(input("\n\tDigite una opción: "))  # Solicita al usuario seleccionar una opción

        # Ejecuta la acción correspondiente a la opción seleccionada
        if opc == 1:
            tarifa_auto = int(input('Ingresa el valor a cobrar por minuto para automóviles: '))
            tarifa_general[0] = tarifa_auto
        elif opc == 2:
            tarifa_moto = int(input('Ingresa el valor a cobrar por minuto para motocicletas: '))
            tarifa_general[1] = tarifa_moto
        elif opc == 3:
            menu_tarifas()  # Regresa al submenú de tarifas
        else:
            print("Ingrese una opción válida \n")
            ingresar_tarifas()  # Reinicia el submenú si la opción no es válida

def modificar_tarifas():
    opc = 1  # Inicializa la opción del submenú para modificar tarifas
    while opc > 0 and opc < 4:  # Mantiene el submenú activo mientras la opción sea válida
        print('1. Modificar tarifa de automóvil.')
        print('2. Modificar tarifa de motocicleta.')
        print('3. Regresar al submenú tarifas.')

        opc = int(input('\n\tDigite una opción: '))  # Solicita al usuario seleccionar una opción

        # Ejecuta la acción correspondiente a la opción seleccionada
        if opc == 1:
            tarifa_auto = int(input('Ingresa el nuevo valor a cobrar por minuto para automóviles: '))
            tarifa_general[0] = tarifa_auto
        elif opc == 2:
            tarifa_moto = int(input('Ingresa el nuevo valor a cobrar por minuto para motocicletas: '))
            tarifa_general[1] = tarifa_moto
        elif opc == 3:
            menu_tarifas()  # Regresa al submenú de tarifas
        else:
            print("Ingrese una opción válida \n")
            modificar_tarifas()  # Reinicia el submenú si la opción no es válida

def ingresar_vehiculo(factura):
    tipo_vehiculo = input("Tipo de vehículo (a: automóvil, m: motocicleta): ")
    if tipo_vehiculo != 'a' and tipo_vehiculo != 'm':  # Verifica si el tipo de vehículo es válido
        print("Tipo de vehículo no válido.")
        return
    
    placa = input("Número de la placa: ")
    if len(placa) != 6:  # Verifica si la placa tiene el formato correcto
        print("Placa no válida. Debe ser del formato 'ABC123' o 'ABC15G'.")
        return
    
    # Verifica si la placa ya está registrada en automóviles o motocicletas
    for registro in vehiculos:
        if registro[1] == placa:
            print("La placa ya está registrada")
            return
    
    hora = int(input("Hora (formato de 24 horas - hhmm): "))
    if len(str(hora)) == 4:  # Verifica si la hora tiene el formato correcto
        hh_ingreso = hora // 100 
        mm_ingreso = hora % 100
        if (hh_ingreso < 0 or hh_ingreso > 23) or (mm_ingreso < 0 or mm_ingreso > 59):
            print("Hora no válida.")
            return
    else: 
        print("Hora no válida.")
        return
    
    nombre_cliente = input("Nombre del cliente: ")
    
    # Registra el vehículo según su tipo
    if tipo_vehiculo == 'a':
        registro_automovil = [factura, placa, hora, nombre_cliente, '', 0, 0, tipo_vehiculo]
        registros_automoviles.append(registro_automovil)
        vehiculos.append(registro_automovil)
    elif tipo_vehiculo == 'm':
        registro_motocicleta = [factura, placa, hora, nombre_cliente, '', 0, 0, tipo_vehiculo]
        registros_motocicletas.append(registro_motocicleta)
        vehiculos.append(registro_motocicleta)

def buscar_vehiculos():
    opc = 1  # Inicializa la opción del submenú para buscar vehículos
    while opc > 0 and opc < 4:  # Mantiene el submenú activo mientras la opción sea válida
        print('1. Buscar motocicletas.')
        print('2. Buscar automóviles.')
        print('3. Regresar al menú principal')

        opc = int(input('\n\tDigite una opción: '))  # Solicita al usuario seleccionar una opción

        # Ejecuta la acción correspondiente a la opción seleccionada
        if opc == 1:
            buscar_moto()
        elif opc == 2:
            buscar_auto()
        elif opc == 3:
            menu()  # Regresa al menú principal
        else:
            print("Ingrese una opción válida \n")
            buscar_vehiculos()  # Reinicia el submenú si la opción no es válida

def buscar_moto():
    """
    Función que busca una motocicleta en los registros.
    """
    placa = input("Ingresa la placa de la motocicleta: ")  # Solicita al usuario ingresar la placa de la motocicleta a buscar
    for registro in registros_motocicletas:  # Itera sobre los registros de motocicletas para buscar la placa ingresada
        if registro[1] == placa:  # Comprueba si la placa del registro coincide con la placa ingresada
            print('Factura N:', registro[0])  # Imprime el número de factura del registro
            print("Placa:", registro[1])  # Imprime la placa del registro
            print("Hora de ingreso:", registro[2])  # Imprime la hora de ingreso del registro
            print("Hora de salida:", registro[4])  # Imprime la hora de salida del registro
            print("Nombre:", registro[3])  # Imprime el nombre del cliente del registro
            print("Número minutos:", registro[5])  # Imprime el número de minutos del registro
            print("Total:", registro[6])  # Imprime el total a pagar del registro
            return  # Sale de la función después de encontrar el registro
    print('La placa ingresada no está registrada en el sistema.')  # Imprime un mensaje si la placa no está registrada

def buscar_auto():
    """
    Función que busca un automóvil en los registros.
    """
    placa = input("Ingresa la placa del automóvil: ")  # Solicita la placa del automóvil a buscar
    for registro in registros_automoviles:  # Recorre los registros de automóviles para buscar la placa
        if registro[1] == placa:  # Comprueba si la placa coincide con un registro de automóvil
            print('Factura N:', registro[0])  # Muestra el número de factura
            print("Placa:", registro[1])  # Muestra la placa del automóvil
            print("Hora de ingreso:", registro[2])  # Muestra la hora de ingreso del automóvil
            print("Hora de salida:", registro[4])  # Muestra la hora de salida del automóvil
            print("Nombre:", registro[3])  # Muestra el nombre del cliente
            print("Número minutos:", registro[5])  # Muestra el número de minutos estacionado
            print("Total:", registro[6])  # Muestra el total a pagar
            return  # Sale de la función después de mostrar la información
    print('La placa ingresada no está registrada en el sistema.')  # Mensaje si la placa no está registrada

def mostrar_registros():
    opc = 1
    while opc > 0 and opc < 4:
        print('1. Mostrar todos los automóviles.')
        print('2. Mostrar todas las motocicletas.')
        print('3. Regresar al menú principal')

        opc = int(input('\n\tDigite una opción: '))  # Solicita al usuario seleccionar una opción

        # Ejecuta la acción correspondiente a la opción seleccionada
        if opc == 1:
            print('Tipo de búsqueda: AUTOMÓVILES.')
            mostrara()  # Llama a la función mostrara() para mostrar todos los automóviles
        elif opc == 2:
            print('Tipo de búsqueda: MOTOCICLETAS.')
            mostrarm()  # Llama a la función mostrarm() para mostrar todas las motocicletas
        elif opc == 3:
            menu()  # Regresa al menú principal
        else: 
            mostrar_registros()  # Reinicia la función si la opción no es válida

def mostrara():
    """
    Función que muestra todos los registros de automóviles.
    """
    n = len(registros_automoviles)  # Obtiene la cantidad de registros de automóviles
    print("FACTURA PLACA INGRESO NOMBRE SALIDA MINUTOS TOTAL")  # Encabezado para mostrar la información
    for i in range(n):  # Recorre cada registro de automóvil
        for j in range(7):  # Recorre cada elemento en el registro
            print(registros_automoviles[i][j], end="   ")  # Muestra el elemento y agrega espacio
        print()  # Salta a una nueva línea después de mostrar todos los elementos de un registro

def mostrarm():
    """
    Función que muestra todos los registros de motocicletas.
    """
    n = len(registros_motocicletas)  # Obtiene la cantidad de registros de motocicletas
    print("FACTURA PLACA INGRESO NOMBRE SALIDA MINUTOS TOTAL")  # Encabezado para mostrar la información
    for i in range(n):  # Recorre cada registro de motocicleta
        for j in range(7):  # Recorre cada elemento en el registro
            print(registros_motocicletas[i][j], end="   ")  # Muestra el elemento y agrega espacio
        print()  # Salta a una nueva línea después de mostrar todos los elementos de un registro

def salida_vehiculos():
    tipo_vehiculo = input('Ingresa el tipo de vehículo: ')  # Solicita al usuario el tipo de vehículo (automóvil o motocicleta)
    if tipo_vehiculo == 'a':
        salida_automovil()  # Llama a la función salida_automovil() si el tipo de vehículo es automóvil
    elif tipo_vehiculo == 'm':
        salida_motocicleta()  # Llama a la función salida_motocicleta() si el tipo de vehículo es motocicleta
    else:
        print("Tipo de vehículo no válido.")
        salida_vehiculos()  # Reinicia la función si el tipo de vehículo no es válido

def salida_automovil():
    placa = input("Placa del automóvil: ")  # Solicita al usuario ingresar la placa del automóvil que desea registrar la salida
    for registro in registros_automoviles:  # Itera sobre los registros de automóviles para buscar la placa ingresada
        if registro[1] == placa:  # Comprueba si la placa coincide con algún registro de automóvil
            if registro[4]:  # Verifica si el automóvil ya ha registrado la salida
                print("El vehículo ya ha registrado la salida.")
            else:
                hora_2 = input("Hora de salida (formato de 24 horas - hhmm): ")  # Solicita la hora de salida al usuario
                if len(str(hora_2)) == 4:  # Verifica si la hora de salida tiene el formato correcto
                    hh_salida = hora_2 // 100  # Obtiene la hora de salida en formato HH
                    mm_salida = hora_2 % 100  # Obtiene los minutos de salida en formato MM
                    if (hh_salida >= 0 and hh_salida <= 23) and (mm_salida >= 0 and mm_salida <= 59):  # Verifica si la hora es válida
                        registro[4] = hora_2  # Registra la hora de salida en el registro del automóvil
                        minutos = calcular_minutos(registro[2], hora_2)  # Calcula los minutos de estadía del automóvil
                        total_pagar = minutos * tarifa_general[0]  # Calcula el total a pagar por la estadía del automóvil
                        registro[5] = minutos  # Registra los minutos de estadía en el registro del automóvil
                        registro[6] = total_pagar  # Registra el total a pagar en el registro del automóvil
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
                else:
                    print("Hora no válida.")
            return
    print("La placa ingresada no está registrada en el sistema.")  # Mensaje si la placa no está registrada en los automóviles

def salida_motocicleta():
    placa = input("Placa de la motocicleta: ")  # Solicita al usuario ingresar la placa de la motocicleta que desea registrar la salida
    for registro in registros_motocicletas:  # Itera sobre los registros de motocicletas para buscar la placa ingresada
        if registro[1] == placa:  # Comprueba si la placa coincide con algún registro de motocicleta
            if registro[4]:  # Verifica si la motocicleta ya ha registrado la salida
                print("El vehículo ya ha registrado la salida.")
            else:
                hora_2 = input("Hora de salida (formato de 24 horas - hhmm): ")  # Solicita la hora de salida al usuario
                if len(str(hora_2)) == 4:  # Verifica si la hora de salida tiene el formato correcto
                    hh_salida = hora_2 // 100  # Obtiene la hora de salida en formato HH
                    mm_salida = hora_2 % 100  # Obtiene los minutos de salida en formato MM
                    if (hh_salida >= 0 and hh_salida <= 23) and (mm_salida >= 0 and mm_salida <= 59):  # Verifica si la hora es válida
                        registro[4] = hora_2  # Registra la hora de salida en el registro de la motocicleta
                        minutos = calcular_minutos(registro[2], hora_2)  # Calcula los minutos de estadía de la motocicleta
                        total_pagar = minutos * tarifa_general[1]  # Calcula el total a pagar por la estadía de la motocicleta
                        registro[5] = minutos  # Registra los minutos de estadía en el registro de la motocicleta
                        registro[6] = total_pagar  # Registra el total a pagar en el registro de la motocicleta
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
                else:
                    print("Hora no válida.")
            return
    print("La placa ingresada no está registrada en el sistema.")  # Mensaje si la placa no está registrada en las motocicletas

def calcular_minutos(hora_ingreso, hora_2):
    hh_ingreso = hora_ingreso // 100  # Obtiene la hora de ingreso en formato HH
    mm_ingreso = hora_ingreso % 100  # Obtiene los minutos de ingreso en formato MM
    hh_salida = hora_2 // 100  # Obtiene la hora de salida en formato HH
    mm_salida = hora_2 % 100  # Obtiene los minutos de salida en formato MM
    minutos_ingreso = hh_ingreso * 60 + mm_ingreso  # Convierte la hora de ingreso a minutos
    minutos_salida = hh_salida * 60 + mm_salida  # Convierte la hora de salida a minutos
    minutos = minutos_salida - minutos_ingreso  # Calcula la diferencia de minutos entre la salida y el ingreso
    if minutos < 0:  # Verifica si la diferencia es negativa (cuando la salida es antes de la entrada del día siguiente)
        minutos = minutos + (24 * 60)  # Ajusta los minutos sumando la cantidad de minutos en un día (24 horas * 60 minutos)
    return minutos  # Devuelve el total de minutos de estadía del vehículo

def buscar_factura(vehiculos):
    factura = int(input("Ingrese el número de la factura: "))  # Solicita al usuario el número de factura a buscar
    for registro in vehiculos:  # Recorre la lista de vehículos para buscar la factura
        if registro[0] == factura:  # Compara el número de factura en el registro actual con el buscado
            print("Factura encontrada:")  # Muestra un mensaje indicando que se encontró la factura
            print(f"Factura N: {registro[0]}")  # Imprime el número de factura del registro
            print(f"Placa: {registro[1]}")  # Imprime la placa del vehículo registrado en la factura
            print(f"Hora de ingreso: {registro[2]}")  # Imprime la hora de ingreso del vehículo
            print(f"Hora de salida: {registro[4]}")  # Imprime la hora de salida del vehículo
            print(f"Nombre: {registro[3]}")  # Imprime el nombre del cliente
            print(f"Número minutos: {registro[5]}")  # Imprime el número de minutos que estuvo el vehículo
            print(f"Total: {registro[6]}")  # Imprime el total a pagar por el servicio
            return  # Termina la función después de encontrar la factura
    print("Factura no encontrada.")  # Imprime un mensaje si la factura no se encuentra en los registros

def cuadre_caja():
    total_automoviles = 0  # Inicializa el total de ingresos por automóviles
    for vehiculo in registros_automoviles:  # Recorre la lista de registros de automóviles
        if vehiculo[4] != '':  # Verifica si el vehículo tiene registrada la hora de salida
            total_automoviles += vehiculo[6]  # Suma el total a pagar del vehículo al total de ingresos por automóviles

    total_motocicletas = 0  # Inicializa el total de ingresos por motocicletas
    for vehiculo in registros_motocicletas:  # Recorre la lista de registros de motocicletas
        if vehiculo[4] != '':  # Verifica si el vehículo tiene registrada la hora de salida
            total_motocicletas += vehiculo[6]  # Suma el total a pagar del vehículo al total de ingresos por motocicletas

    print("\nTotal ingresos automóviles:", total_automoviles)  # Imprime el total de ingresos por automóviles
    print("Total ingresos motocicletas:", total_motocicletas)  # Imprime el total de ingresos por motocicletas
    print("Total general:", total_automoviles + total_motocicletas)  # Imprime el total general sumando los ingresos de automóviles y motocicletas

# Llama a la función menu() para iniciar el programa
menu()
