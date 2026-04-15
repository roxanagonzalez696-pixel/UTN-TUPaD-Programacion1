
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
cantidad_de_chances = 0

#PUNTO 1 
nombre_agente = input("Ingresar el nombre del agente: ").strip().upper()       #INGRESO DE NOMBRE DEL AGENTE

while nombre_agente== "" or not nombre_agente.isalpha():                   
    print(" Error, en el nombre guardado")
    nombre_agente = input("Ingresar nuevamente el nombre del agente: ").strip().upper()

#Permanencia del juego
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:
    print(f" {nombre_agente} ESTAMOS EN EL JUEGO!!! ")
    print(f"ENERGIA: {energia} -- TIEMPO: {tiempo} -- CERRADURAS ABIERTAS: {cerraduras_abiertas}")
    

    accion = input(" Ingresar acción 1-FORZAR CERRADURA, 2-HACKEAR PANEL, 3-DESCANSAR:  ").strip()
    print(f" Opción elegida: {accion}")

    while not accion.isdigit() or not (1<= int(accion) <=3):
        print("Error, ingresar un valor correcto: ") 
        accion = input(" Ingresar acción 1-FORZAR CERRADURA, 2-HACKEAR PANEL, 3-DESCANSAR:  ").strip()
    accion_int = int(accion)

    
    if accion_int == 1:
        print("Acción 1 = FORZAR CERRADURA- Costo: energía= -20 ptos, tiempo= -2")
        energia -= 20
        tiempo -= 2
        cantidad_de_chances +=1 
        
        if cantidad_de_chances == 3:                #REGLA ANTI-SPAM
            alarma = True
            print(" CERRADURA TRABADA! ALARMA ACTIVADA! - Superaste la cantidad de intentos!")
        else:
            if energia < 40:                        #RIESO DE ALARMA
                print("RIESGO DE ALARMA - Solcitar número de rescate")
                numero_escape = input(" Ingrese un número de escape entre 1 y 3").strip()

                while not numero_escape.isdigit() or not (1<= int(numero_escape) <=3):
                    print(" Error en el valor ingresado ")
                    numero_escape = input(" Ingrese un nuevo número de escape entre 1 y 3").strip()
                numero_escape_int = int(numero_escape)

                if numero_escape_int == 3:          #ACTIVACIÓN DE ALARMA          
                    alarma = True
                    print(" ALARMA ACTIVADA!!!")

            if not alarma:
                cerraduras_abiertas +=1
                print(f" CERRADURA ABIERTA NRO: {cerraduras_abiertas} !! ")
        print()

    elif accion_int == 2:
        print("Acción 2 = HACKEAR PANEL: Costo: energía= -10ptos, tiempo= -3ptos ")
        energia -= 10 
        tiempo -= 3
        for i in range(1, 5):
            codigo_parcial += "A"
            
        if len(codigo_parcial) >= 8:
            cerraduras_abiertas +=1 
            print(f"CERRADURA {cerraduras_abiertas} ABIERTA!! CODIGO COMPLETO!!")
            codigo_parcial = ""
            
        print(f"Estado del agente {nombre_agente} ")
        print(f"ENERGIA: {energia} -- TIEMPO: {tiempo} -- CERRADURAS ABIERTAS: {cerraduras_abiertas}")
        print()

    elif accion_int == 3:
        print("Acción 3 = DESCANSAR - Costo: energía= +15ptos, tiempo= -1, ")
        energia +=15
        tiempo -=1
        if alarma:
            energia -=10

        print(f"Estado del agente {nombre_agente} ")
        print(f"ENERGIA: {energia} -- TIEMPO: {tiempo} -- CERRADURAS ABIERTAS: {cerraduras_abiertas}")
        print()
    

print("CONDICIÓN FINAL DEL JUEGO")
if cerraduras_abiertas == 3:
    print(f"VICTORIA!! Agente {nombre_agente} has ganado el juego! Has abierto la bóveda!!")
    print(f"ENERGIA: {energia} -- TIEMPO: {tiempo} -- CERRADURAS ABIERTAS: {cerraduras_abiertas}")
elif energia <= 0:
    print(f" DERROTA!! Agente {nombre_agente} has perdido el juego!! Te has quedado sin energía!")
    print(f"ENERGIA: {energia} -- TIEMPO: {tiempo} -- CERRADURAS ABIERTAS: {cerraduras_abiertas}")
elif tiempo <= 0:
    print (f" DERROTA!! Agente {nombre_agente} has perdido el juego!! Te has quedado sin tiempo!")
    print(f"ENERGIA: {energia} -- TIEMPO: {tiempo} -- CERRADURAS ABIERTAS: {cerraduras_abiertas}")
elif alarma == True and tiempo <= 3:                #BLOQUEO POR ALARMA               
    print(f"  DERROTA POR BLOQUEO ")
    print(f"ENERGIA: {energia} -- TIEMPO: {tiempo} -- CERRADURAS ABIERTAS: {cerraduras_abiertas}")
else:
    print(f"AGENTE {nombre_agente} FUERA DE JUEGO!!!")