import json

from Paciente import Paciente


class Objectencoder:

    def decoder(self, a):
        if not a:
            return a
        else:
            lista = []
            for i in range(len(a)):
                b = list(a[i].keys())
                clase = eval(str(b[0]))
                lista.append(clase(a[i]['Paciente']['Apellido'], a[i]['Paciente']['Nombre'],
                                   a[i]['Paciente']['Telefono'], a[i]['Paciente']['Altura'],
                                   a[i]['Paciente']['Peso']))
            return lista

    def lectura(self, archivo):
        with open(archivo, encoding='UTF-8') as fuente:
            dic = list(json.load(fuente))
            if dic == {}:
                dic = None
            fuente.close()
            return dic

    def guardado(self, elementos, archivo):
        with open(archivo, 'w', encoding='UTF-8') as destino:
            json.dump(elementos, destino, indent=4)
            destino.close()
