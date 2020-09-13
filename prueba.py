from connection.conn import Connection

class Alumno:
    def __init__(self, nombre, edad, correo, salon):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.salon = salon
        
class Docente: 
    def __init__(self, nombre, edad, coreo, curso):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.curso = curso

class Registro(Docente, Alumno):
    def __init__(self, nombre_tabla):
        self.nombre_tabla = nombre_tabla

    def set_docente(self, nombre, edad, coreo, curso):
        Docente.__init__(self, nombre, edad, correo, curso)

    def set_alumno(self, nombre, edad, coreo, salon):
        Alumno.__init__(self, nombre, edad, correo, salon)

    def create_table(self, nombre_tabla):
        self.nombre_tabla = nombre_tabla
        
        


        try:
            conn = Connection()
            query = f'''
                CREATE TABLE IF NOT EXISTS {nombre_tabla}(
                    id SERIAL PRIMARY KEY NOT NULL,

                ) 
            '''

    
    
