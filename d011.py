class Vehiculo():

    def __init__(self, color,longitud_metros,ruedas):
        self.color = color
        self.longitud_metros = longitud_metros
        self.metros = ruedas
            
    #metodos
    def arrancar(self):
        print("El vehiculo ha arrancado")
    def detener(self):
        print("parar el motor")
        
vehiculo1=Vehiculo("rojo",4,4)
vehiculo2=Vehiculo("verde",4,8)

#agregamos un atributo que no esta en la clase
vehiculo2.material_aleron = "Fibra de carbono"

vehiculo1.arrancar()
vehiculo1.detener()

