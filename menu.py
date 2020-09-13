from hackathon import Registro

def menu():

    print('Bienvenido a la creación de registros')
    print('Selecciona un opción : ')
    print('\t1 - Registrar Docente')
    print('\t2 - Registrar Alumno')
    print('\t3 - Registrar Notas de Alumno')
    print('\t4 - Modificar Docente')
    print('\t5 - Modificar Alumno')
    print('\t6 - Modificar Notas de Alumno')
    print('\t7 - Mostrar Docentes')
    print('\t8 - Mostrar Alumnos')
    print('\t9 - Mostrar las notas de los alumnos registrados')
    print('\t10 - Mostrar los salones asignados al profesor')
    print('\t11 - Eliminar el registro de un docente')
    print('\t12 - Eliminar el registro de un alumno')
    print('\t13 - Eliminar el registro de notas de un alumno')
    print('\t14 - Promedio por salón')
    print('\t15 - Salir')

def continuar(error=False):
    result = True
    while result:
        if error:
            print("Has ingresado una opción erronea")
        opcion = input("¿Deseas continuar con la aplicación? (S/N) >> ") 
        if opcion.lower() == "s":
            break
        elif opcion.lower() == "n":
            result = False
            break
        else:
            pass
    return result
    

def preguntar(pregunta, entero=False):
    while True:
        if entero:
            try:
                dato = int(input(pregunta).strip())
                if dato != '': break
                else: print("No has ingresado ningún número")
            except ValueError:
                print("Debes ingresar un número, intente nuevamente")
        else:
            dato = input(pregunta).strip()
            if dato != '': break
            else: print("No has ingresado ningún texto")

    return dato

def metodo_salon(salon):
    if (salon == 1):
        nombre_salon = "1° Primaria"
    elif (salon == 2):
        nombre_salon = "2° Primaria"
    elif (salon == 3):
        nombre_salon = "3° Primaria"
    elif (salon == 4):
        nombre_salon = "4° Primaria"
    elif (salon == 5):
        nombre_salon = "5° Primaria"
    elif (salon == 6):
        nombre_salon = "6° Primaria"
    elif (salon == 7):
        nombre_salon = "1° Secundaria"
    elif (salon == 8):
        nombre_salon = "2° Secundaria"
    elif (salon == 9):
        nombre_salon = "3° Secundaria"
    elif (salon == 10):
        nombre_salon = "4° Secundaria"
    elif (salon == 11):
        nombre_salon = "5° Secundaria"

    return nombre_salon

