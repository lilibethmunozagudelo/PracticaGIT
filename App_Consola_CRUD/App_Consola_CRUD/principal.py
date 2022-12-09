from BD.conexion import DAO
import funciones

def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("*********************** MENÚ PRINCIPAL ***********************")
            print("1. Listas personas")
            print("2. Registrar persona")
            print("3. Actualizar persona")
            print("4. Eliminar persona")
            print("5. Salir")
            print("**************************************************************")
            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 5:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion ==5:
                continuar = False
                print("Gracias por usar este sistema")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    dao = DAO()
    if opcion == 1:
        try:
            personas = dao.listarPersonas()
            if len(personas) > 0:
                funciones.listarPersonas(personas)
            else:
                print("No se encontraron personas")
        except:
            print("Ocurrió un error")
    elif opcion == 2:
        persona = funciones.pedirDatosRegistro()
        try:
            dao.registrarPersona(persona)
        except:
            print("Ocurrió un error")
    elif opcion == 3:
        try:
            personas = dao.listarPersonas()
            if len(personas) > 0:
                persona = funciones.pedirDatosActualizacion(personas)
                if persona:
                    dao.actualizarPersona(persona)
                else:
                    print("Identificación no encontrada...\n")
            else:
                print("No se encontraron personas")
        except:
            print("Ocurrió un error")
    elif opcion == 4:
        try:
            personas = dao.listarPersonas()
            if len(personas) > 0:
                IdentificacionEliminar = funciones.pedirDatosEliminacion(personas)
                if not(IdentificacionEliminar == ""):
                    dao.eliminarPersona(IdentificacionEliminar)
                else:
                    print("Identificación no encontrada...\n")
            else:
                print("No se encontraron personas")
        except:
            print("Ocurrió un error")
    else:
        print("Opción no valida...")

menuPrincipal()