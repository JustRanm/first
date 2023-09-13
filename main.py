'''
#Hola bro
#Ejercicio uno

print("Que lo que")

#Ejercion dos
Universo=("hola mundo")
print(Universo)

#Ejercicio 3 
nombre=input("QUE LO QUE BRO, ¿CUAL ES SU NOMBRE?: ")
print("Un gusto panita " + nombre + " :3")


#Ejercicio 4
print(((3+2)/(2*5))**2)

#ejercicio  5
horas=float(input("Cuantas horas laburo socio: "))
precio=float(input("Cuanto le dan por hora: "))
operacion=str(horas*precio)
print("Usted mi bro gana " + operacion)

#Tambien se puede usar la coma en vez del str

#Ejercicio 6
Numero=int(input("Introdusca entero porsitivo: "))
print("La respuesta es" , Numero*(Numero+1)/2)

#Ejercio 7

P=float(input("Cuantos kg se carga: "))
E=float(input("Que tan alto es bro, en metros: "))
Calculo=round(P/E**2 , 2) 
print("Su indice de masa muscular es" , Calculo)

#Ejercicio 8
N=int(input("Ponga un numero entero: "))
M=int(input("Ahora, vuelva y ponga otro entero: "))
Division=round(N/M,2)
C=N//M
R=N%M
print("La division da: ",Division,", Su conciente es: ",C,"y Su residuo es: ",R,)
print("""\

    ⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀
⠀⠀⠀ ⣴⠿⠏⠀⠀⠀⠀⠀⠀⢳⡀⠀⡏⠀⠀⠀⠀⠀⢷
⠀⠀⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀⠀ ⡇
⠀⠀⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿⠀⣸⠀⠀OK⠀ ⡇
⠀⠀⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀⣿⠀⢹⠀⠀⠀⠀⠀ ⡇
⠀⠀⠙⢿⣯⠄⠀⠀⠀⢀⡀⠀⠀⡿⠀⠀⡇⠀⠀⠀⠀⡼
⠀⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀⠀⠘⠤⣄⣠⠞⠀
⠀⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀
⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀
⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀⠀⣄⢸⠀⠀⠀⠀⠀⠀
⣿⣿⣧⣀⣿.........⣀⣰⣏⣘⣆⣀""")  

                        



#Ejercicio 5
I=float(input("Cuanta platica va a invertir: "))
i=float(input("Cual es el porcentaje de interes mi rei: "))
n=float(input("De cuantos años hablamos: "))
Formula=I*(i/100+1)
print("Papi usted de va a ganar una buena platica de:",Formula )

#EJERCICIO 10
p=int(input("Numero de payasos: "))
m=int(input("Numero de muñecas: "))
Calculo=(p*112)+(m*75)
print("El peso total del paquete es : ",Calculo,"gr")

#Ejercicio 11
platica=float(input("Cuanta platica va a invertir: "))
o1= (platica*0.04)
o2= (platica*0.04*2)
o3= (platica*0.04*3)
suma= o1+o2+o3 
round(suma,2)
print("En un año usted ganara: ", o1) 
print("En dos años usted ganaria: ", o2,)
print( "En tres años estaria recibiendo: " ,o3)
print("Por lo que al final, usted mi pana estaria ahorrando un total de: ", suma)


#Ejercicio 12

Panes=int(input("Cuantos panes viejos a vendido hoy: "))
dia=Panes*3000
Ndia=(3000*0.4)*Panes
print("Si fueran frescos le costaria: ", dia, ". Pero como no son del dia le sale el gangaso a: ", Ndia)


#iF
horas=int(input("Cuantas horas ah laburado: "))
costo=float(input("Cuanta platica gana por hora: "))
if horas>47:
    print((horas*costo*0.1)+(horas*costo),("esto es lo que gana con el bono bro"))
elif horas>30 and horas<47:
    print((horas*costo*0.05)+(horas*costo),"Entonces se llevara esta platica")

else :
    print(horas*costo, "esta platica es la que se gans sin bono")  
    
#Ejercicio 1
N=int(input("Ingrese cualquier entero positivo panita: "))
ope=N*(N+1)/2
if ope>20:
      print(ope,"Esta como grandesito ese numero")
else:
    print(ope,"No tan grande, igual recuerda, EL TAMAÑO NO LO ES TODO")
  
#ejercicio 2
N=int(input("Introdusca un numero enstero bro: "))
M=int(input("Vuelva a repetir el paso anterior :3 : "))
d=N/M
C=float(N//M)
R=N%M
if C<1:
  print("La division es: ",d," El cociente le daria; ",C," El resto seria: ",R, "  y Como C es menor a uno. el divisor es mayor al dividiendo " )
elif C>1:
  print("La division es: ",d," El cociente le daria; ",C," El resto seria: ",R," y Como C es mayor a 1, el divisor es mayor al dividiendo ")
elif C==1:
  print("La division es: ",d," El cociente le daria; ",C," El resto seria: ",R, " y Como C es igual a uno, el divisor es igual al dividiendo")
  
#Ejercicio 3
Ci=float(input("Cuanta platica esta dispuesto a dejar que le roben: "))
I= float(input("A cuanto interes va dejar que le roben: ")) 
N= int(input("A cuantos año va a poner que le roben: "))
C= Ci*((I/100)+1)**N
if C<100000:
  print("Esta platica se salvo de que se le robaran: ", C     ,"Por lo que dejeme decirle socio que no va a ganar         ni m: ")
elif C>100000 and C<1000000:
  print("Esta platica se salvo de que se le robaran: ", C , "Por lo que dejeme decirle socio que le sale rentable: ")
elif C>1000000:
        print("Esta platica se salvo de que se le robaran: ",C, " Por lo          que dejeme decirle socio que fue buena inversion:" )


#Ejercio 4

P=int(input("Cuantos payasitos va a llevar de contrabando: "))
M=int(input("Cuantas muñecas va a llevar de contrabando: "))
O1=(P*112)/1000
O2=(M*75)/1000
P=O1+O2
if P>3000:
    X=input("¿Desea contrabandiar?: ")
    if X =="si":
      print("Se a contrabandiado con exito")
    if X =="no":
      print("No se contrabandio")
else:
 print("No alcanza para contrbandiar ese peso: ", P)
 
#Ejercicio 5

C=float(input("Cuanta platita va a poner a trabajar: "))
if C>0 and C<1000000:
    I=2
    B1=C*(1+I/100)
    B2=B1*(1+I/100)
    B3=B2*(1+I/100)
    a=round(B1,2)
    b=round(B2,2)
    c=round(B3,2)
    s=B1+B2+B3
    print("Ustede se gano en el año 1: ",a,"En el año 2:       ",b,"y ya en el ultimo año gano: ",c, "Por lo que         dejeme decirle socio, que su merced gano en total:         ", round(s,2))
elif C>=1000000 and C<=2000000:
     I=5
     B1=C*(1+I/100)
     B2=B1*(1+I/100)
     B3=B2*(1+I/100) 
     a=round(B1,2)
     b=round(B2,2)
     c=round(B3,2)
     s=B1+B2+B3
     print("Usted gano en el año 1: ", a," En el año 2: ",b," y ya en el ultimo año gano: ",c, " Por lo que dejeme dcirle socio que su merced gano en total: ",round(s,2))
elif C>2000000:
  I=7
  B1=C*(1+I/100)
  B2=B1*(1+I/100)
  B3=B2*(1+I/100)
   a=round(B1,2)
   b=round(B2,2)
   c=round(B3,2)
   s=B1+B2+B3
  
  print("Ustede se gano en el año 1: ",a,"En el año 2:       ",b,"y ya en el ultimo año gano: ",c, "Por lo que    dejeme decirle socio, que su merced gano en total: ",       round(s,2))
  
  

  #Ejercicio 6
Panes=int(input("Cuantos panes viejos a vendido hoy: "))
dia=Panes*3000
Ndia=(3000*0.4)*Panes
print("Si fueran frescos le costaria: ", dia, ". Pero como no son del dia le sale el gangaso a: ", Ndia)
P=int(input("Cuantos paens frescos va comprar mi so: "))
if P>15:
    I=40
    O=3000*(I/100)*P
    print("Dejeme descirle que al por mayor le sale a: ",O)
elif P<15 and P>10:
    I=30
    O=3000*(I/100)*P
    print("No son tantos aun asi le sale a un buen precio de: ",O)
elif P<10:
    I=10
    O=3000*(I/100)*P
    print("Uf no es un gran descuento pero es mejor que   nada, los pancitos le salen: ",O)
  

#Ejercicios de ffunciones
#Ejercico 1
a=int(input("Ingrese un numero para sumar: " ))
b=int(input("Ingrese ahora otro numero: "))
def suma(n1,n2):
  sum=(n2+n1)
  print("SU SUMA: ",sum)
suma(a,b)

#Ejercio 3
a=int(input("Ingrese un numero para resta: " ))
b=int(input("Ingrese ahora otro numero: "))
def resta(n1,n2):
  sum=(n2-n1)
  print("SU RESTA ES: ",sum)
resta(a,b)

#Ejercicio 4
a=int(input("Ingrese un numero para multiplicar: " ))
b=int(input("Ingrese ahora otro numero: "))
def multi(n1,n2):
  mul=(n2*n1)
  print("SU MULTIPLICION ES: ", mul)
multi(a,b)


#Ejercicio 5
a=int(input("Ingrese un numero para dividir: " ))
b=int(input("Ingrese ahora otro numero: "))

def divi(n1,n2):
  if n1==0:
    print("No sea webon no se puede dividir por cer -_-")
  else:
    div=(n1/n2)
    print("SU DIVISION ES: ", div)
divi(a,b)

a=float(input("Ingrese numero para operar: "))
b=float(input("Ingrese otro numero para operar: "))
Menu=int(input("Este es su menu de operaciones, 1 para suma, 2 para resta, 3 para multiplicion y 4 para dividir, eliga que quiere socio: "))
def suma(n1,n2):
  sum=(n2+n1)
  print("SU SUMA: ",sum)
def resta(n1,n2):
  rest=(n2-n1)
  print("SU RESTA ES: ",rest)
def multi(n1,n2):
  mul=(n2*n1)
  print("SU MULTIPLICION ES: ", mul)
def divi(n1,n2):
  if n1==0:
    print("No sea webon no se puede dividir por cer -_-")
  else:
    div=(n1/n2)
    print("SU DIVISION ES: ", round(div,2))
if Menu==1:
  suma(a,b)
elif Menu==2:
  resta(a,b)
elif Menu==3:
  multi(a,b)
elif Menu==4:
  divi(a,b)
  
  
#EJERCICIO 6
def interses(inv):
  d=inv

  if (d>0 and d<1000000):
    return 2
  elif (d>=1000000 and d<20000000):
    return 5
  else:
    return 7 

def balance(int, inv):
  i=int
  p=inv

  return round((p*(1+(i/100))),2)

def ahorro():
  #inversion, intereses, b1, b2, b3 = 0.0

  inversion= float(input("Ingrese a la platica que va invertir: "))

  intereses=interses(inversion)

  b1=balance(intereses, inversion)
  b2=balance(intereses, b1)
  b3=balance(intereses, b2)

  print("El primer año gano una platita de: ",b1 ,"En el segundo año gano una platica de: ", b2 ,"Ya para el tercer año gano una platita de ", b3)


ahorro()


#EJERCICIOS DE FUNCIONES
#EJERCICIO 1

def triangulo ():
  a=float(input("Ingrese la altura del triangulo: "))
  b=float(input("Ingrese la base: "))
  At=(a*b)/2
  print("El area del triangulo es: "+str(At))

def cuadrado ():
  c=float(input("Ingrese un lado: "))
  d=float(input("Ingrese el siguiente lado: "))
  AC=c*d
  print("El area del cuadrado es: " + str(AC))

def circulo ():
  Pi=3.14169
  r=float(input("Ingrese el radio del circulo: "))
  AO=Pi*(r)**2
  print("El area del circulo es: " + str(AO))

def pentagono():
  perimetro=float(input("Cual es el perimetro del pentagono: "))
  apotema=float(input("Ingrese la apotema: "))
  AP=(perimetro*apotema)/2  
  print("Area de el pantagono es: " + str(AP))

def rombo():
  DiagonalM=float(input("Ingrese la diagonal mayor: "))
  Diagonalm=float(input("Ingrese la diagonal menor: "))
  AR= (DiagonalM * Diagonalm)/2
  print("El area del rombo es: " + str(AR))
  
def AreasFIG ():
  Eleccion=int(input("""Que area desea sacar : 
                     1) Triangulo
                     2) Cuadrado
                     3) Circulo 
                     4) Pentagono
                     5) Rombo
                     : """))
  if Eleccion==1:
    triangulo()
  elif Eleccion==2:
    cuadrado()
  elif Eleccion==3:
    circulo()
  elif Eleccion==4:
    pentagono()
  elif Eleccion==5:
    rombo()
AreasFIG()      

 
def maximo(a,b):
  if a>b:
    return a
  else:
    return b

def minimo(a,b):
  if a<b:
    return a
  else:
    return b

#programa principal
x=int(input("un numero: "))
y=int(input("otro numero: "))
print(maximo(x-3, minimo(x+2, y-5)))
'''
#EJercicio 4
"""
def haiyaki (C1):
    return C1*(0.1)

def naruto (C2):
    return C2*(0.05)
    

def Yu (c3):
  return c3*(0.2)

def homcenter():
  costo=float(input("A cuanto le sale el equipito mi bro: "))
  marca=str(input("Es marca NOSY mano?: "))

  if marca=="si" and costo>2000000:
    print("El paralantico le saldra en ", naruto(costo)-haiyaki(costo)+Yu(costo)+costo)
    
  elif marca=="no" and  costo>2000000:
    print("El paralantico le saldra en ", haiyaki(costo)+Yu(costo)+costo)
    
  elif marca=="si" and costo<2000000:
     print("El paralantico le saldra en ", naruto(costo)+Yu(costo)+costo)

  elif marca=="no" and costo<2000000:
     print("El paralantico le saldra en ", Yu(costo)+costo)

  print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀   ⢠⠞⠉⠙⠲⡀⠀
⠀⠀⠀⣴⠿⠏⠀⠀⠀⠀⠀⠀⢳⡀⠀   ⡏⠀⠀⠀⠀⠀   ⢷
⠀⠀⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀⠀      ⡇
⠀⠀⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿⠀⣸⠀⠀Que lo    ⡇
⠀⠀⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀⣿⠀⢹⠀⠀⠀ disfrute ⡇
⠀⠀⠙⢿⣯⠄⠀⠀⠀⢀⡀⠀⠀⡿⠀⠀⡇⠀⠀⠀⠀       ⡼
⠀⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀⠀⠘⠤         ⠞⠀
⠀⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠘⠤.....⠘  ⠀⠀⠀⠀
⠀⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀
⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀
⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀⠀⣄⢸⠀⠀⠀⠀⠀⠀
⣿⣿⣧⣀⣿.........⣀⣰⣏⣘⣆⣀⠀⠀''')
    
  

homcenter()

"""
'''
#Ciclos iteractivos, WHILE
A = 0
while A < 10:
  print(A)
  A = A + 1
'''
#Calculadora con ciclos
"""
  #Ejercico 1
def suma():
  n1=int(input("Ingrese un numero para sumar: " ))
  n2=int(input("Ingrese ahora otro numero: "))
  sum=(n2+n1)
  print("SU SUMA: ",sum)


#Ejercio 3
def resta():
  n1=int(input("Ingrese un numero para resta: " ))
  n2=int(input("Ingrese ahora otro numero: "))
  sum=(n2-n1)
  print("SU RESTA ES: ",sum)


#Ejercicio 4
def multi():
  n1 = int(input("Ingrese un numero para multiplicar: " ))
  n2 = int(input("Ingrese ahora otro numero: "))

  mul = (n2*n1)
  print("SU MULTIPLICION ES: ", mul)



#Ejercicio 5
def divi():
  n1=  int(input("Ingrese un numero para dividir: " ))
  n2 = int(input("Ingrese ahora otro numero: "))
  if n1==0:
    print("No sea webon no se puede dividir por cer -_-")
  else:
    div=(n1/n2)
    print("SU DIVISION ES: ", div)

def menu():
   print('''Este es su menu de operaciones, 
   1) para suma
   2) para resta 
   3) para multiplicion
   4) para dividir  
   5) si ya no desea operar: ''')

def calculadora():
  menu()
  Menu=0
  while Menu != 5:
    Menu=int(input("Seleccione lo que desea hacer: "))
 
    if Menu==1:
      suma()
    elif Menu==2:
      resta()
    elif Menu==3:
      multi()
    elif Menu==4:
      divi()
    elif Menu==5:
      print("Gracias por usar nuestro producto :3")
    else:
      print("Opcion no establecidad, vuelva a intentar")

calculadora()
"""

