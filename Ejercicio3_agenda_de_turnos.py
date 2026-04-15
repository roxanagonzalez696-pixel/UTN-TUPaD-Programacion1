#variables
CIERRE_SISTEMA = 5
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
cantidad_turnos_lunes = 0
cantidad_turnos_libres_lunes = 4

martes1 = ""
martes2 = ""
martes3 = ""
cantidad_turnos_martes = 0
cantidad_turnos_libres_martes = 3

#PUNTO 1.
print ("PUNTO 1: Pedir nombre del operador (solo letras).")

operador = input(" Ingresar nombre Operador: ").strip().upper()                  #INGRESO DEL OPERARDOR
while operador ==" " or not operador.isalpha(): #Valida que el nombre ingresado no sea espacio en blanco ni tenga números o símbolos
    print("Error. Se debe ingresar un nombre sin número, ni espacios, ni símbolos!  ")
    operador = input("Ingresar nuevo nombre del Operador: ").strip().upper()
print(" Nombre Operador: ", operador)
print("----------------")


print("PUNTO 2: Menú repetitivo hasta salir ")                                   #PUNTO 2 - MENÚ PRINCIPAL

opcion = input("Ingresar 1-Reservar Turno, 2-Cancelar turno, 3-Ver agenda, 4- Resumen, 5-Cerrar Sistema:  ").strip()

while not opcion.isdigit():             # Valida que sea entero 
    opcion = input(" Error. Ingresar un nro válido entre 1 y 4 - 5 Para salir del Sitema: ").strip()
opcion_int = int(opcion)

while opcion_int != CIERRE_SISTEMA:
    if opcion_int == 1:
        print(" Opción 1: Agendar turno ") 
        print("PUNTO 3: Elección de día-Ingreso de paciente-Agenda de turno")    #Punto3 - RESERVA DE TURNO

        dia = input(" Ingresar el día de atención, 1-LUNES, 2-MARTES: ").strip() #INGRESO DEL DIA DE ATENCION
        while not dia.isdigit() or int(dia)<1 or int(dia)>2:
            print(" Error en el valor ingresado")
            dia = input(" Ingresar nuevamente, 1-LUNES, 2-MARTES: ")
        dia_int = int(dia)

        nombre_paciente = input("Ingresar nombre del paciente: ").strip().title()#INGRESO DE PACIENTE
        while nombre_paciente == "" or not nombre_paciente.isalpha():
            print(" Error. El nombre solo debe contener solo letras")
            nombre_paciente = input("Ingresar nuevamente nombre del paciente: ").strip().title()

        if dia_int == 1:
            print(" ESTAMOS EN EL TURNERO DEL DÍA LUNES ")
            if nombre_paciente == lunes1 or nombre_paciente == lunes2 or nombre_paciente == lunes3 or nombre_paciente == lunes4:
                print(f" El paciente {nombre_paciente} ya tiene turno asignado este día")
                print()
            else:
                if lunes1 == "":
                    lunes1 = nombre_paciente
                    cantidad_turnos_lunes +=1
                    cantidad_turnos_libres_lunes -=1
                    print(f" Datos turno - día LUNES 1er turno: {nombre_paciente}")
                    print()
                elif lunes2 == "":
                    lunes2 = nombre_paciente
                    cantidad_turnos_lunes +=1
                    cantidad_turnos_libres_lunes -=1
                    print(f" Datos turno - día LUNES 2do turno: {nombre_paciente}")
                    print()
                elif lunes3 == "":
                    lunes3 = nombre_paciente
                    cantidad_turnos_lunes +=1
                    cantidad_turnos_libres_lunes -=1
                    print(f" Datos turno - día LUNES 3er turno: {nombre_paciente}")
                    print()
                elif lunes4 == "":
                    lunes4 = nombre_paciente
                    cantidad_turnos_lunes +=1
                    cantidad_turnos_libres_lunes -=1
                    print(f" Datos turno - día LUNES 4to turno: {nombre_paciente}")
                    print()
                else:
                    print(" No hay turnos disponibles para el día Lunes")
                    print()
        elif dia_int == 2:
            print(" ESTAMOS EN EL TURNERO DEL DÍA MARTES ")
            if nombre_paciente == martes1 or nombre_paciente == martes1 or nombre_paciente == martes3:
                print(f" El paciente {nombre_paciente} ya tiene turno asignado este día")
            else:
                if martes1 == "":
                    martes1 = nombre_paciente
                    cantidad_turnos_martes += 1 
                    cantidad_turnos_libres_martes -=1
                    print(f" Datos turno - día MARTES 1er turno: {nombre_paciente}")
                    print()
                elif martes2 == "":
                    martes2 = nombre_paciente
                    cantidad_turnos_martes += 1
                    cantidad_turnos_libres_martes -=1 
                    print(f" Datos turno - día MARTES 2do turno: {nombre_paciente}")
                    print()
                elif martes3 == "":
                    martes3 = nombre_paciente
                    cantidad_turnos_martes += 1 
                    cantidad_turnos_libres_martes -=1
                    print(f" Datos turno - día MARTES 3er turno: {nombre_paciente}")
                    print()
                else:
                    print(" No hay turnos disponibles para el día Martes")
                    print()
        else:
            print(" Opción día no valido")
            print()

    elif opcion_int == 2:
        print(" Opción 2: Cancelar turno por nombre")
        print("PUNTO 4: Cancelación de turno - Pedir día, paciente. Anular")     #PUNTO 4 - ANNULACIÓN DE TURNO

        dia = input(" Ingresar día de turno a cancelar, 1-LUNES, 2-MARTES: ").strip()
        while not dia.isdigit() or int(dia)<1 or int(dia)>2:
            print(" Error en el valor ingresado")
            dia = input(" Ingresar nuevamente, 1-LUNES, 2-MARTES: ")
        dia_int = int(dia)

        nombre_paciente = input("Ingresar nombre del paciente: ").strip().title()#INGRESO DE PACIENTE
        while nombre_paciente == "" or not nombre_paciente.isalpha():
            print(" Error. El nombre solo debe contener solo letras")
            nombre_paciente = input("Ingresar nuevamente nombre del paciente: ").strip().title()

        if dia_int == 1:
            print(" ESTAMOS EN EL TURNERO DEL DÍA LUNES ")
            if nombre_paciente == lunes1 or nombre_paciente == lunes2 or nombre_paciente == lunes3 or nombre_paciente == lunes4:
                print(f" El paciente {nombre_paciente} tiene turno asignado este día")
                print()

                if nombre_paciente == lunes1:
                    lunes1 == " "
                    cantidad_turnos_libres_lunes +=1
                    print(" TURNO CANCELADO!! ")
                    print()
                elif nombre_paciente == lunes2:
                    lunes2 == " "
                    cantidad_turnos_libres_lunes +=1
                    print(" TURNO CANCELADO!! ") 
                    print()
                elif nombre_paciente == lunes3:
                    lunes3 == " "
                    cantidad_turnos_libres_lunes +=1
                    cantidad_turnos_libres_lunes +=1
                    print(" TURNO CANCELADO!! ")
                    print()
                elif nombre_paciente == lunes4:
                    lunes4 == " "
                    cantidad_turnos_libres_lunes +=1
                    print(" TURNO CANCELADO!! ")
                    print()
            else:
                print(f"El/La paciente {nombre_paciente} no tiene turno para cancelar el día LUNES ")
                print()

        elif dia_int == 2:
            print(" ESTAMOS EN EL TURNERO DEL DÍA MARTES ")
            if nombre_paciente == martes1 or nombre_paciente == martes1 or nombre_paciente == martes3:
                print(f" El paciente {nombre_paciente} tiene turno asignado este día")

                if nombre_paciente == martes1:
                    martes1 == " "
                    cantidad_turnos_libres_martes +=1
                    print(" TURNO CANCELADO!! ")
                    print()
                elif nombre_paciente == martes2:
                    martes2 == " "
                    cantidad_turnos_libres_martes +=1
                    print(" TURNO CANCELADO!! ") 
                    print()
                elif nombre_paciente == martes3:
                    martes3 == " "
                    cantidad_turnos_libres_martes +=1
                    print(" TURNO CANCELADO!! ")
                    print()
            else:
                print(f"El/La paciente {nombre_paciente} no tiene turno para cancelar el día MARTES ")
                print()
        else:
            print(" Opción día no valido")
            print()

    elif opcion_int == 3:
        print(" PUNTO 5 - Mostrar turnos del día ")                              #PUNTO 5 - AGENDA DEL DÍA

        dia = input(" Ingresar el día de atención, 1-LUNES, 2-MARTES: ").strip() #INGRESO DEL DIA DE ATENCION
        while not dia.isdigit() or int(dia)<1 or int(dia)>2:
            print(" Error en el valor ingresado")
            dia = input(" Ingresar nuevamente, 1-LUNES, 2-MARTES: ")
        dia_int = int(dia)

        if dia_int == 1:
            print(" ESTAMOS EN EL TURNERO DEL DÍA LUNES ")
            if lunes1 == "":
                print(" Turno 1: (LIBRE)")
            else:
                print(f" Turno 1: {lunes1}")

            if lunes2 == "":
                print(" Turno 2: (LIBRE)")
            else:
                print(f" Turno 2: {lunes2}")

            if lunes3 == "":
                print(" Turno 3: (LIBRE)")
            else:
                print(f" Turno 3: {lunes3}")

            if lunes4 == "":
                print(" Turno 4: (LIBRE)")
            else:
                print(f" Turno 4: {lunes4}")

        elif dia_int == 2:
            print(" ESTAMOS EN EL TURNERO DEL DÍA MARTES ")
            if martes1 == "":
                print(" Turno 1: (LIBRE)")
            else:
                print(f" Turno 1: {martes1}")

            if martes2 == "":
                print(" Turno 2: (LIBRE)")
            else:
                print(f" Turno 2: {martes2}")
            
            if martes3 == "":
                print(" Turno 3: (LIBRE)")
            else:
                print(f" Turno 3: {martes3}")

    elif opcion_int == 4:                                                        #PUNTO 6: RESUMEN DE TURNOS - TOTALES 
        print(" Opción 4: Resumen de turnos")
        print(" Total de turnos por día ")
        print(" Turnos dia Lunes ")
        print(f" Turnos ocupados el día Lunes: {cantidad_turnos_lunes} ")
        print(f" Turnos libres día Lunes: {cantidad_turnos_libres_lunes}")
        print( )
        print(" Turnos dia Martes ")
        print(f" Turnos ocupados el día Martes: {cantidad_turnos_martes} ")
        print(f" Turnos libres día Martes: {cantidad_turnos_libres_martes}")
        print( )
        print(" Día con más turnos")
        if cantidad_turnos_lunes == cantidad_turnos_martes:
            print(f"Ambos días tiene misma cantidad de turnos: {cantidad_turnos_lunes}")
        elif cantidad_turnos_lunes > cantidad_turnos_martes:
            print(f"Día lunes cuenta con más turnos: {cantidad_turnos_lunes}")
        else:
            print(f"Día Martes cuenta con más turnos: {cantidad_turnos_martes}")
        print()
    else:
        print(" Opción del menú no valida ")
        print()

    print(" --MENÚ PRINCIPAL--  ")                                 #RETROALIMENTACION WHILE DEL MENÚ PRINCIPAL
    opcion = input(" Reingreso al menú. Ingresar 1-Reservar Turno, 2-Cancelar turno, 3-Ver agenda, 4- Resumen, 5-Cerrar Sistema: ").strip() 
    while not opcion.isdigit():
        opcion = input(" Error. Ingresar un nro valido: ")
    opcion_int = int(opcion)
    print()
print(" --- CIERRE DE SESIÓN ---")






    

