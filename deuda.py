class deuda:

    def __init__(self,deuda,meses,aquien):

        self.deuda=deuda
        self.meses=meses
        self.aquien=aquien

    def __str__(self):

        return f'deuda total: {self.deuda} para pagar dentro de {self.meses} meses'

    def setMeses(self,valor):

        self.meses+=valor

    def aumentarDeuda(self):

        if self.meses<0:

            self.deuda=self.deuda+(self.deuda*0.1)

        else:

            print(f" \ntodavía puedes pagar tu deuda sin cargos con {self.aquien} que tiene un valor de {self.deuda}, ojo o te vamos a quitar tu casa :)")

