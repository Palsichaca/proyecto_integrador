from servicio.curso_servicio import CursoServicio

#clase para crear cursos y mostrarlos
class CursoControlador():
    def crear(nombre):
        return CursoServicio.crear_curso(nombre)

    def mostrar():
        return CursoServicio.mostrar_curso()