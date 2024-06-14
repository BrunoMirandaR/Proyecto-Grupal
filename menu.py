#menu.py
import sys
import Funciones_del_menu as lb

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
        lb.carta()
    elif x == 2:
        lb.comprar()
    elif x == 3:
        lb.miembros()
    elif x == 4:
        sys.exit()
    else:
        print("Opcion no valida, intentelo de nuevo")
