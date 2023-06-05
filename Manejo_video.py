from inspect import stack
from turtle import color
import cv2 # OpenCV para computer vision
import numpy as np # Para cálculo de matrices
import matplotlib.pyplot as plt #Para graficar
import os #Habilita el manejo de directorios
import skvideo.io
from math import sqrt

Ruta = r'C:\Users\user\Desktop\Procesamiento de Imagenes\Proceso_videos\Video.mp4'
Video = cv2.VideoCapture(Ruta)
#Testeando tamaño de video original
Frames_number=0
Contador = 0
frames_array = []
while(Video.isOpened()):
    ret, frame = Video.read () ## ret devuelve un valor booleano
    if ret == True:
        Frames_number=Frames_number+1
        Color=frame[:,:,[2,1,0]]
        [Fl,Cl,Ch]=Color.shape
        frames_array.append(Color)
         
    else:
        break
Resultado = np.zeros((Fl,Cl,Ch))
Stack=np.zeros((Frames_number,Fl,Cl,Ch))#Variable para guardar frames del video 
Video.release()
valor_alterar = 60

new_array = []
print("Numero de frames:" , Contador)
print("Cantidad lista: ", len(frames_array))

Ruta = r'C:\Users\user\Desktop\Procesamiento de Imagenes\Proceso_videos\Video.mp4'#Ubicación de la imagen desde el google drive
Video = cv2.VideoCapture(Ruta)
t=0
salida = cv2.VideoWriter('salida.mp4', cv2.VideoWriter_fourcc(*'mp4v'),30,(Cl,Fl))
while(Video.isOpened()):
    ret, frame = Video.read () 
    if ret == True:
        Color=frame[:,:,[2,1,0]]
        I_Gris=cv2.cvtColor(Color, cv2.COLOR_BGR2GRAY)

        ImgSobelX = cv2.Sobel(I_Gris,cv2.CV_8U,1,0, ksize= 3)
        ImgSobelX=cv2.normalize(ImgSobelX, ImgSobelX, 0, 255, norm_type=cv2.NORM_MINMAX) 
        ImgSobelX = cv2.cvtColor(ImgSobelX, cv2.COLOR_GRAY2BGR)

        Stack[t]=ImgSobelX.astype(np.uint8)
        t=t+1
        #print('')
        #plt.imshow(ImgSobelX.astype('uint8'),vmin=0, vmax=255,cmap='gray') # cmap='gray' Grafica la imagen 
        #plt.show()

        salida.write(ImgSobelX)
    

        

    else:
        break


salida.release()
Video.release()




                    


