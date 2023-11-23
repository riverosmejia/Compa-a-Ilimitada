from user import Usuario_
from grupo import grupo

class sist:

    def __init__(self):

        self.UsuarioActual=None
        self.ListaU=[]
        self.GrupoActual=None
        self.ListaG=[]

    def seleccionarGrupo(self,name):

        resp1=input('dime el grupo al que quieres seleccionar: ')

        for grupos in self.ListaG:

            print(grupos.YaEsta(name))

            if grupos.YaEsta(name):

                self.GrupoActual=grupos

                return

    def iniciarSesion(self,name,cont):

        for users in self.ListaU:

            if users.nombre==name and users.contraseña==cont:

                self.UsuarioActual=users

                print(f'Bienvenido {self.UsuarioActual.getName()}!')

                return

        print("El nombre de usuario o contraseña no son correctos, intentalo de nuevo")

    def Arranque(self):

        terminar=False
        
        contadorM=int(0)

        while terminar is not True:

            #print(self.GrupoActual)

            print(f'mes: {contadorM}')

            #contadorM+=1

            resp=0

            if self.UsuarioActual is not None:

                print(f'monto actual: {self.UsuarioActual.getMonto()}')

            if self.GrupoActual is None:

                resp=int(input("1- iniciar sesión\n2- cerrar sesión\n3- crear usuario\n4- ver usuarios existentes\n5- ver grupos existentes\n6- acceder a grupo\n7- crear grupo\n8. seleccionar grupo\n9- pedir préstamo\n10- agregar dinero\n11- ver deudas\n12- pagar deudas\n13- ver historial completo14\n14. pasar mes\n15- salir\nR/="))

            else:

                resp=int(input("1- salir\n2- invitar personas\n3- salirse del grupo\n4- pedir prestamo interno\n5- disolver grupoR/="))

            if self.GrupoActual is None:

                if resp==1:

                    nameI=input("dame el nombre del usuario: ")

                    contI=input("dame la constraseña del usuario: ")

                    self.iniciarSesion(nameI,contI)

                if resp==2:

                    if self.UsuarioActual is not None:

                        self.UsuarioActual=None

                        print('sesión cerrada correctamente!')

                    else:

                        print('no hay sesión iniciada actualmente')

                elif resp==3:

                    name=input("dame el nombre del usuario: ")

                    cont=input("dame la constraseña del usuario: ")

                    mont=int(input("dame el monto de dinero del usuario: "))

                    usuarioN=Usuario_(name,cont,mont)

                    self.ListaU.append(usuarioN)

                elif resp==4:

                    if self.UsuarioActual is not None:

                        for users in self.ListaU:

                            print(users)       

                    else:

                        print('primero inicia sesión')

                elif resp == 5:

                    if self.UsuarioActual is not None:

                        for groups in self.ListaG:

                            print(groups)     

                    else:

                        print('primero inicia sesión')


                elif resp == 6:

                    if self.UsuarioActual is not None:

                        name=input("dame el nombre del grupo: ")

                        for groups in self.ListaG:

                            if groups.nombre==name:

                                groups.agregarUser(self.UsuarioActual)

                                print(f'usuarios actuales: {grupos.usuarios}')
                    
                    else:

                        print('primero inicia sesión')

                elif resp==7:

                    name=input("dame el nombre del grupo: ")

                    mont=int(input("dame el monto de dinero que ingresarás al grupo: "))

                    if self.UsuarioActual is not None:

                        if mont > self.UsuarioActual.getMonto():

                            print("error, no puedes ingresar un monto mayor al que tienes")

                        else:

                            GrupoN=grupo(name,2,mont)

                            GrupoN.agregarUser(self.UsuarioActual)

                            self.UsuarioActual.setMonto(self.UsuarioActual.getMonto()-GrupoN.getMonto())

                            self.ListaG.append(GrupoN)

                            self.UsuarioActual.agregarHistorial(f'se ha creado un grupo y se ha invertido {mont}')

                            #self.UsuarioActual.historial.append(f'se ha creado un grupo y se ha invertido {mont}')


                    else:

                        print('primero inicia sesión')

                if self.GrupoActual is None:

                    if resp == 8:

                        self.seleccionarGrupo(self.UsuarioActual.nombre)

                if resp == 9:

                    resp2=input('dame el nombre del grupo a pedir prestamo: ')

                    for groups in self.ListaG:

                            if groups.nombre==resp2:

                                if groups.YaEsta(resp2):

                                    print('porcentaje de deuda 3%')

                                    porcentaje=0.03

                                else:

                                    print('porcentaje de deuda 5%')

                                    porcentaje=0.05

                                if self.UsuarioActual is not None:

                                    self.UsuarioActual.endeudarse(groups,porcentaje)

                elif resp==10 and self.GrupoActual is None:

                    if self.UsuarioActual is not None:

                        ad=int(input('cuanto dinero vas a agregar'))

                        self.UsuarioActual.setMonto(self.UsuarioActual.getMonto()+ad)

                        #self.UsuarioActual.monto=self.UsuarioActual.monto+ad

                    else:

                        print('primero inicia sesión')

                elif resp == 11:

                    for deudas in self.UsuarioActual.deudas:

                        print(deudas)

                elif resp ==12:

                    self.UsuarioActual.pagar()

                elif resp == (12+1):

                    if self.UsuarioActual is not None:

                        self.UsuarioActual.verhistorial()

                elif resp == 14:

                    if self.UsuarioActual is not None:

                        self.UsuarioActual.revaluarDeudas()

                    contadorM+=1

                elif resp == 15:

                    terminar=True

            if self.GrupoActual is not None:

                if resp == 10:

                    None


