# Proyecto-Grupal
import sys
global rut
def sesion():
    intento = 4
    rut = int(-5)

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
    #Muestra menu
    menu()
    
#Beta del menu e ingreso de pedidos que se me olvido hacer profe no me rete
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
8. Bebida 500ml $1000
------------------------------------------------------------------------------------
9. Jugo natural $1500
------------------------------------------------------------------------------------
10. Papas fritas $2000
------------------------------------------------------------------------------------""")
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
    x = 5
    
    while x != 1 or x != 2 or x != 3 or x != 4:
        x=int(input("alo: "))
       
    
        if x == 1:
         print("elegiste el 1")
    
        elif x == 2:
         print("elegiste el 2")
    
        elif x == 3:
         print("elegiste el 3")
    
        elif x == 4:
         print("elegiste el 4")
    
#INICIO DE SESION
sesion()
