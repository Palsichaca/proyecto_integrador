from basedato.db import db

from modelo.estudiantes import Estudiantes
from modelo.cursos import Cursos


def main():
    db.connect()
    db.create_tables([Curso, ])



if __name__ == "__main__":
    main()
            

