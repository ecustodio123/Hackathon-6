from connection.conn import Connection

class Registro:

    def __init__(self):
        pass

    def create_table_docente(self):

        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS profesor(
                    id SERIAL PRIMARY KEY NOT NULL,
                    nombre_profesor varchar(50) NOT NULL,
                    edad REAL,
                    correo varchar(75) NOT NULL,
                    curso varchar(50) NOT NULL
                );
            '''

            conn.execute_query(query)
            conn.commit()

        except Exception as e:
            print(f'{str(e)}')

        finally:
            conn.close_connection()

    def create_table_alumno(self):

        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS alumno(
                    id SERIAL PRIMARY KEY NOT NULL,
                    nombre_alumno varchar(50) NOT NULL,
                    edad REAL,
                    correo varchar(75) NOT NULL,
                    salon varchar(50) NOT NULL
                );
            '''

            conn.execute_query(query)
            conn.commit()

        except Exception as e:
            print(f'{str(e)}')

        finally:
            conn.close_connection()

    def create_table_nota(self):

        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS nota(
                    id SERIAL PRIMARY KEY NOT NULL,
                    matematica REAL,
                    comunicacion REAL,
                    ingles REAL,
                    bimestre integer
                );
            '''
            conn.execute_query(query)
            conn.commit()

        except Exception as e:
            print(f'{str(e)}')

        finally:
            conn.close_connection()

    def fetchall_docentes(self):
        try:
            conn = Connection()
            query = '''
                SELECT * from profesor;
            '''

            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:
                print(f'DNI => {row[0]}')
                print(f'Nombre => {row[1]}')
                print(f'Edad => {row[2]}')
                print(f'Correo => {row[3]}')
                print(f'Curso => {row[4]}')
                print('=====================')

        except Exception as e:
            print(f'{str(e)}')

        finally:
            conn.close_connection()

    def fetchall_alumnos(self):
        try:
            conn = Connection()
            query = '''
                SELECT * from alumno;
            '''

            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:
                print(f'DNI => {row[0]}')
                print(f'Nombre => {row[1]}')
                print(f'Edad => {row[2]}')
                print(f'Correo => {row[3]}')
                print(f'Salon => {row[4]}')
                print('=====================')

        except Exception as e:
            print(f'{str(e)}')

        finally:
            conn.close_connection()
        
    def fetchall_notas(self):
        try:
            conn = Connection()
            query = '''
                SELECT * from alumno_nota;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:
                print('=====================')
                print(f'DNI => {row[0]}')
                print(f'Bimestre => {row[8]}')
                print(f'Nombre del alumno => {row[1]}')
                print(f'Edad => {row[2]}')
                print(f'Correo => {row[3]}')
                print(f'Salon => {row[4]}')
                print(f'Matematica => {row[5]}')
                print(f'Comunicacion => {row[6]}')
                print(f'Ingles => {row[7]}')
                print('=====================')

        except Exception as e:
            print(f'{str(e)}')

        finally:
            conn.close_connection()

    def fetchall_docentes_salon(self):
        try:
            conn = Connection()
            query = '''
                SELECT * from profesor_salon_completo;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:
                print('=====================')
                print(f'Nombre => {row[1]}')
                print(f'Edad => {row[2]}')
                print(f'Correo => {row[3]}')
                print(f'Curso => {row[4]}')
                print(f'Salón => {row[5]}')
                print('=====================')

        except Exception as e:
            print(f'{str(e)}')

        finally:
            conn.close_connection()

    def insert_docente(self, ident, nombre, edad, correo, curso):
        
        self.ident = ident
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.curso = curso

        try: 
            conn = Connection()
            query = f'''
                INSERT INTO profesor (id, nombre_profesor, edad, correo, curso) VALUES ('{ident}','{nombre}', {edad} , '{correo}' ,'{curso}')
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f"Se ha registrado correctamente el profesor con nombre {nombre}")

        except Exception as e:
            print(f'{str(e)}')

        finally:
            conn.close_connection()

    def insert_alumno(self, ident, nombre, edad, correo, salon):
        
        self.ident = ident
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.salon = salon

        try: 
            conn = Connection()
            query = f'''
                INSERT INTO alumno (id, nombre_alumno, edad, correo, salon) VALUES ('{ident}','{nombre}', {edad} , '{correo}' ,'{salon}')
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f"Se ha registrado correctamente el alumno con nombre {nombre}")

        except Exception as e:
            print(f'{str(e)}')

        finally:
            conn.close_connection()

    def insert_nota(self, ident, matematica, comunicacion, ingles, bimestre):
        self.ident = ident
        self.matematica = matematica
        self.comunicacion = comunicacion
        self.ingles = ingles
        self.bimestre = bimestre

        try: 
            conn = Connection()
            query = f'''
                INSERT INTO nota (id, matematica, comunicacion, ingles, bimestre) VALUES ({ident}, {matematica} ,{comunicacion}, {ingles}, {bimestre})
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f"Se ha registrado correctamente las notas del alumno con el id {ident}")

        except Exception as e:
            print(f'{str(e)}')

        finally:
            conn.close_connection()

    def update_docente(self, id, nombre, edad, correo, curso):

        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.curso = curso

        try: 
            conn = Connection()
            query = f'''
                UPDATE profesor SET nombre_profesor = '{nombre}', edad = {edad}, correo = '{correo}', curso = '{curso}' WHERE id = {id};
            '''
            cursor = conn.execute_query(query)
            conn.commit()
            print(f'''Se ha actualizado al profesor registrado con el id {id}:
                        Nombre: {nombre}
                        Edad: {edad}
                        Correo: {correo}
                        Curso: {curso}
            ''')

        except Exception as e:
            print(f'{str(e)}')

        finally:
            conn.close_connection()

    def update_alumno(self, id, nombre, edad, correo, salon):

        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.salon = salon

        try: 
            conn = Connection()
            query = f'''
                UPDATE alumno SET nombre_alumno = '{nombre}', edad = {edad}, correo = '{correo}', salon = '{salon}' WHERE id = {id};
            '''
            cursor = conn.execute_query(query)
            conn.commit()
            print(f'''Se ha actualizado al alumno registrado con el id {id}:
                        Nombre: {nombre}
                        Edad: {edad}
                        Correo: {correo}
                        Salón: {salon}
            ''')

        except Exception as e:
            print(f'{str(e)}')

        finally:
            conn.close_connection()

    def update_nota(self, id, bimestre, matematica, comunicacion, ingles):

        self.id = id
        self.bimestre = bimestre
        self.matematica = matematica
        self.comunicacion = comunicacion
        self.ingles = ingles

        try: 
            conn = Connection()
            query = f'''
                UPDATE nota SET matematica = {matematica}, comunicacion = {comunicacion}, ingles = {ingles}, bimestre = {bimestre} WHERE id = {id};
            '''
            cursor = conn.execute_query(query)
            conn.commit()
            print(f'''Se ha actualizado las notas del alumno registrado con el DNI {id}:
                        Matematica: {matematica}
                        Comunicacion: {comunicacion}
                        Ingles: {ingles}
            ''')

        except Exception as e:
            print(f'{str(e)}')

        finally:
            conn.close_connection()
    
    def delete_docente(self, id):
        try:
            conn = Connection()
            query = f'''
                DELETE FROM profesor WHERE id ={id};
            '''

            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se elimino el profesor registrado con el ID {id}')
        
        except Exception as e:
            print(f'{str(e)}')
        finally:
            conn.close_connection()
    
    def delete_alumno(self, id):
        try:
            conn = Connection()
            query = f'''
                DELETE FROM alumno WHERE id ={id};
            '''

            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se elimino el alumno registrado con el ID {id}')
        
        except Exception as e:
            print(f'{str(e)}')
        finally:
            conn.close_connection()

    def delete_nota(self, id):
        try:
            conn = Connection()
            query = f'''
                DELETE FROM nota WHERE id ={id};
            '''

            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se elimino el alumno registrado con el ID {id}')
        
        except Exception as e:
            print(f'{str(e)}')
        finally:
            conn.close_connection()

    def inner_alumno_nota(self):

        try:
            conn = Connection()
            query = '''
                DROP TABLE IF EXISTS alumno_nota;
            '''
            
            conn.execute_query(query)
            conn.commit()

        except Exception as e:
            print(f'{str(e)}')

        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS alumno_nota(
                    id SERIAL PRIMARY KEY NOT NULL,
                    nombre_alumno varchar(50) NOT NULL,
                    edad REAL,
                    correo varchar(75) NOT NULL,
                    salon varchar(50) NOT NULL,
                    matematica REAL,
                    comunicacion REAL,
                    ingles REAL,
                    bimestre integer
                );
            '''
            conn.execute_query(query)
            conn.commit()

        except Exception as e:
            print(f'{str(e)}')

        try:
            conn = Connection()
            query = f'''
            INSERT INTO alumno_nota(nombre_alumno, edad, correo, salon, matematica, comunicacion, 
            ingles, bimestre)
            SELECT nombre_alumno, edad, correo, salon, matematica, comunicacion, 
            ingles, bimestre FROM alumno INNER JOIN nota on alumno.id = nota.id
            '''
            cursor = conn.execute_query(query)
            conn.commit()

        except Exception as e:
            print(f'{str(e)}')

        finally:
            conn.close_connection()

    def inner_profesor_salon(self):

        try:
            conn = Connection()
            query = '''
                DROP TABLE IF EXISTS profesor_salon_completo;
            '''
            
            conn.execute_query(query)
            conn.commit()

        except Exception as e:
            print(f'{str(e)}')

        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS profesor_salon_completo(
                    id SERIAL PRIMARY KEY NOT NULL,
                    nombre_profesor varchar(50) NOT NULL,
                    edad REAL,
                    correo varchar(75) NOT NULL,
                    curso varchar(50) NOT NULL,
                    id_salon varchar(50) NOT NULL
                );
            '''
            conn.execute_query(query)
            conn.commit()

        except Exception as e:
            print(f'{str(e)}')

        try:
            conn = Connection()
            query = f'''
            INSERT INTO profesor_salon_completo(nombre_profesor, edad, correo, curso, id_salon)
            SELECT nombre_profesor, edad, correo, curso, id_salon
            FROM profesor INNER JOIN salon_profe on profesor.id = salon_profe.id_profesor
            '''
            cursor = conn.execute_query(query)
            conn.commit()

        except Exception as e:
            print(f'{str(e)}')

        finally:
            conn.close_connection()

    def inner_alumno_nota_salon(self):

        try:
            conn = Connection()
            query = '''
                DROP TABLE IF EXISTS alumno_nota_salon;
            '''
            
            conn.execute_query(query)
            conn.commit()

        except Exception as e:
            print(f'{str(e)}')

        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS alumno_nota_salon(
                    id SERIAL PRIMARY KEY NOT NULL,
                    nombre_alumno varchar(50) NOT NULL,
                    salon varchar(50) NOT NULL,
                    matematica REAL,
                    comunicacion REAL,
                    ingles REAL,
                    bimestre integer,
                    nombre_profesor varchar(50) NOT NULL
                );
            '''
            conn.execute_query(query)
            conn.commit()

        except Exception as e:
            print(f'{str(e)}')

        try:
            conn = Connection()
            query = f'''
            INSERT INTO alumno_nota_salon(nombre_alumno, salon, matematica, comunicacion, ingles, bimestre, nombre_profesor)
            SELECT nombre_alumno, salon, matematica, comunicacion, ingles,  bimestre, nombre_profesor
            FROM alumno_nota INNER JOIN profesor_salon_completo on alumno_nota.salon = profesor_salon_completo.id_salon
            '''
            cursor = conn.execute_query(query)
            conn.commit()

        except Exception as e:
            print(f'{str(e)}')

        finally:
            conn.close_connection()

    def promedio_salon(self, salon):

        self.salon = salon

        try:
            conn = Connection()
            query = f'''
                SELECT matematica, comunicacion, ingles
                from alumno_nota_salon Where salon='{salon}';
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            suma_matematica = 0
            suma_comunicacion = 0
            suma_ingles = 0
            cont = 0

            for row in rows:
                
                suma_matematica = row[0] + suma_matematica
                suma_comunicacion = row[1] + suma_comunicacion
                suma_ingles = row[2] + suma_ingles
                cont = cont + 1

            promedio_matematica = suma_matematica / cont
            promedio_comunicacion = suma_comunicacion / cont
            promedio_ingles = suma_ingles / cont

            print(f"El promedio en el salon de {salon} en matematica es de {promedio_matematica}")
            print(f"El promedio en el salon de {salon} en comunicacion es de {promedio_comunicacion}")
            print(f"El promedio en el salon de {salon} en ingles es de {promedio_ingles}")


                # print('=====================')
                # print(f'ID => {row[0]}')
                # print(f'Bimestre => {row[8]}')
                # print(f'Nombre del alumno => {row[1]}')
                # print(f'Edad => {row[2]}')
                # print(f'Correo => {row[3]}')
                # print(f'Salon => {row[4]}')
                # print(f'Matematica => {row[5]}')
                # print(f'Comunicacion => {row[6]}')
                # print(f'Ingles => {row[7]}')
                # print('=====================')

        except Exception as e:
            print(f'{str(e)}')

        finally:
            conn.close_connection()
