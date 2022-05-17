class Paciente:
    __apellido = ''
    __nombre = ''
    __telefono = 0
    __altura = 0
    __peso = 0

    def __init__(self, ape, nom, tel, alt, pes):
        self.__apellido = ape
        self.__nombre = nom
        self.__telefono = tel
        self.__altura = alt
        self.__peso = pes

    def getapellido(self):
        return self.__apellido

    def getnombre(self):
        return self.__nombre

    def gettelefono(self):
        return self.__telefono

    def getaltura(self):
        return self.__altura

    def getpeso(self):
        return self.__peso

    def guardarvalores(self, ape, nom, tel, alt, pes):
        self.__apellido = ape
        self.__nombre = nom
        self.__telefono = tel
        self.__altura = alt
        self.__peso = pes


