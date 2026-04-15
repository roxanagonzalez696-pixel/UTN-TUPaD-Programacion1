#VARIABLES 
total_sin_descuento = 0
total_con_descuento = 0

#PUNTO 1 
print("Punto 1: Pedir nombre del Cliente. Solo letras. Validar con while y .isalpha()")
cliente=input("Ingresar el nombre del Cliente: ").strip()

while cliente ==" " or not cliente.isalpha(): #Validamos que el nombre ingresado no sea espacio en blanco ni tenga números o símbolos
    print("Error. Se debe ingresar un nombre sin número, ni espacios, ni símbolos!  ")
    cliente=input("Ingresar nuevo nombre Cliente: ").strip()
print(" El Cliente ingresado es: ", cliente)
print()

#PUNTO 2   
print("Punto 2: Pedir cantidad de productos a comprar. Validar con while y .isalpha() ")
cantidad = input(" Ingresar la cantidad de producto/s a comprar: ").strip()

while  not cantidad.isdigit() or int(cantidad) == 0: #Validamos que la cantidad ingresada sea entero y mayor a cero con 
    print("Error. Se debe ingresar un número entero mayor a cero!  ")
    cantidad = input(" Ingresar nueva cantidad de productos a comprar : ").strip()
print("La cantidad de producto/s ingresado/s es: ", cantidad)
cantidad_entero = int(cantidad) # Convertimos el string cantidad a entero
print()

#PUNTO 3
print("Punto 3: Por cada producto(usando for). Pedir precio. Si tiene descuento o no. Aplicar descuento ")
for i in range(1, cantidad_entero + 1):
    precio = input(f" Ingresar precio de Producto {i} = $  ").strip()

    while not precio.isdigit() or int(precio) == 0: # Se valida que precio ingresado sea entera positiva y mayor a cero 
        print("Error! Ingresar un valor entero positivo y mayor a cero")
        precio = input(f" Producto {i} = Precio: $  ").strip()
    precio_entero = int(precio) #Convertimos el string precio en valor entero

    tiene_descuento = input(" Ingresar (s) si tiene descuento, (n) si no tiene: ").strip().lower() #Convertimos mayúsculas en minúsculas
    while tiene_descuento != "s" and tiene_descuento != "n":#Validamos que solo se ingrese s y n 
        print("Error. En el valor ingresado!  ")
        tiene_descuento = input(" Ingresar (s) si tiene descuento, (n) si no tiene: ").strip().lower()
    total_sin_descuento += precio_entero

    if tiene_descuento =="s":
        precio_final = precio_entero * 0.9
    else:
        precio_final = precio_entero
    total_con_descuento += precio_final

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento /cantidad_entero
print()

#PUNTO 4
#Nota: dentro del for, no logré que la variable tiene_descuento lleve S ó N según lo elejido. Deja el valor asignado en la última iteración
print(" Punto 4: Salida por pantalla - Resúmen de la compra por Cliente ")
print(f" Cliente: {cliente} ")
for i in range (1, cantidad_entero + 1):
    print(f" Producto {i} - Precio: $ {precio_entero} - Descuento (S/N): {tiene_descuento}")
print()

print("Totales")
print("Total sin descuento = $ ", total_sin_descuento)    
print(f"Total con descuento = $  {total_con_descuento:.2f}")
print(f"Ahorro = $  {ahorro:.2f}")
print(f"Promedio por producto = $ {promedio:.2f}")

print("------")



