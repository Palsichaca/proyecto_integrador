from peewee import MySQLDatabase
#local
#datos de base de datos
db = MySQLDatabase(
    "db:marte",
    user="root",
    password="",
    host="localhost",
    port=3306
)