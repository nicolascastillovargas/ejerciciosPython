#!/usr/bin/env python
# coding: utf-8

# In[1]:


contador=0

while contador <10:
    print(contador)
    contador +=1


# In[16]:


contador_ext=0
contador_int=0

while contador_ext <5:
    while contador_int<6:
        print(contador_ext,contador_int)
        contador_int +=1
        
        if contador_int >=3:
            print("nea")
            
    contador_ext +=1
    contador_int =0


# In[ ]:


frutas = ['manzana','pera','mango']
for fruta in frutas:
    print('pera')


# In[11]:


objetivo = int(input('escoge un entero: '))
respuesta = 0

while respuesta**2 < objetivo:
    respuesta += 1
if respuesta**2 == objetivo:
    print(f'la raiz cuadrada de {objetivo} es {respuesta}')
else:
    print( 'esa no imbecil')


# In[21]:


objetivo = int(input('escoge un numero:'))
epsilon = 0.01
paso = epsilon**2
respuesta = 0.0

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso
    
if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'paila pex')
else:
    print(f'la raiz cuadrada de {objetivo} es la {respuesta}')


# In[13]:


a=1.9974999999997964*1.9974999999997964
print(a)


# In[27]:


objetivo = int(input('escoge un numero: '))
epsilon = 0.01
bajo = 0.0
alto = max(1.0, objetivo)
respuesta= (alto + bajo) / 2

while abs(respuesta**2 - objetivo) >= epsilon:
    
    if respuesta**2 < objetivo: 
        bajo = respuesta
    else: 
        alto = respuesta
    respuesta = (alto+bajo) / 2
print(f'la raiz cuadrada de {objetivo} es {respuesta}')


# In[ ]:




