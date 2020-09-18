import re
from Elements import *
from Stack import *

class multifunctions:
    def read_path(self,input):
        pila = Stack()
        file = open(input, "r" , encoding="utf8")
        lmpiador = ""

        probando = []
        
        patname = r"[\s*<nombre>\n*\s*[A-Z]*[a-z]*\s*[A-Z]*\s*[a-z]*\s*[0-9]*\n*\s*</nombre>]*"

        patruteopen = r"\s*<ruta>"
        patruteclose = r"\s*</ruta>"    

        patnameclose = r"\s*</nombre>"
        patstartclose = r"\s*</inicio>"
        patendclose = r"\s*</fin>"
        patweight = r"[\s*<peso>\s*[0-9]*.[0-9]*\s*</peso>]*"

        for i in file:
            
            if re.match(patruteopen,i):
                ruta = Rute()
            
            if (re.match(patnameclose,i)):
                ruta.nombre = str(pila.pop()).strip()

            if (re.match(patstartclose,i)):
                ruta.inicio = str(pila.pop()).strip()    
                
            if (re.match(patendclose,i)):
                ruta.fin = str(pila.pop()).strip()   

            if (re.match(patweight,i)):
                ruta.peso = str(i).strip()

            if(re.match(patruteclose, i)):
                probando.append(ruta)
                while(pila.get_Size()!=0):
                    pila.pop()

            pila.push(i)

            #if (re.match(patunic0,i) and not(re.match(patunic,i))):
                #print(i)   
        for i in probando:
          print(i.get())


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