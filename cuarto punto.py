""" 
Un alumno desea saber cuál será su calificación final en la materia de
fundamentos de programación. Dicha calificación se compone de los
siguientes porcentajes: 50% del promedio de sus tres talleres, 30% de la
calificación de un examen en clase y 20% de la calificación de un proyecto
final.

"""

def talleres():
    sum = 0
    for i in range(3):
        
        valor = float(input(f"digite nota del taller {i+1} \n"))
        if valor>=0 and valor<=5:
            sum = (sum + valor)
        else:
            return "error"
    sum= sum/3
    return sum
taller = talleres()
examen = float(input("digite la nota del examen \n"))
if examen>=0 and examen<=5:
    proyecto = float(input("digite la nota del proyecto \n"))
    if proyecto>=0 and examen<=5:
        op = (taller*0.5)+(examen*0.3)+(proyecto*0.2)
        print(f"la nota es {op}")
        
else:
    print("error")



