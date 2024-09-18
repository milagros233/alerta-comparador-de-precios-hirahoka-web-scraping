#!/usr/bin/env python
# coding: utf-8

# In[7]:


#importando librerias
import requests
from bs4 import BeautifulSoup

def get_data():
    #url del producto
    url= "https://hiraoka.com.pe/celulares/celulares/celular-libre-samsung-galaxy-a15-6-5-256gb-8gb-ram-blue-black"

    ##El header es información que mandan los navegadores, debemos incluirlo para simular que somos un usuario normal
    header = {"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
    
    #pedicion para visitar la pagina
    r= requests.get(url, headers=header, timeout=10)
    if r.status_code == 200:
        #soup
        soup= BeautifulSoup(r.text,'html.parser')
        #diccionario donde estaran los productos
        product= {}
        #buscador de nombre del producto
        name_product=soup.find('h1', class_= "page-title").text

        #transformando ya que viene con caracteres especiales
        name_product=  name_product .replace("///","").strip()

        #buscador precio del producto
        price_product= soup.find('span', attrs={'class':'price'}).text
       
        #transformando ya que viene con caracteres especiales
        price_product= float(price_product.replace("S/","").strip())
        
        #ejemplo del dicionario'celular': 500.00
        product[name_product]= price_product
        
        return product
        
    else:
        print(f"Error al acceder a la página {r.status_code}")


# In[ ]:




