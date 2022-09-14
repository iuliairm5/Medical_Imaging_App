# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 11:27:56 2021

@author: Iulia
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as sc

#citesc imaginea initiala
cale= r'E:\..\hip_1.bmp'
img=plt.imread(cale)

#citesc imaginea pe care ar trebui sa o obtin
cale2= r'E:\..\hip_1_final.bmp'
imgfinala=plt.imread(cale2)
plt.figure()
plt.imshow(imgfinala,cmap='gray')
plt.title('Imaginea finala')

#functia care transforma imaginea color in img cu nivele de gri
def rgb2gri(img_in,format): 
    s=img_in.shape
    if len(s)==3 and s[2]==3:
        if format=='png':
            img_out=(0.299*img_in[:,:,0]+0.587*img_in[:,:,1]+0.114*img_in[:,:,2])*255
        elif format =='jpg':
            img_out=0.299*img_in[:,:,0]+0.587*img_in[:,:,1]+0.114*img_in[:,:,2]
        elif format =='bmp':
            img_out=(0.299*img_in[:,:,0]+0.587*img_in[:,:,1]+0.114*img_in[:,:,2])
        img_out=img_out.astype('uint8')
        return img_out
    else:
        print('Conversia nu a putut fi realizata deoarece imaginea de intrare nu este color!')
        return img_in
    
img=rgb2gri(img,'bmp') #am obtinut imaginea in nivele de gri

#filtrul median imi elimina zgomotul tip sare(255) si piper(0) (zgomot impulsiv)
imgf=sc.median_filter(img,size=2) 

#am luat o noua variabila in care salvez continutul matricei imgf, dar o fac tip float pentru operatiile care urmeaza
imgff=imgf
imgff=imgff.astype(float)

#extrag separat numarul de linii si de coloane ale matricei imaginii imgf
y=imgf.shape[0];
w=imgf.shape[1];

#voi aplica functia putere cu r>1 pentru a face nivelele de gri mai luminoase mai intunecate
r=2.5
for i in range(y):
    for j in range(w):
        imgff[i][j]=255*((imgf[i][j]/255)**r)         
            
imgff=np.clip(imgff,0,255) #matricea imaginii va contine doar valori intre 0 si 255
imgff=imgff.astype('uint8') #revin la formatul uint8
plt.figure()
plt.imshow(imgff,cmap='gray') #afisarea imaginii mele finale
plt.title('Imaginea mea finala')


imgg=(imgfinala.astype(float)-imgff.astype(float))
print(imgg.sum())
