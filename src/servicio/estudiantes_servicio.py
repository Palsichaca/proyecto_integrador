from modelo.cursos import Cursos
from modelo.estudiantes import Estudiantes


#reune todos los datos necesarios para creae estudiantes(agregar el resto mas tarde)
class EstudiantesServicio:
    @staticmethod
    def crear_estudiante(nombre, curso_id):
        curso = Cursos.get(curso.id==curso_id)
        estudiante =Estudiantes.create(nombre=nombre, curso=curso )
        return estudiante 
    @staticmethod    
    def mostrar_estudiante():
        return list(Estudiantes.select())

    @staticmethod
    def eliminar_estudiante(id):
        estudiante = Estudiantes.get(Estudiantes.id ==id)
        estudiante.delete_instance()
        return estudiante