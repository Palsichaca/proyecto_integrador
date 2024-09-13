from modelo.cursos import Cursos

#reune todos los datos necesarios para creae clase(agregar el resto mas tarde)
class CursoServicio:
    @staticmethod
    def crear_curso(nombre):
        curso = Cursos.create(nombre=nombre)
        return curso

    @staticmethod
    def mostrar_curso():
        return list(Cursos.select())


        