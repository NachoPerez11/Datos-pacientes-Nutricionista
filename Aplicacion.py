from tkinter import *

from tkinter import ttk, messagebox

import tkinter as tk

from ObjectEncoder import Objectencoder


class App:
    __ventana = None
    __apellido = None
    __nombre = None
    __telefono = None
    __altura = None
    __peso = None
    __nuevopaciente = None
    __imc = None
    __imcven = None
    __compcorp = None
    __listbox = None
    __lista = None
    __datos = None
    __indice = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Lista de Pacientes')
        self.__ventana.geometry('400x315')
        self.__ventana.resizable(0, 0)
        self.__ventana['borderwidth'] = 0
        opts = {'fill': 'both', 'expand': 'True', 'padx': '5', 'pady': '5'}
        frame = tk.Frame(self.__ventana)
        frame.pack(side=LEFT, fill=BOTH, expand=True, padx=15, pady=5)
        self.__listbox = tk.Listbox(frame)
        self.__listbox.pack(side=LEFT, fill=Y, pady=10)
        scroll = tk.Scrollbar(frame, command=self.__listbox.yview)
        scroll.pack(fill=Y, expand=True)
        self.__listbox.config(yscrollcommand=scroll.set)
        self.cargarpacientes()
        self.dobleclick(self.ponercontacto)
        frame1 = tk.LabelFrame(self.__ventana, text='Paciente')
        frame1.pack(side=TOP, padx=15, pady=10)
        frame2 = tk.Frame(self.__ventana)
        frame2.pack(side=BOTTOM, **opts)
        frame5 = tk.Frame(frame1)
        frame5.pack(side=BOTTOM, **opts)
        tk.Button(frame2, text='Agregar paciente', command=self.agregarpvista).pack(side=TOP, pady=15)
        frame3 = tk.Frame(frame1)
        frame3.pack(side=LEFT, **opts)
        tk.Label(frame3, text='Apellido').pack(side=TOP, **opts)
        tk.Label(frame3, text='Nombre').pack(side=TOP, **opts)
        tk.Label(frame3, text='Teléfono').pack(side=TOP, **opts)
        tk.Label(frame3, text='Altura').pack(side=TOP, **opts)
        tk.Label(frame3, text='Peso').pack(side=TOP, **opts)
        frame4 = tk.Frame(frame1)
        frame4.pack(side=RIGHT, **opts)
        self.__indice = StringVar()
        self.__imc = StringVar()
        self.__apellido = StringVar()
        self.__nombre = StringVar()
        self.__telefono = StringVar()
        self.__peso = StringVar()
        self.__altura = StringVar()
        self.apellidoentry = tk.Entry(frame4, textvariable=self.__apellido)
        self.apellidoentry.pack(side=TOP, **opts)
        self.nombreentry = tk.Entry(frame4, textvariable=self.__nombre)
        self.nombreentry.pack(side=TOP, **opts)
        self.telefonoentry = tk.Entry(frame4, textvariable=self.__telefono)
        self.telefonoentry.pack(side=TOP, **opts)
        self.alturaentry = tk.Entry(frame4, textvariable=self.__altura)
        self.alturaentry.pack(side=TOP, **opts)
        self.pesoentry = tk.Entry(frame4, textvariable=self.__peso)
        self.pesoentry.pack(side=TOP, **opts)
        verimc = tk.Button(frame5, text='Ver IMC', command=self.imcvista)
        verimc.pack(side=LEFT, padx=5, pady=5)
        borrar = tk.Button(frame5, text='Borrar', command=self.borrarpaciente)
        borrar.pack(side=LEFT, padx=5, pady=5)
        guardar = tk.Button(frame5, text='Guardar', command=self.cambiardatospaciente)
        guardar.pack(side=LEFT, padx=5, pady=5)
        self.apellidoentry.focus()
        self.__ventana.mainloop()

    # Crea ventana de cálculo de IMC
    def imcvista(self):
        self.__imcven = Toplevel()
        self.__imcven.title('IMC')
        self.__imcven.geometry('323x181')
        self.__imcven.resizable(0, 0)
        self.__imc = StringVar()
        self.calculoimc()
        frame1 = tk.Frame(self.__imcven)
        frame1.pack(padx=15, pady=30)
        tk.Label(frame1, text='IMC').grid(column=2, row=4)
        tk.Label(frame1, text='Composición corporal').grid(column=2, row=6)
        imc = tk.Entry(frame1, textvariable=self.__imc, state='readonly')
        imc.grid(column=4, row=4, pady=10, padx=10)
        comcorp = tk.Entry(frame1, textvariable=self.__compcorp, state='readonly')
        comcorp.grid(column=4, row=6, pady=10, padx=10)
        frame2 = tk.Frame(self.__imcven)
        frame2.pack(side=BOTTOM, padx=5, pady=5)
        tk.Button(frame2, text='Volver', command=self.__imcven.destroy).pack(side=TOP, padx=5, pady=5)
        self.__imcven.mainloop()

    # Crea ventana de agregar paciente
    def agregarpvista(self):
        self.__nuevopaciente = Toplevel()
        self.__nuevopaciente.title('Nuevo paciente')
        self.__nuevopaciente.geometry('257x320')
        self.__nuevopaciente.resizable(0, 0)
        self.__nuevopaciente['borderwidth'] = 0
        opts = {'padx': '5', 'pady': '10'}
        frame = ttk.LabelFrame(self.__nuevopaciente, text='Paciente')
        frame.pack(side=TOP, **opts)
        frame1 = tk.Frame(frame)
        frame1.pack(side=LEFT, **opts)
        tk.Label(frame1, text='Apellido').pack(side=TOP, **opts)
        tk.Label(frame1, text='Nombre').pack(side=TOP, **opts)
        tk.Label(frame1, text='Teléfono').pack(side=TOP, **opts)
        tk.Label(frame1, text='Altura').pack(side=TOP, **opts)
        tk.Label(frame1, text='Peso').pack(side=TOP, **opts)
        frame2 = tk.Frame(frame)
        frame2.pack(side=RIGHT, **opts)
        ape = StringVar()
        nom = StringVar()
        tel = StringVar()
        alt = StringVar()
        pes = StringVar()
        self.apellidoentry1 = tk.Entry(frame2, textvariable=ape)
        self.apellidoentry1.pack(side=TOP, **opts)
        self.nombreentry1 = tk.Entry(frame2, textvariable=nom)
        self.nombreentry1.pack(side=TOP, **opts)
        self.telefonoentry1 = tk.Entry(frame2, textvariable=tel)
        self.telefonoentry1.pack(side=TOP, **opts)
        self.alturaentry1 = tk.Entry(frame2, textvariable=alt)
        self.alturaentry1.pack(side=TOP, **opts)
        self.pesoentry1 = tk.Entry(frame2, textvariable=pes)
        self.pesoentry1.pack(side=TOP, **opts)
        frame3 = tk.Frame(self.__nuevopaciente)
        frame3.pack(side=TOP, **opts)
        tk.Button(frame3, text='Confirmar', command=self.agregarpaciente).pack(side=BOTTOM)
        self.apellidoentry.focus()

    # Calcula el IMC
    def calculoimc(self):
        try:
            v1 = int(self.__altura.get()) / 100
            v2 = int((self.__peso.get()))
            res = (v2 / (v1 ** 2))
            self.__imc.set(round(float(res), 2))
            self.comparacion()
        except ValueError:
            messagebox.showerror(title='Error', message='Debe seleccionar un paciente')

    # Compara valor de IMC y guarda la composición corporal
    def comparacion(self):
        self.__compcorp = StringVar()
        valor = float(self.__imc.get())
        if valor < 18.5:
            self.__compcorp.set('Peso inferior al normal')
        elif 18.5 <= valor <= 24.9:
            self.__compcorp.set('Peso normal')
        elif 25.0 <= valor <= 29.9:
            self.__compcorp.set('Peso superior al normal')
        elif valor > 30.0:
            self.__compcorp.set('Obesidad')

    # Agrega paciente a json
    def agregarpaciente(self):
        pac = Objectencoder()
        dic = {'Paciente': {'Apellido': self.apellidoentry1.get(), 'Nombre': self.nombreentry1.get(),
                            'Telefono': self.telefonoentry1.get(), 'Altura': self.alturaentry1.get(),
                            'Peso': self.pesoentry1.get()}}
        try:
            int(dic['Paciente']['Altura'])
            int(dic['Paciente']['Telefono'])
            float(dic['Paciente']['Peso'])
            if dic['Paciente']['Apellido'] != '' and dic['Paciente']['Nombre'] != '':
                dic1 = pac.lectura('Pacientes.json')
                if dic1 is None:
                    dic1 = [dic]
                else:
                    dic1.append(dic)
                pac.guardado(dic1, 'Pacientes.json')
                self.__listbox.delete(0, len(self.__lista))
                self.cargarpacientes()
                self.__nuevopaciente.destroy()
            else:
                self.apellidoentry1.focus()
                messagebox.showerror('Error', 'No puede dejar campos vacíos')
        except ValueError:
            self.telefonoentry1.focus()
            messagebox.showerror('Error', 'Debe ingresar los datos correspondientes')

    # Carga en memoria temporal los pacientes del archivo json
    def cargarpacientes(self):
        obj = Objectencoder()
        self.__datos = obj.lectura('Pacientes.json')
        self.__datos = sorted(self.__datos, key=lambda p: p['Paciente']['Apellido'])
        self.__lista = obj.decoder(self.__datos)
        for i in range(len(self.__lista)):
            nombre = '{}, {}'.format(self.__lista[i].getapellido(), self.__lista[i].getnombre())
            self.__listbox.insert(i, nombre)

    # Realiza la función del botón 'Guardar'
    def cambiardatospaciente(self):
        try:
            i = int(self.__indice.get())
            obj = Objectencoder()
            ape = self.__apellido.get()
            nom = self.__nombre.get()
            tel = self.__telefono.get()
            alt = self.__altura.get()
            pes = self.__peso.get()
            try:
                int(tel)
                int(alt)
                float(pes)
                if type(tel) == int and type(alt) == int and type(pes) == float:
                    self.__lista[i].guardarvalores(ape, nom, tel, alt, pes)
                    dic = {'Paciente': {'Apellido': ape, 'Nombre': nom, 'Telefono': tel, 'Altura': alt, 'Peso': pes}}
                    self.__datos[i] = dic
                    obj.guardado(self.__datos, 'Pacientes.json')
                    self.__listbox.delete(0, len(self.__lista))
                    self.cargarpacientes()
            except ValueError:
                messagebox.showerror('Error', 'Debe ingresar los datos correspondientes')
        except ValueError:
            messagebox.showerror('Error', 'Seleccione un paciente')

    # Realiza la función del botón 'Borrar'
    def borrarpaciente(self):
        if messagebox.askokcancel('Borrar Paciente', '¿Desea borrar TODOS los datos del paciente?'):
            try:
                self.__listbox.delete(int(self.__indice.get()))
                self.__lista.pop(int(self.__indice.get()))
                self.__datos.pop(int(self.__indice.get()))
                obj = Objectencoder()
                obj.guardado(self.__datos, 'Pacientes.json')
                self.__apellido.set('')
                self.__nombre.set('')
                self.__telefono.set('')
                self.__altura.set('')
                self.__peso.set('')
            except ValueError:
                messagebox.showerror('Error', 'Seleccione un paciente')

    # Vincula el doble click
    def dobleclick(self, callback):
        handler = lambda _: callback(self.__listbox.curselection()[0])
        self.__listbox.bind('<Double-Button-1>', handler)

    # Carga los datos de un paciente en el formulario
    def ponercontacto(self, i):
        self.__indice.set(i)
        self.__apellido.set(self.__lista[i].getapellido())
        self.__nombre.set(self.__lista[i].getnombre())
        self.__telefono.set(self.__lista[i].gettelefono())
        self.__altura.set(self.__lista[i].getaltura())
        self.__peso.set(self.__lista[i].getpeso())

