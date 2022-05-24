from __future__ import division
import sys 

n1 = 0
n2 = 0

menú = """
1.-Suma
2.-Resta
3.-Multiplicación
4.-División 
5.-Potencia 
6.-Raiz 
7.-Salir
"""

def Suma():
    print("Ingrese primer sumando: ")
    n1 = float(input()) 
    print("Ingrese segundo sumando: ")
    n2 = float(input())
    print("El resultado es: ", n1 + n2)

def Resta():
    print("Ingrese el minuendo: ")
    n1 = float(input())
    print("Ingrese el sustraendo: ")
    n2 = float(input())
    print("El resultado es: ", n1 - n2)

def Multiplicación():
     print("Ingrese el primer coeficiente: ")
     n1 = float(input())
     print("Ingrese el segundo coeficiente: ") 
     n2 = float(input())
     print("El resultado es: ", n1 * n2)  

def Divisón():
    print("Ingrese el dividendo: ")
    n1 = float(input())
    print("Ingrese el divisior: ")
    n2 = float(input())
    print("El resultado es: ", n1 / n2 )

def Potencia():
    print("Ingrese la base: ")
    n1 = float(input())
    print("Ingrese el exponente: ")
    n2 = float(input())
    print("El resultado es: ", n1 ** n2)

def Raiz():
    print("Ingrese el radicando: ")
    n1 = float(input())
    print("Ingrese el indice: ")
    n2 = float(input())
    print("El resultado es: ", n1 ** (1/n2))


print("Su calculadora le da la bienvenida")
while True:
    print(menú)
    mco = int(input()) 
    if mco == 1: 
        Suma()
    elif mco == 2:  
        Resta()
    elif mco == 3:
        Multiplicación()         
    elif mco == 4:
        division() 
    elif mco == 5:
        Potencia()
    elif mco == 6:
        Raiz()
    elif mco == 7:
        sys.exit()
          

