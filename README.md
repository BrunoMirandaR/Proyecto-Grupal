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
