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
    def mostrar_info(self):
        print(f"Vehiculo de color {self.color}")
        
vehiculo1=Vehiculo("rojo",4,4)
vehiculo2=Vehiculo("verde",4,8)

#agregamos un atributo que no esta en la clase


vehiculo2.material_aleron = "Fibra de carbono"

vehiculo1.arrancar()
vehiculo1.detener()

vehiculo2.arrancar()
vehiculo1.mostrar_info()


class Motocicleta():
    #atributo de clase
    estado ="nueva"
    motor = False
    
    # atributos
    def __init__(self, color, matricula,combustible_litros, numero_ruedas,marca, modelo, fecha_fabricacion,peso):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.peso = peso
        self.nombre_completo= f"{self.marca} , {self.matricula}"
    # metodos
    def detener_motor(self):
        if self.motor:
            self.motor=False
            print("Se detuvo el motor")
        else:
            print("el motor ya esta detenido")
    
    def encender_motor(self):
        if self.motor:
            print("el motor ya estaba encendido")
        else:
            self.motor =True
            print ("el motor fue encendido")
            
moto_chito = Motocicleta("rojo","aazz",10,2,"Honda", "zyx","01/01/23",50)
    
moto_guti = Motocicleta(marca="nissan", modelo="1987", 
                        fecha_fabricacion="01/12/22",
                        peso="80",color="celeste", 
                        matricula="asdd",
                        combustible_litros=20, 
                        numero_ruedas=2)
moto_guti.valor=28000

print(moto_guti.valor)
print(moto_chito.nombre_completo)
        
moto_chito.detener_motor()

