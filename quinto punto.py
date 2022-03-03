""" 
Dada la cantidad de alumnos de Redes, contabilidad y diseño determine el
porcentaje de alumnos de cada uno de los cursos.
"""

def aver():
    sum =0
    nalum = int(input("digite cantidad de alumnos: \n"))
    for i in range(nalum):
        nota = float(input(f"digite la nota del alumno {i+1}"))
        sum = sum + nota
    return sum/nalum
print("inserte valores de redes")
redes=(aver())

print("inserte valores de contabilidad")
contabilidad=(aver())

print("inserte valores de diseño")
diseño=(aver())

print(f"el promedio de redes es {redes}")
print(f"el promedio de contabilidad es {contabilidad}")
print(f"el promedio de diseño es {diseño}")