#Ejercicio 2 de ciclos
"""
def tiendita():
  valor=1
  suma=0
  while valor != 0:
    valor = float(input("Ingrese el valor del producto: "))
    suma = suma + valor 
  
    if valor < 0:
        print("Valor no valido vuelva a ingresar el valor de la comprar")
    elif suma > 1000000 and valor==0:
       suma= suma-(suma*0.1)
       print("Le valor de su compra es: ",suma)
      
    elif valor==0:
        print("Le valor de su compra es: ",suma)
       
tiendita()
"""

#BUcle FOR
'''
for santiago in range(1,5,2):
  print(santiago)
'''
#Ejercicio 1
"""
import random
Random = random.randint(1,100)
def adivinacion():
  Eleccion=0
  while Random!=Eleccion:
    Eleccion= int(input("Intente adivinar el numero del 1 al 100: "))
    if Random > Eleccion:
      print("Es mayor")
    elif Random < Eleccion:
      print("Es menor")
    elif Random == Eleccion:
      print("Felicitaciones has adivinado")

adivinacion()
"""
#Segunda manera de hacer el Ejercio 1
"""
import random
def adivina():
  numero_secreto = random.randint(1,100)
  adivinando = False

  while not adivinando:
    intento = int(input("Adivine el numero: "))
    if intento == numero_secreto:
      print("CORRECTO has a adivinado el numero")
      adivinando = True
    elif intento < numero_secreto:
      print("El numero es mayor")
    else:
      print("El numero es menor")

adivina()
"""
#Ejercicio 2 con for
'''
def Tabla_multiplos():
  numero = int(input("Ingrese un numero para saber su tabla: "))
  for multi in range(1,11):
    Tabla = multi*numero
    print("Su tabla es: ",Tabla)
Tabla_multiplos()
'''
#Ejercicio 3 con FOR Factorial

def calulador_factoriales():
  Numero = int(input("Ingrese el numero factorial: "))
  Multiplicar = 1
  
  for factorial in range (1,Numero + 1):
    Multiplicar *= factorial
    

  print("El resultado es: ",Multiplicar)
calulador_factoriales()
  