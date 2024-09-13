from peewee import Model, Autofield, Charfield, Integerfield, Datafield, Timefield
from basedato.db import db
from modelo.cursos import Cursos
#base de datos de estudiantes
class Estudiantes(Model):
    id = Autofield()
    nombre = Charfield()
    dni = Integerfield()
    correo_electronico = Charfield()
    numero_de_telefono = Integerfield()
    fecha_de_nacimiento = Datafield()
    curso_id = ForeignKeyField(Cursos)

    class Meta:
        database = db
        table_name = "estudiantes"