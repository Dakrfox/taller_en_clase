# -*- coding: utf-8 -*-
"""
Una Institución educativa ha recibido una donación especial que será
repartida entre las carreras de Telecomunicaciones, Sistemas,
Administración y Contabilidad de la siguiente forma:
    a. Telecomunicaciones 10% del valor dado a sistemas
    b. Sistemas: 25% del valor dado a Administración
    c. Administración: 35% del valor de la donación
    d. Contabilidad: lo que resta de la donación
"""
def ope(donacion,percentage):
    op = float(donacion)*percentage
    return op
    
print("reparticion de dinero de donacion")
don = input("digite el valor de la donacion: \n")
print(f"a telecomunicacion se le dara el 10% {ope(don,0.1)}$")
print(f"a sistemas se le dara el 25% {ope(don,0.25)}$")
print(f"a administracion se le dara el 35% {ope(don,0.35)}$")
print(f"a contabilidad se le dara el 30% {ope(don,0.30)}$")

def perinv():
    
    for n in 3:
        inversion = input(f" socio {n} digite valor de su inversion")
        sum.append(inversion)
    return sum

"""
Haga un programa en Python que permita ingresar el dinero invertido por
tres personas para formar una empresa. Cada una de ellas invierte una
cantidad distinta. Imprimir el porcentaje que cada quien invierte con respecto
al total de la inversión.
 
"""
print (perinv())



