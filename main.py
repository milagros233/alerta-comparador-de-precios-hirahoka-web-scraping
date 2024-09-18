#!/usr/bin/env python
# coding: utf-8

# In[4]:

#librerias a utilizar
from extraerData import get_data
from emailSender import send_email
import json
import os


# %%
file= 'PRODUCT_PRICE'

#en la funcion se le tiene que llamar al dicnionario de producto
def save_product(product):
    with open (file,'w') as f:
        json.dump(product,f)

# %%
#se va a leer los del diccionario de producto que estan en el archivo
#si existe el archivo lo leera y retorna si no existe, retornara un diccionario vacio
def load_previous_prices():
   if os.path.exists(file):
       with open (file,'r') as f:
           return json.load(f)
   else:
       return {}
# %%
#verifica si hubo cambios en el precio del producto para que pueda enviar el correo al remitente
def check_change():
    #se obtiene los datos actuales del web scraping 
    current_price= get_data()
 
    #se obtiene los precios anteriores  (archivo)
    previos_product= load_previous_prices()

    #verificar si el producto esta en los precios anteriores y si es menor al registrado para que pueda mandarse un correo
    #variable que almacena los cambie
    change=[]
    for nom,price in current_price.items():
        if nom in previos_product and  previos_product[nom]  > price:
            change.append(f"{nom}: precio anterior {previos_product[nom]} precio actual {price}")
            sub= "¡Alerta Baja de Precio!"
            content= "A disminuido el precio de producto: ".join(change)
            send_email(subject=sub,body=content)
            save_product(current_price)
        else:
            print("No se detectaron cambios")

# %%
#ejecucion de la funcion check_change
if __name__ == "__main__":
  check_change()
# %%


