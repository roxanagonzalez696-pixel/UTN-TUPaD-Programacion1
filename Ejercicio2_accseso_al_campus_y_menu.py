# EJERCICIO 2 — “Acceso al Campus y Menú Seguro”

# PUNTO 1.
print("Punto 1: Definir credenciales fijas. Solicitamos usuario y clave por primera vez")
usuario_correcto = input("Ingrese su usuario por primera vez: ").strip()
clave_correcta = input("Ingrese su clave por primera vez: ").strip()
print("Usuario y clave guardados exitosamente")
print(" -----------------")

#PUNTO 2
print("Punto 2: Permitir máximo de 3 intentos para ingresar clave y usuario")

for i in range(1,4):
    usuario = input("Ingrese su usuario: ").strip()
    clave = input("Ingrese su clave: ").strip()
    if usuario == usuario_correcto and clave == clave_correcta:
        print(f" Intento {i} / 3 - Usuario: {usuario} - Clave: {clave}")
        print("Ingreso concedido")
        break
    else:
        print(f" Intento {i} / 3 - Usuario: {usuario} - Clave: xxx")
        print("Error! Credenciales invalidas")
 #PUNTO 3.       
 #Punto 3: Si falla en 3 intentos mostrar: CUENTA BLOQUEADA y continuar     
    if i == 3:
        print(" Cuenta bloqueada, Gestionar cambio de usuario y clave ")  
print("--------------------")

#PUNTO 4
print("Punto 4: Si el ingreso es correcto acceder al menú mediante un while")

usuario = input("Ingrese su usuario: ").strip()
clave = input("Ingrese su clave: ").strip()
if usuario == usuario_correcto and clave == clave_correcta:
    print("Ingreso concedido")
    opcion = input("Ingresar 1- Estado. 2- Cambiar clave, 3- Mensaje, 4- Salir: ").strip()
    while not opcion.isdigit() or int(opcion)>4: 
        print("PUNTO 5- Validamos que el string ingresado sea un nro entero positivo y que se encuentre entre 1 y 4")
        print("Error en la opción ingresada !")
        opcion = input("Ingresar 1- Estado. 2- Cambiar clave, 3- Mensaje, 4- Salir: ").strip()
    opcion_int = int(opcion)
    if opcion_int == 1:
        print(" Opción 1 ")
        print(" Estado = INSCRIPTO ")
    elif opcion_int == 2:
        print(" Opción 2 - Cambiar clave ")
        clave = input("Ingrese su nueva clave: ").strip()
        while  not(len(clave) >=6): # Verifica que la clave ingresda contenga 6 caracteres
            print(" Error mínimo 6 caracteres ")
            clave = input("Ingrese su nueva clave con un mínimo de 6 dígitos : ").strip()
        clave_correcta = clave
        if clave == clave_correcta: #Confirma nueva clave ingresada
            print(" Nueva clave generada exitosamente! ")
            clave_correcta = clave
        else:   
            print("Error! gestionar nueva usuario y clave")
    elif opcion_int == 3:
        print(" Opción 3")
        print(" ¡Bienvenido a la Tecnicatura Univerditaria en Progración a distancia FRSN! ") #
    elif opcion_int == 4:
        print("Opción 4 - Cerrar sesión ")
    else:
        print(" Error opción fuera de rango!  ")
    print()

else:
    print("Error! Credenciales invalidas")
print("--------------------")





    

