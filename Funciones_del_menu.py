#Beta del menu
import sys
desc = False
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
    global desc
    global comida
    global totaliva
    total = 0
    comida = ["Completo Italiano $3000","Completo Aleman $3500","Completo Dinamico $4000","Completo Chacarero $4500","Completo Barros Luco $5000","Completo Bruno $5500","Completo Diego $6000","Bebida 600ml $1000","Jugo natural $1500","Papas fritas $2000"]
    while True:
        try:
            try:
                    pedido = int(input("Ingrese el numero de su pedido: "))
                    if pedido == 1:
                        total += 3000
                        print("Ha seleccionado\n",comida[0])

                    elif pedido == 2:
                        total += 3500
                        print("Ha seleccionado\n",comida[1])
                    elif pedido == 3:
                        total += 4000
                        print("Ha seleccionado\n",comida[2])
                    elif pedido == 4:
                        total += 4500
                        print("Ha seleccionado\n",comida[3])
                    elif pedido == 5:
                        total += 5000
                        print("Ha seleccionado\n",comida[4])
                    elif pedido == 6:
                        total += 5500
                        print("Ha seleccionado\n",comida[5])
                    elif pedido == 7:
                        total += 6000
                        print("Ha seleccionado\n",comida[6])
                    elif pedido == 8:
                        total += 1000
                        print("Ha seleccionado\n",comida[7])
                    elif pedido == 9:
                        total += 1500
                        print("Ha seleccionado\n",comida[8])
                    elif pedido == 10:
                        total += 2000
                        print("Ha seleccionado\n",comida[9])
                    else:
                        print("Pedido no valido")
                    while True:
                        try:
                            print("")
                            continuar = input("Desea seguir pidiendo? (si/no): ")
                            if continuar == "si":
                                break
                            elif continuar == "no":
                                if desc==True: #CON DESCUENTO ACTIVO

                                    monto = total
                                    subtotal = monto
                                    IVA = total * 0.19
                                    total = total * 0.81
                                    monto = monto * 0.85
                                    print("Precio: $",total)
                                    print("IVA: $",IVA)
                                    print("SubTotal:$",subtotal)
                                    print("Descuento: $ -15% ")
                                    print("Total a pagar: $",monto)
                                    exit()


                                elif desc==False: #CON DESCUENTO DESACTIVADO
                                    monto = total
                                    IVA = total * 0.19
                                    total = total * 0.81
                                    print("Precio: $",total )
                                    print("IVA: $",IVA)
                                    print("Total a pagar: $",monto)
                                    exit()
                            else:
                                print("Respuesta no valida")
                            continue
                        except ValueError:
                            print("Respuesta no valida")
                        continue
            except ValueError:
                    print("Pedido no valido")
        except ValueError:
            print("Pedido no valido")
        continue

def vip():
    global desc
    

    print("Vip consiste en tener un 15% de descuento en cada compra por un monto de 4.000 al mes")
    print("")
    salidavip = False
    while salidavip == False:
        vip=str(input("""Desea pagar para obtener su descuento (si/no)
        Su eleccion: """))
        if vip == "si":
            desc=True
            print("   Usuario vip $3240")
            print("      Iva(19%) $760")
            print("Total a pagar: $4000")
            print("")
            salidavip = True
        elif vip == "no":
            print("")
            salidavip = True
        else:
            print("Opcion no valida.")
global rut
def sesion():
    intento = 3
    rut = -5
    
    while rut < 0 or rut < 10000000: #se coloca el valor para un rut valido
        rut=int(input("Ingrese su rut sin guin ni puntos (EJ:123456789): ")[0:9])

        if rut < 0 or rut < 10000000:
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
    
    

