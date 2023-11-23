import json
from deuda import deuda

class Usuario_:
    def __init__(self, nombre, contraseña, monto):
        self.nombre = nombre
        self.contraseña = contraseña
        self.monto = monto
        self.tam=0
        self.historial=[]
        self.deudas=[]
        self.quiero=False

    def __str__(self):
        return f'nombre: {self.nombre} monto: {self.monto}'

    def setQ(self,q):

        self.quiero=q

    def getQ(self):

        return self.quiero

    def revaluarDeudas(self):

        for deuda in self.deudas:

            deuda.setMeses(-1)

            deuda.aumentarDeuda()

    def agregarHistorial(self,mensaje):

        self.historial.append(mensaje)

    def getMonto(self):

        return self.monto

    def getName(self):
        
        return self.nombre

    def setMonto(self,valor):

        self.monto=valor

    def endeudarse(self,aquien,porcentaje):

        resp3=int(input('cuanto será el préstamo: '))

        resp4=int(input('meses a poner la deuda: '))


        if resp3+(resp3*porcentaje)>aquien.monto:

            print(f'error, el grupo {aquien.nombre} no tiene dinero suficiente')

            return

        self.monto+=resp3

        deuda1=resp3+(resp3*porcentaje)

        self.deudas.append(deuda(deuda1,resp4,aquien))

        aquien.monto-=deuda1

        self.historial.append(f' una deuda del {deuda1} a {resp4} meses con el grupo {aquien.nombre}')

    def pagar(self):

        cont=0

        for deudas in self.deudas:

            print(f'{cont}.{deudas}')

            cont+=1

        resp=int(input('cual deuda vas a pagar:'))

        if self.monto<self.deudas[resp].deuda:

            print('dinero insuficiente en tu monto')

        else:

            deuda1=self.deudas[resp].deuda

            self.monto=self.monto-self.deudas[resp].deuda

            self.deudas[resp].aquien.setMonto((self.deudas[resp].aquien.getMonto()+self.deudas[resp].deuda)-((self.deudas[resp].aquien.getMonto()+self.deudas[resp].deuda)*0.001))

            #self.deudas[resp].aquien.monto+=self.deudas[resp].deuda

            self.deudas.pop(resp)

            self.historial.append(f' deuda del {deuda1} a {resp4} meses con el grupo {aquien.nombre} pagada')


    def verhistorial(self):

        for acto in self.historial:

            print(acto)

    def to_dict(self):
        # Convierte la instancia de Usuario a un diccionario
        return {
            'nombre': self.nombre,
            'contraseña': self.contraseña,
            'monto': self.monto,
            'tam': self.tam
        }

    @classmethod
    def from_dict(cls, usuario_dict):
        # Crea una instancia de Usuario desde un diccionario
        return cls(
            usuario_dict['nombre'],
            usuario_dict['contraseña'],
            usuario_dict['monto'],
            usuario_dict['tam']
        )

    