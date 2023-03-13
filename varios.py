
""" a=12
b=5
print ("a dividido b es:", a/b , " y el resto es " , a%b )
#/* area de un triangulo=basexaltura  *\
base= float(input("ingresar base:"))
h=float(input("Ingrese la altura: " ))  
resultado=base*h/2
print("Resultado:") ,resultado
 """
# strings
txto= ['1','2','4']
separador="-"
print (separador.join(txto))

frases= "Meses: {}, {},{}".format("enero", "febrero","marzo")
print(frases)

frases= "Meses: {1}, {0},{2}".format("enero", "febrero","marzo")
print(frases)

frases= "Meses: {uno}, {dos},{tres}".format(tres="enero", uno="febrero",dos="marzo")
print(frases)

#f-strings

nombre="gustavo"
edad=50
saludo= f"hola, me llamo {nombre} y tengo {edad} años"
print(saludo)

#conversion de tipos
alumno="pepe"
nota=7.8
resultado= f"el alumno " + alumno + " tiene una calificacion de " + str(nota) + "."
print(resultado)


# metodos de cadena
"""  
frase="aprendiendo a programar Python"
print(frase)
print(frase[2])
print(frase[-2])
print(frase[3:6])
print(frase[5:])
print(frase[:10])
print(frase.upper )
print(frase.title)
print(frase.lower)
print(frase.capitalize)
print(frase.translate)

"""
nombre="Michael Jordan"
edad="32"
media_puntos=78.2
juega=False

frase= f"jugador" + nombre + " de " + edad + "años tiene un promedio de " + str(media_puntos) + " y actualmente juega " + str(juega)
for i in range (7):
    print ( str(i) ) 

for i in range (5,10):
    print ( str(i) + " " +  frase) 

for i in range (10, 100, 10):
    print ( str(i) + " " +  frase) 

alumnos = ["juan","pedro", "ana","luciana","ariel"]
for i in range (len(alumnos)):
    print (alumnos[i])
    
x = int(input("ingrese un numero"))
while int(x) != 99:
    if x < 0:
        print ("es un numero negativo")
    elif x == 0:
        print ("es un nro. 0")
    elif x > 0:
        print ("es un nro. positivo")
    x = int(input("ingrese un numero"))

# ingresar dos numeros y calcular la suma de los nuro.del intervalo
x=0
y=0
z=0
acum=0
while x >= y:
    x= int(input("Ingrese el nro. de inicio: "))
    y= int(input("Ingrese el nro. de fin : "))
    if x < y:
        for z in range(x,y):
            acum=acum + (z+x)
    else:
        print("Ingrese un intervalo correcto")
    print( f"La suma de los nros. entre {x}  y {y} es {z}")

