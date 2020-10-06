from tabulate import tabulate
import datetime
import webbrowser

class Report(object):
    def tabulador(self, list_on_list, lexemas_position):

#----------------------TABULADOR PARA LEXEMAS--------------------
        tabla2 = """<thead><tr>
          <th><strong>Lexema</strong></th>
          <th><strong>Fila</strong></th>
          <th><strong>Columna</strong></th>
          <th><strong>Token</strong></th>
        </tr></thead>
        """

        lexem_index=0
        index2 = 0
        for lexema in lexemas_position:
            lexem_index+=1
            index2+=1
            if index2==1:
                tabla2+="<tr>" + "<td>"+str(lexema)+"</td>" 
            elif index2<=4:
                tabla2 +=  "<td>"+str(lexema)+"</td>" 
            if index2 == 4:
                index2=0


#----------------------TABULADOR PARA ERRORES--------------------
        tabla = """<thead><tr>
          <th><strong>No.</strong></th>
          <th><strong>Fila</strong></th>
          <th><strong>Columna</strong></th>
          <th><strong>Carácter</strong></th>
          <th><strong>Descripción</strong></th>
        </tr></thead>
        """
        index = 0
        for fila in list_on_list:
            index += 1
            tabla += "<tr><td>"+str(index)+"</td>" 
            for colum in fila:
                tabla += "<td>" + str(colum) + "</td>" 

#----------------------CREADOR DEL HTML--------------------

        f = open('reportes.html','w')

        mensaje = '''<html>
        <head>
            <title>Reportes</title>
            <link rel="stylesheet" href="estilos.css">
        </head>
        <body>
        <h1>Reporte de errores</h1>
        <div id="tabla1"><table class="egt" border="1">'''+tabla+'''</table></div>
        <h1>Reporte de lexemas encontrados</h1>
        <div id="tabla2"><table class="egt2" border="1">'''+tabla2+'''</table></div>
        </body>
        </html>'''

        f.write(mensaje)
        f.close()
        webbrowser.open_new_tab('reportes.html')
        tabla=""
        tabla2=""
        mensaje=""
        print("Reporte de errores generado")

        while len(list_on_list) !=0:
            list_on_list.pop()
        while len(lexemas_position) !=0:
            lexemas_position.pop()
       