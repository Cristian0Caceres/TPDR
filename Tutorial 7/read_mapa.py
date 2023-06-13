# By Alberto Caro S.
# Ing. Civil en Informatica
# Doctor(c) Cs. de la Computacion
# Pontificia Universidad Catolica de Chile
# Programacion de Robot -> INFO1139
#---------------------------------------------------------------------
#__________      ___.           __  .__               
#\______   \ ____\_ |__   _____/  |_|__| ____ _____   
# |       _//  _ \| __ \ /  _ \   __\  |/ ___\\__  \  
# |    |   (  <_> ) \_\ (  <_> )  | |  \  \___ / __ \_
# |____|_  /\____/|___  /\____/|__| |__|\___  >____  /
#        \/           \/                    \/     \/ 
#---------------------------------------------------------------------
import pygame as PG, time as Ti, random as RA, ctypes as CT
from pygame.locals import *

#---------------------------------------------------------------------
# Definicion de Constantes y Variables
#---------------------------------------------------------------------
nRES = (1184,576); nT_WX = nT_HY = 32 ; nMAX_ROBOTS = 01 ; lGo = True
nMx  = nMy = 0; nR_1 = 1154 ; nR_2 = 32

#---------------------------------------------------------------------
# Definicion Structure Celda Inteligente del Mapa
#---------------------------------------------------------------------
class eCelda(CT.Structure):
 _fields_ = [
             ('nT',CT.c_ubyte), # Tipo de Tile/Baldosa
             ('nD',CT.c_ubyte), # Tile Disponible? 
             ('nS',CT.c_ubyte), # 0 : No se pinta - # 1 : Si se pinta
             ('nF',CT.c_ubyte), # Fila de Mapa
             ('nC',CT.c_ubyte), # Columna de Mapa 
             ('nR',CT.c_ubyte), # Recurso a Explotar:
                                # 1:Acero
                                # 2:Cobre
                                # 3:Litio
                                # 4:Butano
             ('nQ',CT.c_ubyte)  # Cantidad del Recurso
            ]

#---------------------------------------------------------------------
# Lectura de datos File Binario Estructurado
#---------------------------------------------------------------------
def GetData():
    nFh.readinto(eReg) # Leemos el Registro completo de tipo eCelda
    return eReg # lo devolvemos a quien lo pidio
    
#---------------------------------------------------------------------
# Maain
#---------------------------------------------------------------------
eReg = eCelda() # Variable de tipo eCelda del Mapa
nFh  = open('mapa.dat','rb') # Abrimos File Mode Lectura Binario Estructurado
# Pintamos / Formateamos la salida de los datos a apantalla
sLine = 'Tile: %02d Disp: %1d Show: %1d Fila: %02d Colu: %02d Recu: %1d Qty: %04d' 
for nReg in range(666): # Recorrimos el Archivo
    eReg = GetData()    # 4.662 Bytes tamano mapa.dat / 7 Bytes = 666
    # Imprimimos los datos de todas las celdas del mapa a pantalla (screen)
    print(sLine %(eReg.nT,eReg.nD,eReg.nS,eReg.nF,eReg.nC,eReg.nR,eReg.nQ))
nFh.close() # Matamos el File
    



    




    
    


    
    

            