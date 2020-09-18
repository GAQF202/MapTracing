import re
from Elements import *


class multifunctions:
    def read_path(self,input):
        file = open(input, "r" , encoding="utf8")

        
        patunic = r"[\s*<nombre>\n*\s*[A-Z]*[a-z]*\s*[A-Z]*\s*[a-z]*\s*[0-9]*\n*\s*</nombre>]*"
        cont = file.read()

        #for i in file:
          #if (re.match(patunic, i)):
            #print(i)

        fa = re.findall(patunic,cont)

        print(fa)

    



#FUNCION DE MENU
class login:

    not_file = False

    def take_name(self):
        print("***********************************************")
        print("Lenguajes formales y de programación sección:A-")
        print("*    Gerson Aaron Quinia Folgar 201904157     *")
        print("***********************************************")
        print("**************Eliga una opción*****************")

        print("1. Cargar Archivo")
        print("2. Graficar Ruta")
        print("3. Graficar Mapa ")
        print("4. Salir ")

        option = int(input())
        rute_list = []
   
        if option == 1:
            print("Ingrese la ruta del archivo")
            path = str(input())
            lector.read_path(path)
        
        elif option == 2:
            ruta = Rute()
            ruta.nombre = "hola"
            ruta.peso = "jajaja"
            ruta.inicio = "dfd"
            ruta.fin = "hola extraño"
            rute_list.append(ruta)
            print(rute_list[0].nombre)

            ruta = Rute()
            ruta.nombre = "adios"
            ruta.peso = "jajaja"
            ruta.inicio = "dfd"
            ruta.fin = "hola extraño"
            rute_list.append(ruta)
            print(rute_list[1].nombre)


        elif option == 3:
            print("Graficando Mapa...")

        elif option == 4:
            print("Gracias por utilizar MapTracing :)")
        else:
            print("")
            print("Por favor Eliga una opción válida")
            inicio.take_name()

inicio = login()
lector = multifunctions()