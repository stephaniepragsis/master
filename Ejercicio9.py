#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y
# Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla
# con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota>
# cada una de las correspondientes notas introducidas por el usuario

def get_califications(subjects):
    dictionary = {}
    for subject in subjects:
        dictionary[subject] = input(f"Introduce la nota para {subject}: ")
    return dictionary

def print_califications(califications):
    for subject in califications.keys():
        print(f"En {subject} has sacado {califications[subject]}")

asignaturas=["mates", "lengua", "historia"]
print("Esto es un cambio para subir")
print_califications(get_califications(asignaturas))
