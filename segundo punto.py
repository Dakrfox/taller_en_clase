"""
Haga un programa en Python que permita ingresar el dinero invertido por
tres personas para formar una empresa. Cada una de ellas invierte una
cantidad distinta. Imprimir el porcentaje que cada quien invierte con respecto
al total de la inversión.
 
"""
inversion1 = input(" socio 1 digite valor de su inversion")
inversion2 = input(" socio 2 digite valor de su inversion")
inversion3 = input(" socio 3 digite valor de su inversion")

sum = int(inversion1) + int(inversion2) + int(inversion3)
print(sum)
op = int(inversion1)/sum *100
print(f"socio 1 invirtio {op}%")
op = int(inversion2)/sum *100
print(f"socio 2 invirtio {op}%")
op = int(inversion3)/sum *100
print(f"socio 3 invirtio {op}%")