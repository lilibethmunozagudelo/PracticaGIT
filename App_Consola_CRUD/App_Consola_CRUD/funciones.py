def listarPersonas(personas):
    print("\nPersonas: \n")
    contador = 1
    for per in personas:
        datos = "{0}. Identificación: {1} | Nombre: {2} (edad {3} años)"
        print(datos.format(contador, per[0], per[1], per[2]))
        contador = contador + 1
    print(" ")

def pedirDatosRegistro():
    identificacionCorrecta = False
    while(not identificacionCorrecta):
        identificacion=input("Ingrese identificación: ")
        if len(identificacion) < 7:
            print("Identificación incorrecta: Debe tener mínimo 8 caracteres")
        elif len(identificacion) > 20:
            print("Identificación incorrecta: Debe tener máximo 20 caracteres")
        else:
            identificacionCorrecta = True

    nombre=input("Ingrese nombre: ")
    
    edadCorrecta = False
    while(not edadCorrecta):
        edad=input("Ingrese edad: ")
        if edad.isnumeric():
            edadCorrecta = True
            edad = int(edad)
        else:
            print("Edad incorrecta: la edad debe ser número unicamente")

    persona=(identificacion, nombre, edad)
    return persona

def pedirDatosActualizacion(personas):
    listarPersonas(personas)
    existePersona = False
    identificacionEditar = input("Ingrese la identificación a editar: ")
    for per in personas:
        if per[0] == identificacionEditar:
            existePersona = True
            break

    if existePersona:
        nombre=input("Ingrese nombre a modificar: ")
        edadCorrecta = False
        while(not edadCorrecta):
            edad=input("Ingrese edad a modificar: ")
            if edad.isnumeric():
                edadCorrecta = True
                edad = int(edad)
            else:
                print("Edad incorrecta: la edad debe ser número unicamente")

        persona=(identificacionEditar, nombre, edad)
    else:
        persona = None

    return persona

def pedirDatosEliminacion(personas):
    listarPersonas(personas)
    existePersona = False
    identificacionEliminar = input("Ingrese la identificación a eliiminar: ")
    for per in personas:
        if per[0] == identificacionEliminar:
            existePersona = True
            break
    if not existePersona:
        identificacionEliminar = ""
    return identificacionEliminar