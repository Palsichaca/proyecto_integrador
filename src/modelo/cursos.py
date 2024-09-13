from peewee import Model, Autofield, Charfield, Datafield, Timefield
from basedato.db import db
#base de datos de cursos
class Cursos(Model):
    id = Autofield()
    descripcion = Charfield
    nombre = Charfield(unique=True)
    fecha_de_inicio = Datafield()
    fecha_de_fin = Datafield()
    horas = Timefield

    class Meta:
        database = db
        table_name = "cursos"
    