try:
    while True:
        nota_alumno = Registro()
        nota_alumno.inner_alumno_nota()
        nota_alumno.inner_profesor_salon()
        nota_alumno.inner_alumno_nota_salon()

        # profesor_salon = Registro()
        # profesor_salon.inner_profesor_salon()

        menu()
        opcion = input("Ingresa la opción >> ")
        if opcion == "1":
            docente = Registro()
            docente.create_table_docente()
            print("")
            ident = preguntar("Por favor introduzca el DNI del profesor que está registrando: ")
            nombre = preguntar("Por favor introduzca el nombre del profesor que está registrando: ")
            edad = preguntar("Por favor introduzca la edad del profesor que está registrando: ", True)
            correo = preguntar("Por favor introduzca el correo del profesor que está registrando: ")
            curso = preguntar("Por favor introduzca el curso al que corresponde el profesor que está registrando: ")
            print("")
            docente.insert_docente(ident, nombre, edad, correo, curso)

            if continuar():
                pass
            else:
                break

        elif opcion == "2":
            alumno = Registro()
            alumno.create_table_alumno()
            print("")
            ident = preguntar("Por favor introduzca el DNI del profesor que está registrando: ")
            nombre = preguntar("Por favor introduzca el nombre del alumno que está registrando: ")
            edad = preguntar("Por favor introduzca la edad del alumno que está registrando: ", True)
            correo = preguntar("Por favor introduzca el correo del alumno que está registrando: ")
            
            while True:
                salon = preguntar(f'''Por favor introduzca el salon al que corresponde el alumno que está registrando:
        1 - Primero de Primaria
        2 - Segundo de Primaria
        3 - Tercero de Primaria
        4 - Cuarto de Primaria
        5 - Quinto de Primaria
        6 - Sexto de Primaria
        7 - Primero de Secundaria
        8 - Segundo de Secundaria
        9 - Tercero de Secundaria
        10 - Cuarto de Secundaria
        11 - Quinto de Secundaria
                >>''', True)
                if (salon >= 1 and salon <= 11):
                    salon = metodo_salon(salon)
                    break
                elif(salon > 11 or salon < 0):
                    print("Ha intducido mal el salon")
            
            alumno.insert_alumno(ident, nombre, edad, correo, salon)

            if continuar():
                pass
            else:
                break

        elif opcion == "3":
            nota = Registro()
            nota.create_table_nota()
            print("")
            ident = preguntar("Por favor introduzca el DNI del alumno que está registrando las notas: ", True)
            bimestre = preguntar("Por favor introduzca el bimestre que le corresponde al alumno: ", True)
            matematica = preguntar("Por favor introduzca la nota del alumno en el curso de Matematica: ", True)
            comunicacion = preguntar("Por favor introduzca la nota del alumno en el curso de Comunicación: ", True)
            ingles = preguntar("Por favor introduzca la nota del alumno en el curso de Inglés: ", True)
            nota.insert_nota(ident, matematica, comunicacion, ingles, bimestre)

            if continuar():
                pass
            else:
                break
        
        elif opcion == "4":
            docente = Registro()
            print("")
            id = preguntar("Por favor introduzca el DNI del profesor, al cual desea modificar: ")
            nombre = preguntar("Por favor introduzca el nuevo nombre del profesor que está registrando: ")
            edad = preguntar("Por favor introduzca la nueva edad del profesor que está registrando: ", True)
            correo = preguntar("Por favor introduzca el nuevo correo del profesor que está registrando: ")
            curso = preguntar("Por favor introduzca el nuevo curso al que corresponde el profesor que está registrando: ")
            print("")
            docente.update_docente(id, nombre, edad, correo, curso)

            if continuar():
                pass
            else:
                break


        elif opcion == "5":

            alumno = Registro()
            print("")
            id = input("Por favor introduzca el id del alumno, al cual desea modificar: ")
            nombre = preguntar("Por favor introduzca el nuevo nombre del alumno que está registrando: ")
            edad = preguntar("Por favor introduzca la nueva edad del alumno que está registrando: ", True)
            correo = preguntar("Por favor introduzca el nuevo correo del alumno que está registrando: ")
            while True:
                salon = preguntar(f'''Por favor introduzca el nuevo salon al que corresponde el alumno que está registrando:
        1 - Primero de Primaria
        2 - Segundo de Primaria
        3 - Tercero de Primaria
        4 - Cuarto de Primaria
        5 - Quinto de Primaria
        6 - Sexto de Primaria
        7 - Primero de Secundaria
        8 - Segundo de Secundaria
        9 - Tercero de Secundaria
        10 - Cuarto de Secundaria
        11 - Quinto de Secundaria
                >>''', True)
                if (salon >= 1 and salon <= 11):
                    salon = metodo_salon(salon)
                    break
                elif(salon > 11 or salon < 0):
                    print("Ha intducido mal el salon")

            print("")
            alumno.update_alumno(id, nombre, edad, correo, salon)

            if continuar():
                pass
            else:
                break

        elif opcion == "6":

            nota = Registro()
            print("")
            id = input("Por favor introduzca el DNI del alumno, al cual desea modificar: ")
            bimestre = preguntar("Por favor introduzca el nuevo bimestre que le corresponde al alumno: ", True)
            matematica = preguntar("Por favor introduzca la nueva nota corregida del alumno en el curso de Matematica: ", True)
            comunicacion = preguntar("Por favor introduzca la nueva nota corregida del alumno en el curso de Comunicación: ", True)
            ingles = preguntar("Por favor introduzca la nueva nota corregida del alumno en el curso de Inglés: ", True)
            nota.update_nota(id, bimestre, matematica, comunicacion, ingles)

            if continuar():
                pass
            else:
                break

        elif opcion == "7":
            docente = Registro()
            docente.fetchall_docentes()
            if continuar():
                pass
            else:
                break
        
        elif opcion == "8":
            alumno = Registro()        
            alumno.fetchall_alumnos()
            if continuar():
                pass
            else:
                break
        
        elif opcion == "9":
            nota = Registro()        
            nota.fetchall_notas()
            if continuar():
                pass
            else:
                break

        elif opcion == "10":
            profesores = Registro()
            profesores.fetchall_docentes_salon()
            if continuar():
                pass
            else:
                break

        elif opcion == "11":
            docente = Registro()
            print("")
            id = preguntar("Por favor introduzca el DNI del profesor, que desea eliminar: ")
            docente.delete_docente(id)

            if continuar():
                pass
            else:
                break
        
        elif opcion == "12":
            alumno = Registro()
            print("")
            id = preguntar("Por favor introduzca el id del alumno, que desea eliminar: ")
            alumno.delete_alumno(id)

            if continuar():
                pass
            else:
                break

        elif opcion == "13":
            nota = Registro()
            print("")
            id = preguntar("Por favor introduzca el id que esta asociado al registro del alumno y que desea eliminar: ")
            nota.delete_nota(id)

            if continuar():
                pass
            else:
                break
        
        elif opcion == "14":
            promedio = Registro()
            print("")
            
            while True:
                salon = preguntar(f'''Por favor introduzca el salon al que corresponde el alumno que está registrando:
        1 - Primero de Primaria
        2 - Segundo de Primaria
        3 - Tercero de Primaria
        4 - Cuarto de Primaria
        5 - Quinto de Primaria
        6 - Sexto de Primaria
        7 - Primero de Secundaria
        8 - Segundo de Secundaria
        9 - Tercero de Secundaria
        10 - Cuarto de Secundaria
        11 - Quinto de Secundaria
                >>''', True)
                if (salon >= 1 and salon <= 11):
                    salon = metodo_salon(salon)
                    break
                elif(salon > 11 or salon < 0):
                    print("Ha intducido mal el salon")
            
            promedio.promedio_salon(salon)

            if continuar():
                pass
            else:
                break

        elif opcion == "15":
            break

        else:
            if continuar():
                pass
            else:
                break
    
    print("Gracias por usar el programa")

except KeyboardInterrupt: # Captura la detención de nuestra aplicación
    print('La aplicación se detuvo')
