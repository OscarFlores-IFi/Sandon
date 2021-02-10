# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup as bs
import requests
from time import sleep
# from multiprocessing import pool
import pandas as pd

def get_soup(link_principal, link_secundario, iterador):
    #función para conseguir el html de la pagina web
    html = link_principal + str(iterador) + link_secundario
    site = requests.get(html)
    soup = bs(site.content, 'html.parser')
    print(html)
    return soup

def only_alpha(string):
    # Toma unicamente letras
    alpha = ""
    for char in string:
        if char.isalpha():
            alpha += char
    return(alpha)  

def repeat(func, link1, link2, min_iterations: int = 10):
    # repite el procedimiento de jalar datos de la pagina hasta terminar con la lista. 
    p_list = []
    for j in range(1,min_iterations):
        try:
            tmp = func(get_soup(link1,link2,j))
            if len(tmp) > 0:                 
                p_list = p_list + tmp
                sleep(1)
            else:
                return p_list
        except:
            return p_list
        
# def guardar_archivo(lista):
#     nombre = input("nombre de archivo: ")
#     doc = (open(("C:\\Users\\Oscar Flores\\Desktop\\" + nombre + ".csv"), 'w'))
#     doc.writelines(lista)
#     doc.close()



        









#%%## Para Fresko: 
def sacar_datos_Fresko(soup):
    # encuentra los datos de Fresko 
    productos = (soup.find_all('div', class_="li_prod_picture"))
    
    # for i in productos: 
    #     nombre = i.find('strong').get_text()
    #     precio = i.find('span', class_ = "precio_normal").get_text()
    #     unidad = only_alpha(i.find_all("p")[-1].get_text())
    return [[i.find('strong').get_text(), 
             i.find('span', class_ = "precio_normal").get_text(), 
             only_alpha(i.find_all("p")[-1].get_text())] for i in productos]
    
link_Ff = ("https://www.lacomer.com.mx/lacomer/doHome.action?key=Frutas-y-Verduras&succId=407&padreId=14&pasId=13&opcion=listaproductos&path=,14&pathPadre=0&jsp=PasilloPadre.jsp&noPagina=",
                    "&mov=1&subOpc=0&agruId=13&succFmt=100&dep=Frutas-&numResultados=40&filtroSeleccionado=0")

link_Fv = ("https://www.lacomer.com.mx/lacomer/doHome.action?key=Frutas-y-Verduras&succId=407&padreId=15&pasId=13&opcion=listaproductos&path=,15&pathPadre=0&jsp=PasilloPadre.jsp&noPagina="
                    ,"&mov=1&subOpc=0&agruId=13&succFmt=100&dep=Verduras&numResultados=40&filtroSeleccionado=0")

frutas_Fresko = repeat(sacar_datos_Fresko, link_Ff[0], link_Ff[1])
verduras_Fresko = repeat(sacar_datos_Fresko, link_Fv[0], link_Fv[1])


Fresko = pd.DataFrame(frutas_Fresko + verduras_Fresko).sort_values(by=0,axis=0)




# #%%## Para Soriana: 
# def sacar_datos_Soriana(soup):
#     # encuentra los datos de Soriana 
#     productos = (soup.find_all('div', class_="col-lg-3 col-md-4 col-sm-12 col-xs-12 product-item"))
    
#     # for i in productos: 
#     #     nombre = ' '.join(i.find_all("h4")[0].get_text().split(" ")[:-1])
#     #     precio = i.find_all("h4")[1].get_text()
#     #     unidad = i.find_all("h4")[0].get_text().split(" ")[-1]
#     return [[' '.join(i.find_all("h4")[0].get_text().split(" ")[:-1]), 
#              i.find_all("h4")[1].get_text(), 
#              i.find_all("h4")[0].get_text().split(" ")[-1]] for i in productos]

    
# link_Sf = ("https://superentucasa.soriana.com/default.aspx?p=13287&px=", "&nuor=0")

# link_Sv = ("https://superentucasa.soriana.com/default.aspx?p=13288&px=", "&nuor=0")


# tmp1 = sacar_datos_Soriana(get_soup( link_Sf[0], link_Sf[1],1))
# tmp2 = sacar_datos_Soriana(get_soup( link_Sf[0], link_Sf[1],2))
# tmp3 = sacar_datos_Soriana(get_soup( link_Sf[0], link_Sf[1],3))
# tmp4 = sacar_datos_Soriana(get_soup( link_Sf[0], link_Sf[1],4))

# # frutas_Soriana = repeat(sacar_datos_Soriana, link_Sf[0], link_Sf[1])
# # verduras_Soriana = repeat(sacar_datos_Soriana, link_Sv[0], link_Sv[1])




