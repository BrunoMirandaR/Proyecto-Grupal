#Beta del menu
import sys
def carta():
    print("""--------------------- Carta ---------------------
    1. Completo Italiano $3000
    Ingredientes: Palta, tomate y mayo.
    ------------------------------------------------------------------------------------
    2. Completo Aleman $3500
    Ingredientes: Chucrut, palta, tomate y mayo.
    ------------------------------------------------------------------------------------
    3. Completo Dinamico $4000
    Ingredientes: Palta o salsa verde, tomate y mayo.
    ------------------------------------------------------------------------------------
    4. Completo Chacarero $4500
    Ingredientes: Porotos verdes, aji verde y mayo.
    ------------------------------------------------------------------------------------
    5. Completo Barros Luco $5000
    Ingredientes: Queso derretido.
    ------------------------------------------------------------------------------------
    6. Completo Bruno $5500
    Ingredientes: Salsa de pizza, queso derretido, Pepperoni, Pimenton verde y tomate.
    ------------------------------------------------------------------------------------
    7. Completo Diego $6000
    Ingredientes: Papas fritas, pollo apanado, palta, tomate y mayo.
    ------------------------------------------------------------------------------------
    8. Bebida 600ml $1000
    ------------------------------------------------------------------------------------
    9. Jugo natural $1500
    ------------------------------------------------------------------------------------
    10. Papas fritas $2000
    ------------------------------------------------------------------------------------""")

def ventas ():
    while True:
        try:
            total = 0
            while True:
                try:
                    pedido = int(input("Ingrese el numero de su pedido: "))
                    if pedido == 1:
                        total += 3000
                    elif pedido == 2:
                        total += 3500
                    elif pedido == 3:
                        total += 4000
                    elif pedido == 4:
                        total += 4500
                    elif pedido == 5:
                        total += 5000
                    elif pedido == 6:
                        total += 5500
                    elif pedido == 7:
                        total += 6000
                    elif pedido == 8:
                        total += 1000
                    elif pedido == 9:
                        total += 1500
                    elif pedido == 10:
                        total += 2000
                    else:
                        print("Pedido no valido")
                    continue
                    while True:
                        try:
                            continuar = input("Desea seguir pidiendo? (si/no): ")
                            if continuar == "si":
                                break
                            elif continuar == "no":
                                print("Total a pagar: $", total)
                                exit()
                            else:
                                print("Respuesta no valida")
                            continue
                        except ValueError:
                            print("Respuesta no valida")
                        continue
                except ValueError:
                    print("Pedido no valido")
                continue
        except ValueError:
            print("Pedido no valido")
        continue

def menu():
    x = 0
    print("------------- Hola, Bienvenido a MIRANDAS -------------")
    while x != 4:
        x = int(input("""Escriba el numero de la opcione que desea usar: 
        1) Ver carta
        2) Comprar
        3) Miembros VIP
        4) Salir
        """))
        if x == 1:
            carta()
        elif x == 2:
            ventas()
        elif x == 3:
            sesion()
        elif x == 4:
            sys.exit()
        else:
            print("Opcion no valida, intentelo de nuevo")

global rut
def sesion():
    intento = 4
    rut = -5

    while rut < 0 or rut < 1000000:
        rut=int(input("Ingrese su rut sin guin ni puntos (EJ:123456789): ")[0:9])

        if rut < 0 or rut < 1000000:
            intento = intento - 1
            print("Rut invalido, intentelo nuevamente")
            print (f"Le quedan: {intento} intentos.")
            print("")

            if intento == 0:
                print("Se superaron los intentos, intentelo más tarde.")
                sys.exit()
    

        else:
            contraseña=input("Ingrese su contraseña: ")
            break
    

    rut_cambiado = str(rut)[:-1] + "-" + str(rut)[-1]


    #ESTO NO ESTARÁ EN AL PROYECTO FINAL, SOLO ES PARA COMPROBAR
    print("Muy bien hecho pe causa")
    print(f""" ===SUS DATOS===
        Rut: {rut_cambiado}
        Contraseña: {contraseña}
            """)
    menu()
    
    


