from servicio.estudiantes_servicio import EstudiantesServicio

#clase para crear estudiantes y mostrarlos
class EstudianteControlador():
    def crear(nombre,curso_id):
        return EstudiantesServicio.crear_estudiante(nombre,curso_id)
    def mostrar():
        return EstudiantesServicio.mostrar_estudiante()

    def eliminar():
        return EstudiantesServicio.eliminar_estudiante()
    
