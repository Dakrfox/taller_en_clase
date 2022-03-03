
"""" 
Un vendedor recibe un sueldo base más un 15% extra por comisión de sus
ventas efectuadas en el mes. El vendedor desea saber cuanto dinero en
total obtendrá por las ventas que realiza en el mes. Desarrolle un programa
en Python que permita mostrar el valor ganado por comisión y el valor total
a pagar al vendedor.
"""

sueldo = float(input("digite el sueldo del vendedor \n"))
numVentas = int(input("digite el numero de ventas realizada en el mes\n"))
sum =0
for n in range(numVentas):
    venta = float (input(f"digite el valor de la venta {n}\n"))
    sum = sum + (venta*0.15)
    
print(f"el valor total de las comisiones es {sum} y el valor total de la mensualidad es {sueldo+sum}")    

    