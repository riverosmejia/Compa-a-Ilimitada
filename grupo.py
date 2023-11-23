
from user import Usuario_

class grupo:

    def __init__(self,nombre,tamaño,monto):
    
        self.nombre=nombre
        self.maximo=tamaño
        self.tamaño=0
        self.monto=monto
        self.usuarios=[]

    def __str__(self):

        return f'nombre del grupo: {self.nombre} monto del grupo: {self.monto} usuarios actuales: {self.tamaño+1} '

    def disolver(self):

        for user in self.usuarios:

            if user.quiero==False:

                return False

        return True

    def setMonto(self,nuevo):

        self.monto=nuevo

    def getMonto(self):

        return self.monto

    def agregarUser(self, usuario):

        if self.tamaño != self.maximo:

            print(usuario.tam)

            if usuario.tam <3:

                if self.YaEsta(usuario.nombre) is not True:

                    self.usuarios.append(usuario.nombre)

                    self.tamaño+=1

                    usuario.tam+=1

                else:

                    print('ya estas en el grupo, vuelve a intentarlo')

            else: 

                print('te has unido a un número de grupos suficientes')

        else:

            print("el grupo está lleno")

    def YaEsta(self, name):

        for users in self.usuarios:

            if users==name:

                return True

        return False
            