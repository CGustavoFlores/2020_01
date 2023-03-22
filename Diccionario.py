import datetime

YoSoy="Gustavo Flores"
print("Hi, Me names is " + YoSoy)
<<<<<<< HEAD
=======
print("Hi, Me names is " + YoSoy)

a1=21
a2=30.4
print(type(a1))
print(type(a2))

# funcionest

def gflow_te_saluda(nombre, edad):
    print(f"Hola!! {nombre} !! Gflow te saluda !. Tu edad es {edad}")

gflow_te_saluda("Luciana",40)

nombre= input("Introduzca su nombre, por favor: ")
nacimiento = input("Ingrese en año nacio: ")
anioactual=datetime.datetime.now()
an = anioactual.year
edad= int(an) - int(nacimiento)

print("funcion year" ,datetime.datetime.year)

gflow_te_saluda(nombre,edad)
>>>>>>> c218440c8b2314f1bc3563e0313434f0c1423ee5

