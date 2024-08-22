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
    
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarServicio(self,s):
        self.__servicio = s
    def asignarGenero(self,g):
        self.__genero = g
    def asignarCedula(self,c):
        self.__cedula = c

class Sistema:
    def __init__(self):
        self.__listas_pacietes = []
        self.__numero_pacientes = len(self.__lista_pacientes)
    def ingresarPaciente(self):
        nombre = input("Ingrese e nombre: ")
        cedula = int(input("Ingrese la CC: "))
        genero = input("Ingrese el genero: ")
        servicio = input("Ingreso el servicio: ")
        p = Paciente()
        p.asignarNombre(nombre)
        p.asignarCedula(cedula)
        p.asignarGenero(genero)
        p.asignarServicio(servicio)
        self.__lista_pacientes.append(p)
        self.__numero_pacientes = len(self.__listas_pacietes)
    def verNumeroPacientes(self):
        return self.__numero_pacientes
    def verDatosPaciente(self):
        cedula = int(input("Ingrese la CC a buscar"))
        for paciente in self.__lista_pacientes:
            if cedula == paciente.verCedula():
                print("Nombre: " + paciente.verNombre())
                print("Cedula: " + str(paciente.verCedula()))
                print("Genero: " + paciente.verGenero())
                print("Servicio: " + paciente.verServicio())

mi_sistema = Sistema()

while True:
    opcion = int(input("""
        1- Numero paciente
        2- Numero de Pacientes
        3- Datos paciente
        4- Salir
        """))
    if opcion == 1:
        mi_sistema.ingresarPaciente()
    elif opcion  == 2:
        print("Ahora hay: "+ str(mi_sistema.verNumeroPacientes()))
    elif opcion == 3:
        mi_sistema.verDatosPaciente()
    elif opcion == 4:
        break
    else:
        print("Opciòn no valida")