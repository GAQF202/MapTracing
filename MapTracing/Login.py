import re
from Elements import *
from Stack import *
from MapTracing import *
import os
from tabulate import tabulate
from reportes import *


probando = []  
estaciones = []
errores = []
lexemas = []
lexema_temporal = []
lexema_position = []

def save_lexema(lex,pos):

    for d in lex:
        lexemas.append(str(lex.pop(0)))
        lexemas.append(str(pos.pop(0)))
        lexemas.append(str(pos.pop(0)))
        lexemas.append(str(lex.pop(0)))


def save_mistakes(row,colum,token):
    error_temporal=[]
    if token!='\t':
        error_temporal.append(str(row))
        error_temporal.append(str(colum))
        error_temporal.append(token)
        errores.append(error_temporal)

class multifunctions:
    def analyzer(self,input):
        f = open(input, "r", encoding="utf8")

        lines = f.readlines()

        file = open("gege.txt","w")

        estado = 0
        lexema = ''
        colum = 0
        row = 0

        pila = Stack()
        

        for line in lines:
            row += 1
            for caracter in line:
                colum += 1
                if caracter == '\n':
                    colum=0
                if caracter == '\n' or caracter == ' ':
                    continue

                if estado == 0:
                    if caracter == "<":
                        estado=1

                    else:
                        save_mistakes(row,colum,caracter)

                elif estado == 1:
                    if ord(caracter) >= 65 and ord(caracter) <=122:#es letra
                        estado = 2
                        lexema = lexema +caracter
                    elif caracter=="/":
                        estado=7
                        lexema = lexema +caracter
                    else:
                        save_mistakes(row,colum,caracter)
                elif estado==7:
                    if  ord(caracter) >= 65 and ord(caracter) <=122:#es letra
                        estado = 2
                        lexema = lexema + caracter
                    else:
                        save_mistakes(row,colum,caracter)

                elif estado == 2:
                    if ord(caracter) >= 65 and ord(caracter) <=122 :#es letra
                        estado == 2
                        lexema = lexema +caracter

                    elif caracter==">":
                        estado = 3
                        lexema = lexema + caracter + "\n"
                    else:
                        save_mistakes(row,colum,caracter)

                elif estado == 3:
                    if (ord(caracter) >= 65 and ord(caracter) <=122):#es letra
                        estado = 4
                        lexema = lexema +caracter

                        lexema_position.append(row)
                        lexema_position.append(colum)

                    elif (ord(caracter) >= 48 and ord(caracter) <=57):#es numero
                        estado = 8
                        lexema = lexema +caracter
                        
                        lexema_position.append(row)
                        lexema_position.append(colum)

                    elif caracter == "#":
                        estado = 5
                        lexema = lexema +caracter

                        lexema_position.append(row)
                        lexema_position.append(colum)

                    elif caracter == "<":
                        estado = 1
                        lexema = lexema + "\n"
                    else:   
                        save_mistakes(row,colum,caracter)
                elif estado == 4:
                    if (ord(caracter) >= 65 and ord(caracter) <=122):#es letra 
                        estado=4
                        lexema = lexema +caracter
                    elif (ord(caracter) >= 48 and ord(caracter) <=57):#es numero
                        estado = 8
                        lexema = lexema +caracter
                    elif caracter=="_":
                        estado = 11
                        lexema = lexema +caracter
                    elif caracter=="<":
                        estado = 1
                        lexema = lexema + "\n"
                    else:
                        save_mistakes(row,colum,caracter)

                elif estado == 5:
                    if (ord(caracter) >= 65 and ord(caracter) <=122) or (ord(caracter) >= 48 and ord(caracter) <=57):#es letra o numero
                        estado=6
                        lexema = lexema +caracter
                    else:
                        save_mistakes(row,colum,caracter)
                elif estado == 6:
                    if (ord(caracter) >= 65 and ord(caracter) <=122) or (ord(caracter) >= 48 and ord(caracter) <=57):#es letra o numero
                        estado=6
                        lexema = lexema +caracter
                    elif caracter=="<":
                        estado = 1
                        lexema = lexema + "\n"
                    else:
                        save_mistakes(row,colum,caracter)

                elif estado == 8:
                    if (ord(caracter) >= 65 and ord(caracter) <=122):#es letra 
                        estado = 4
                        lexema = lexema +caracter
                    elif (ord(caracter) >= 48 and ord(caracter) <=57):#es numero
                        estado = 8
                        lexema = lexema +caracter
                    elif caracter==".":
                        estado = 9
                        lexema = lexema +caracter
                    elif caracter=="_":
                        estado = 11
                        lexema = lexema +caracter
                    elif caracter=="<":
                        estado = 1
                        lexema = lexema + "\n"
                    else:
                        save_mistakes(row,colum,caracter)
                elif estado == 9:
                    if (ord(caracter) >= 48 and ord(caracter) <=57):#es numero
                        estado = 10
                        lexema = lexema +caracter

                elif estado == 10:
                    if (ord(caracter) >= 48 and ord(caracter) <=57):#es numero
                        estado = 10
                        lexema = lexema +caracter
                    elif caracter=="<":
                        estado=1
                        lexema = lexema + "\n"

                elif estado == 11:
                    if (ord(caracter) >= 65 and ord(caracter) <=122) or (ord(caracter) >= 48 and ord(caracter) <=57):#es letra o numero
                        estado=4
                        lexema = lexema +caracter

            file.write(lexema)
            lexema = "" 
        #file.close()
        patruteopen = r"\s*r*R*u*U*t*T*a*A*>"
        patruteclose = r"\s*/r*R*u*U*t*T*a*A*>"
        patestationopen = r"\s*e*E*s*S*t*T*a*A*c*C*i*I*o*O*n*N*>"
        patestationclose = r"\s*/e*E*s*S*t*T*a*A*c*C*i*I*o*O*n*N*>"
        patname = r"\s*/nombre>"
        patnameclose = r"\s*/nombre>"
        patstartclose = r"\s*/inicio>"
        patendclose = r"\s*/fin>"
        patweight = r"\s*/peso>"
        patestatusclose = r"\s*/estado>"
        patcolorclose = r"\s*/color>"
        
        file = open("gege.txt","r")
        lines = file.readlines()
        padre =""
        for row in lines:
            if row == "\n":
                continue
           
            if re.match(patruteopen,row):
                padre = "ruta"
                ruta = Rute()
            elif re.match(patestationopen,row):
                estacion = Estation()
                padre = "estacion"

            if (re.match(patnameclose,row)) and padre == "ruta":
                ruta.nombre = str(pila.pop()).strip()
                lexema_temporal.append(ruta.nombre)
                lexema_temporal.append("nombre")
                
            if (re.match(patstartclose,row))and padre == "ruta":
                ruta.inicio = str(pila.pop()).strip()
                lexema_temporal.append(ruta.inicio)
                lexema_temporal.append("inicio")
   
            if (re.match(patendclose,row))and padre == "ruta":
                ruta.fin = str(pila.pop()).strip()
                lexema_temporal.append(ruta.fin)  
                lexema_temporal.append("fin")

            if (re.match(patweight,row))and padre == "ruta":
                ruta.peso = str(pila.pop()).strip()
                lexema_temporal.append(ruta.peso)
                lexema_temporal.append("peso")

            if(re.match(patruteclose, row))and padre == "ruta":
                probando.append(ruta)
                padre=""
                while(pila.get_Size()!=0):
                    pila.pop()


            if (re.match(patnameclose,row)) and padre == "estacion":
                estacion.nombre = str(pila.pop()).strip() 
                lexema_temporal.append(estacion.nombre)
                lexema_temporal.append("nombre")
   
            if (re.match(patestatusclose,row))and padre == "estacion":
                estacion.estado = str(pila.pop()).strip() 
                lexema_temporal.append(estacion.estado)
                lexema_temporal.append("estado")

            if (re.match(patcolorclose,row))and padre == "estacion":
                estacion.color = str(pila.pop()).strip()    
                lexema_temporal.append(estacion.color)
                lexema_temporal.append("color")

            if(re.match(patestationclose, row))and padre == "estacion":
                probando.append(estacion)
                padre=""
                while(pila.get_Size()!=0):
                    pila.pop()

            pila.push(row)


        #for b in probando:
          #print(b.get())
        
        save_lexema(lexema_temporal,lexema_position)
        reportar = Report()
        reportar.tabulador(errores,lexemas)
        inicio.regresar()
        

#FUNCION DE MENU
class login:

    not_file = False

    def take_name(self):

        print("1. Cargar Archivo")
        print("2. Graficar Ruta")
        print("3. Graficar Mapa ")
        print("4. Salir ")

        option = int(input())
        rute_list = []
   
        if option == 1:
            print("Ingrese la ruta del archivo")
            path = str(input())
            lector.analyzer(path)     
            
        elif option == 2:
            if len(probando)==0:
                print("----Debe ingresar primero un archivo válido----")
                inicio.take_name()
            else:
                print("Ingrese su estacion inicial")


        elif option == 3:
            print("Graficando Mapa...")
            rios1 = [['Almanzora', 105],
            ['Guadiaro', 79],
            ['Guadalhorce', 154],
            ['Guadalmedina', 51.5]]
        
            print(tabulate(rios1))
            
        elif option == 4:
            print("Gracias por utilizar MapTracing :)")
        else:
            print("")
            print("Por favor Eliga una opción válida")
            inicio.take_name()

    def regresar(self):
        print("Para regresar presione cualquier tecla")
        regreso = input()
        if(regreso != None):
            os.system("cls")
            inicio.take_name()

inicio = login()
lector = multifunctions()