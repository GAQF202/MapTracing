from graphviz import Digraph
from Stack import *
from Elements import *
import networkx as nx
lista = ["estacion1" , "estación2", "estacion3", "estación4"]
colores = ["#C0C0C0", "#808080", "#000000", "#FFFFFF"]

#CLASE PARA BUSCAR EL CAMINO DE RUTAS MAS CORTO
#class Browser(object):  

def short_rute(rutas,estaciones,inicio,fin):
    rutas_seleccionadas = []
    aristas = []

    for estacion in estaciones:
        for ruta in rutas:
            
            if (estacion.estado.lower() == "cerrada") and (ruta.inicio.lower()==estacion.nombre.lower() or ruta.fin.lower()==estacion.nombre.lower()):
                ruta.elim = "si"
    
    for ruta in rutas:
        if ruta.elim != "si":
            aristas.append(ruta.get_edge())
    
    DG = nx.DiGraph()
    DG.add_weighted_edges_from(aristas)
    short_way = nx.dijkstra_path(DG,source=inicio.lower(),target=fin,weight="weight")

    i = -1
    for way in short_way:
        i+=1
        for ruta in rutas:
            if short_way[i-1] == ruta.inicio.lower() and short_way[i] == ruta.fin.lower() and short_way[i-1] != fin.lower():
                rutas_seleccionadas.append(ruta)
                ruta.marca = "si"

    return short_way

#------------------------------METODO PARA GRAFICAR MAPAS Y RUTAS------------------------------
def graficos(rutas, estaciones,map_name):
    f = Digraph('finite_state_machine', filename='fsm.gv')
    f.attr(rankdir='LR', size='8,5')
    f.attr(label= r"\n\n"+ map_name)
    #f.attr(fontsize='20', color="#19EDBD")
    f.attr(fontsize='20')
#--------------------------------CREA RUTAS COMO ARISTAS----------------------------------------
    for estacion in estaciones:
        f.attr('node', shape='ellipse',style='filled', color = str(estacion.color))
        f.node(estacion.nombre.lower() + "\n" + estacion.estado.lower())
#-------------------------------CREA ESTACIONES COMO NODOS--------------------------------------
    
    for ruta in rutas:
        if ruta.get_marca()=="si":
            f.attr('edge',color="#FF6347",penwidth = "3")
            f.edge(str(ruta.inicio).lower()+ "\n" + estacion.estado.lower(), str(ruta.fin).lower()+ "\n" + estacion.estado.lower(), label=str(ruta.nombre)+"\n"+str(ruta.peso))
        else:
            f.attr('edge',color="black",penwidth = "")
            f.edge(str(ruta.inicio).lower()+ "\n" + estacion.estado.lower(), str(ruta.fin).lower()+ "\n" + estacion.estado.lower(), label=str(ruta.nombre)+"\n"+str(ruta.peso))
    
    for ruta in rutas:
        ruta.marca = ""

    f.view()

def graficar_camino(rutas,estaciones,nodos):
    bolitas = []
    g = Digraph('finite_state_machine', filename='CaminoSeleccionado.gv')
    g.attr(rankdir='LR', size='8,5')
    for nodo in nodos:
        for estacion in estaciones:
            if str(nodo).lower() == estacion.nombre.lower():
                bolitas.append(estacion)

    for bolita in bolitas:
        g.attr('node', shape='ellipse',style='filled', color = str(bolita.color))
        g.node(bolita.nombre.lower()+ "\n" + bolita.estado.lower() )

    for ruta in rutas:
        if ruta.get_marca()=="si":
            g.attr('edge',color="#FF6347",penwidth = "3")
            g.edge(str(ruta.inicio).lower()+ "\n" + bolita.estado.lower(), str(ruta.fin).lower()+ "\n" + bolita.estado.lower(), label=str(ruta.nombre)+"\n"+str(ruta.peso))

    for ruta in rutas:
        ruta.marca = ""
    while len(bolitas) != 0:
        bolitas.pop()

    g.view()
