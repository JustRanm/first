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
  print("Esta platica se salvo de que se le robaran: ", C , 
       "Por lo que dejeme decirle socio que no va a ganar ni m: ")
elif C>100000 and C<1000000:
  print("Esta platica se salvo de que se le robaran: ", C , "Por lo que dejeme decirle socio que le sale rentable: ")
elif C>1000000:
        print("Esta platica se salvo de que se le robaran: ",C, " Por lo          que dejeme decirle socio que fue buena inversion:" )

'''
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