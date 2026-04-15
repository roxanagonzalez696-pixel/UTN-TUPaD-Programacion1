
vida_del_gladiador = 100                                                       #PASO 2 - Inicialización de variables
vida_del_enemigo = 100
pociones_de_vida = 3
daño_base_ataque_pesado = 15
daño_base_del_enemigo = 12
turno_gladiador = True
daño_golpe = 0.0

print(" ------------BIENVENIDO A LA ARENA------------")
nombre_gladiador = input("Ingresar el nombre del Gladiador: ").strip().title() # PASO 1 - INGRESO NOMBRE DEL GLADIADOR
                 
while nombre_gladiador == "" or not nombre_gladiador.isalpha():
    print("Error! Solo se permiten letras")
    nombre_gladiador = input("Ingresar nombre sin números ni espacios: ").strip().title()
    print(f" Nombre del Gladiador: {nombre_gladiador}")

print("CICLO DE COMBATE - mientras ambos jugadores tengan más de 0 ptos de vida")
while  vida_del_gladiador >0 and vida_del_enemigo >0:                          #VERIFICA QUE AMBOS COMBATIENTES TENGAN VIDA
    print("============INICIO DEL COMBATE============")

    print(f" {nombre_gladiador} (HP: {vida_del_gladiador}) vs Enemigo: (HP: {vida_del_enemigo}) | POCIONES: {pociones_de_vida}")

    print(" Elige acción")
    print("1. Ataque Pesado")
    print("2. Ráfaga veloz")
    print("3. Curar")

    opcion = input("Elegir una acción 1-ATAQUE PESADO, 2- RÁFAGA VELOZ, 3-CURAR: ").strip()
    while not opcion.isdigit() or not (1<= int(opcion) <=3):                                                      #VALIDA QUE SEA ENTERO
        print("Error en el valor ingresado")
        opcion = input("Elegir nuevamente una acción 1-ATAQUE PESADO, 2- RÁFAGA VELOZ, 3-CURAR: ").strip() 
    opcion_int = int(opcion)
    print(f" Acción elegida: {opcion_int}")

    if opcion_int == 1:
        print(" Acción 1: ATAQUE PESADO")
        if vida_del_enemigo <20:
            daño_golpe = daño_base_ataque_pesado * 1.5
            vida_del_enemigo -= daño_golpe
        print(f" Ataque al enemigo por {daño_golpe:.2f} puntos de daño ")
        print()

    elif opcion_int == 2:
        print(" Acción : RÁFAGA VELOZ")
        for i in range(1,4):
            vida_del_enemigo -= 5
            print("Golpe conectado por 5 de daño")
            print()

    elif opcion_int == 3:
        print(" Acción 3: CURAR")
        if pociones_de_vida > 0:
            vida_del_gladiador += 30
            pociones_de_vida -= 1
            print(" Has recuperado 30 ptos de vida, pero has perdido una poción! ")
            
        else:
            print("No quedan pociones!!!")
            #TURNO DEL ENEMIGO! 
            vida_del_gladiador -= daño_base_del_enemigo
            print("El enemigo te atacó por 12 ptos de daño!")
            print() 

# FIN DEL JUEGO
if vida_del_gladiador > 0:
    print(f" VICTORIA!!! {nombre_gladiador} has ganado la batalla")
    print(f" {nombre_gladiador} (HP: {vida_del_gladiador}) vs Enemigo: (HP: {vida_del_enemigo}) | POCIONES: {pociones_de_vida}")
else:
    print("DERROTA!!! Has caido en combate!! ")
    print(f" {nombre_gladiador} (HP: {vida_del_gladiador}) vs Enemigo: (HP: {vida_del_enemigo}) | POCIONES: {pociones_de_vida}")


