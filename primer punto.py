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

    
print("reparticion de dinero de donacion")
don = int(input("digite el valor de la donacion: \n"))
administracion = don*0.35
sistemas = administracion*0.25
tc = sistemas*0.1
sum = administracion + sistemas + tc
resta = don-sum
print(f"a telecomunicacion se le dara {tc}")
print(f"a sistemas se le dara {sistemas}$")
print(f"a administracion se le dara {administracion}$")
print(f"a contabilidad se le dara {resta}$")






