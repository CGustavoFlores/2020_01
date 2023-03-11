
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
