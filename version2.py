class Paciente:
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""
        self.__servicio = ""

    def verNombre(self):
        return self.__nombre
    
    def verServicio(self):
        return self.__servicio
    
    def verGenero(self):
        return self.__genero
    
    def verCedula(self):
        return self.__cedula
    
    def asignarNombre(self, n):
        self.__nombre = n
    
    def asignarServicio(self, s):
        self.__servicio = s
    
    def asignarGenero(self, g):
        self.__genero = g
    
    def asignarCedula(self, c):
        self.__cedula = c

class Sistema:
    def __init__(self):
        self.__lista_pacientes = []  # Corregido el nombre de la lista
        self.__numero_pacientes = 0  # Inicializado en 0

    def ingresarPaciente(self):
        nombre = input("Ingrese el nombre: ")
        cedula = int(input("Ingrese la cédula: "))
        genero = input("Ingrese el género: ")
        servicio = input("Ingrese el servicio: ")
        p = Paciente()
        p.asignarNombre(nombre)
        p.asignarCedula(cedula)
        p.asignarGenero(genero)
        p.asignarServicio(servicio)
        self.__lista_pacientes.append(p)  # Corregido el nombre de la lista
        self.__numero_pacientes = len(self.__lista_pacientes)  # Corregido el nombre de la lista

    def verNumeroPacientes(self):
        return self.__numero_pacientes
    
    def verDatosPaciente(self):
        cedula = int(input("Ingrese la cédula a buscar: "))
        encontrado = False  # Variable para verificar si se encontró el paciente
        for paciente in self.__lista_pacientes:
            if cedula == paciente.verCedula():
                print("Nombre: " + paciente.verNombre())
                print("Cédula: " + str(paciente.verCedula()))
                print("Género: " + paciente.verGenero())
                print("Servicio: " + paciente.verServicio())
                encontrado = True
                break
        if not encontrado:
            print("Paciente no encontrado.")

mi_sistema = Sistema()

while True:
    opcion = int(input("""
        1- Ingresar paciente
        2- Ver número de pacientes
        3- Ver datos de paciente
        4- Salir
        """))
    if opcion == 1:
        mi_sistema.ingresarPaciente()
    elif opcion == 2:
        print("Ahora hay: " + str(mi_sistema.verNumeroPacientes()))
    elif opcion == 3:
        mi_sistema.verDatosPaciente()
    elif opcion == 4:
        break
    else:
        print("Opción no válida.")
