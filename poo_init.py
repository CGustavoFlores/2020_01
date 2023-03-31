class SportInfo:
    """mostrar informacion de un deporte"""
    def __init__(self, name):
        print("Estamos creando un objeto")
        self.name= name
        
    def __del__(self):
        print("estamos destruyendo un objeto: {}"
            .format(self.__class__.__name__))
        
    def __str__(self):
        return "Soy el deporte {}".format(self.name)

#añadimos objetos asociados a esta clase
run = SportInfo("Correr")
print(run.name) #correr
print(run.__doc__)

del run


swim = SportInfo("Nadar")
print(swim.name)
print(swim.__doc__)

del swim

print("Final")
