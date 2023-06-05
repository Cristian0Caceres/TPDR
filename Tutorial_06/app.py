# By Alberto Caro S.
# Ing. Civil en Computacion
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
import pygame as PG, time as Ti, random as RA, ctypes as ct
from pygame.locals import *

#---------------------------------------------------------------------
# Definicion de Constantes Globales
#---------------------------------------------------------------------
nRES = (960,640); nTW_X = nTH_Y = 32 ; nMx = nMy = 0 ; lOK = True;
xm1=0;ym1=0;xm2=0;ym2=0;xm3=0;ym3=0;nBTN_LEFT = 1#establesemos las variables gobales entre ellas xm y ym los cuales corresonden a las posisiones en x e y en los mapas 1 2 3 y para identificar a que mapa corresponden se les pone el numero del mapa correspondiente

#---------------------------------------------------------------------
# Definicion de Structura
#---------------------------------------------------------------------
class eRobots(ct.Structure):
 _fields_ = [
             ('nF',ct.c_short),
             ('nX',ct.c_short),
             ('nY',ct.c_short),
             ('nR',ct.c_short),
             ('dX',ct.c_short),
             ('dY',ct.c_short),
	   ('nV',ct.c_short)
            ]
#---------------------------------------------------------------------
# Carga imagenes y convierte formato PG
#---------------------------------------------------------------------
def Load_Image(sFile,transp = False):
    try: image = PG.image.load(sFile)
    except PG.error,message:
           raise SystemExit,message
    image = image.convert()
    if transp:
       color = image.get_at((0,0))
       image.set_colorkey(color,RLEACCEL)
    return image

#---------------------------------------------------------------------
# Inicializa PGs.-
#---------------------------------------------------------------------
def PyGame_Init():
    PG.init()
    PG.mouse.set_visible(False)
    PG.display.set_caption('Dynamic Big Map 2D - By Alberto Caro')
    return PG.display.set_mode(nRES)

#---------------------------------------------------------------------
# Inicilaiza parametros de los Robots
#---------------------------------------------------------------------
def Init_Robots():
    return

#---------------------------------------------------------------------
# Pinta los Robots en el Super Extra Mega Mapa.-
# Se pintan los Robots en Surface -> sMapa (6400 x 480)
#---------------------------------------------------------------------
def Pinta_Robots():
    return

#---------------------------------------------------------------------
# Actualiza la estructura de datos de cada uno de los robots dentro del
# Mapa sMapa.
#---------------------------------------------------------------------
def Mueve_Robots():
    return

#---------------------------------------------------------------------
# Inicializa las Baldozas = Tiles del Super Extra Mega Mapa.-
#---------------------------------------------------------------------
def Get_Tiles(nMW_X,nMH_Y,tRng):
    return [[ RA.randint(tRng[0],tRng[1]) for i in range(0,nMW_X/nTW_X)] for i in range(0,nMH_Y/nTH_Y)]

#---------------------------------------------------------------------
# Inicializa Superficie del Super Extra Mega Mapa.-
#---------------------------------------------------------------------
def Get_Surface(nAncho_X,nAlto_Y):
    return PG.Surface((nAncho_X,nAlto_Y))

#---------------------------------------------------------------------
# Inicializa Array de Sprites.-
#---------------------------------------------------------------------
def Img_Init():
    aImg = []#esta lista almacena las imagenes que se cargan abajo
    aImg.append(Load_Image('T00.png',False )) # Tierra
    aImg.append(Load_Image('T01.png',False )) # Tierra + Piedras
    aImg.append(Load_Image('T02.png',False )) # Rocas
    aImg.append(Load_Image('T03.png',False )) # Marmol Celeste
    aImg.append(Load_Image('T04.png',False )) # Marmol Star Yellow
    aImg.append(Load_Image('T05.png',False )) # Marmol Star Blue
    aImg.append(Load_Image('T06.png',False )) # Marmol Star Red
    aImg.append(Load_Image('T07.png',False )) # Marmol Gris Claro
    aImg.append(Load_Image('T08.png',False )) # Marmol Cafe
    aImg.append(Load_Image('T09.png',True  )) # Mouse
    aImg.append(Load_Image('bkg.png',False )) # Bkg
    aImg.append(Load_Image('video.png',False )) # Video
    aImg.append(Load_Image('mm.png',False )) #Minimapa1 (esta imagen corresponde a la que usamos en el minimapa 1 esto nos permitira cargarla en pantalla mas adelante)
    aImg.append(Load_Image('mm2.png',False )) #Minimapa2(esta imagen corresponde a la que usamos en el minimapa 2 esto nos permitira cargarla en pantalla mas adelante)
    aImg.append(Load_Image('mm3.png',False )) #Minimapa3(esta imagen corresponde a la que usamos en el minimapa 3 esto nos permitira cargarla en pantalla mas adelante)
    return aImg

#---------------------------------------------------------------------
# Make Mapa
#---------------------------------------------------------------------
def Make_Mapa(sMem,aTiles,tCF):
    nPx = nPy = 0
    for f in range(0,tCF[1]/nTH_Y):
     for c in range(0,tCF[0]/nTW_X):
      if aTiles[f][c] == 0:
         sMem.blit(aSprt[0],(nPx,nPy)); nPx += nTW_X
      if aTiles[f][c] == 1:
         sMem.blit(aSprt[1],(nPx,nPy)); nPx += nTW_X
      if aTiles[f][c] == 2:
         sMem.blit(aSprt[2],(nPx,nPy)); nPx += nTW_X
      if aTiles[f][c] == 3:
         sMem.blit(aSprt[3],(nPx,nPy)); nPx += nTW_X
      if aTiles[f][c] == 4:
         sMem.blit(aSprt[4],(nPx,nPy)); nPx += nTW_X
      if aTiles[f][c] == 5:
         sMem.blit(aSprt[5],(nPx,nPy)); nPx += nTW_X
      if aTiles[f][c] == 6:
         sMem.blit(aSprt[6],(nPx,nPy)); nPx += nTW_X
      if aTiles[f][c] == 7:
         sMem.blit(aSprt[7],(nPx,nPy)); nPx += nTW_X
      if aTiles[f][c] == 8:
         sMem.blit(aSprt[8],(nPx,nPy)); nPx += nTW_X
     nPx = 0; nPy += nTH_Y
    return

#---------------------------------------------------------------------
# Pinta Mouse
#---------------------------------------------------------------------
def Pinta_Mouse():
    sPanta.blit(aSprt[9],(nMx,nMy))
    return

#---------------------------------------------------------------------
# Pinta Display Main
#---------------------------------------------------------------------
def Pinta_Panta():
    sPanta.blit(aSprt[10],(0,0))
    sPanta.blit(aSprt[11],(5,5))
    return

#---------------------------------------------------------------------
# Pinta Mapas
#---------------------------------------------------------------------
def Pinta_Mapas():
    sPanta.blit(sMap_1.subsurface((xm1,ym1,597,304)),(357,5))
    sPanta.blit(sMap_2.subsurface((xm2,ym2,345,393)),(5,241))
    sPanta.blit(sMap_3.subsurface((xm3,ym3,597,319)),(357,315))
    return

#---------------------------------------------------------------------
# Pinta Minimapa
#---------------------------------------------------------------------
def Pinta_Mmapa():
    sPanta.blit(aSprt[12],(755,7))#pintamos en su posision los minimapas esto usando su posision en la lista  que almacena las imagenes
    sPanta.blit(aSprt[13],(247,248))#los minimapas 1 y 3 estan a la misma distancia x en el display por lo que estos solo difieren en la posision de y siendo que el minimapa 3 esta mas abajo que el 1
    sPanta.blit(aSprt[14],(851,322))#los minimapas 1 y 3 son distintos a el mini mapa 2 en su forma y posision por ende al calcular la posision que usara valorres distintos
    return


#---------------------------------------------------------------------
# Pinta Reglas
#---------------------------------------------------------------------
def Pinta_Regla():
    if nMx >= 357 and nMx <= 953:
       if nMy >= 5 and nMy <= 308:
          PG.draw.line(sPanta,(255,255,0),(357,nMy),(953,nMy),2)
          PG.draw.line(sPanta,(255,255,0),(nMx,5),(nMx,308),2)
    return

#--------------------------------------------------------------
# Handle de Pause.-
##--------------------------------------------------------------
def Pausa():
    while 1:
     e = PG.event.wait()
     if e.type in (PG.QUIT, PG.KEYDOWN):
        return

#--------------------------------------------------------------
# Mueve
##--------------------------------------------------------------
def Mueve(cKey):
    global nXd
    if cKey == 'D':
       nXd += 1
       if nXd >= 2880: nXd = 2880
    if cKey == 'I':
       nXd -= 1
       if nXd <= 0: nXd = 0
    return

#---------------------------------------------------------------------
# update mapa_1
#---------------------------------------------------------------------
def UpDate_Scroll_Mapa(nMx,nMy):
    global xm1 , ym1
    if nMx in range(755,957): # Si nMx esta en el rango de 755 a 957
       if nMy in range(7,104): # y nMy esta en el rango de 7 a 104
          xm1 = int(3840*(nMx-755)/float(192)) # Calcula la coordenada x del mapa
          ym1 = int(1920*(nMy-7)/float(96)) # Calcula la coordenada y del mapa
          PG.display.set_caption('[Coord Mapa]-> X: %d1 - Y: %d1' %(xm1,ym1))
          if xm1 >= 3243: xm1 = 3243 # Si xm1 es mayor o igual a 3243, establece xm1 en 3243
          if ym1 >= 1616: ym1 = 1616 # Si ym1 es mayor o igual a 1616, establece ym1 en 1616
    return xm1,ym1  # Devuelve las coordenadas del mapa
def UpDate_Scroll_Mapa_1(nMx,nMy): #Definir los parametros (nMx y nMy) de la posicion en X e Y del cursor

    #Inicializar las coordenadas X e Y del Mini Mapa 1 como variables globales
    global xd1 , yd1

    #Verificar si el cursor esta dentro de los limites del Mini Mapa 1
    if nMx in range(755,947):
       if nMy in range(12,108):

          #Calcular las coordenadas correspondientes en el Mini Mapa 1
          xd1 = int(3840*(nMx-755)/float(192)) #calcula la posicion en el eje X del area visible del mapa 1 en funcion de la posicion
          yd1 = int(1920*(nMy-12)/float(96))   #calcula la posicion en el eje Y del area visible del mapa 1 en funcion de la posicion

          #Actualizar el titulo de la ventana con las coordenadas del Mini Mapa 1
          PG.display.set_caption('[Coord Mapa_1]-> X: %d - Y: %d' %(xd1,yd1))

          #Limitar las coordenadas maximas permitidas en el Mini Mapa 1 en X e Y
          if xd1 >= 3243: xd1 = 3243
          if yd1 >= 1616: yd1 = 1616

    #Devolver las coordenadas actualizadas del mapa 1
    return xd1,yd1

#---------------------------------------------------------------------
# Update Mini_Mapa_2
#---------------------------------------------------------------------
def UpDate_Scroll_Mapa_2(nMx,nMy): #Definir los parametros (nMx y nMy) de la posicion en X e Y del cursor
    #Inicializar la coordenada X e Y del Mini Mapa 2 como variables globales
    global xm2 , ym2
    #Verificar si el cursor esta dentro de los limites del Mini Mapa 2
    if nMx in range(247,343):
       if nMy in range(248,408):
          #Calcular las coordenadas correspondientes en el Mini Mapa 2
          xm2 = int(1920*(nMx-247)/float(96)) #calcula la posicion en el eje X del area visible del mapa 2 en funcion de la posicion
          ym2 = int(3200*(nMy-248)/float(160))#calcula la posicion en el eje Y del area visible del mapa 2 en funcion de la posicion
          #Actualizar el titulo de la ventana con las coordenadas del Mini Mapa 2
          PG.display.set_caption('[Coord Mapa_2]-> X: %d - Y: %d' %(xd2,yd2))
          #Limitar las coordenadas maximas permitidas en el Mini Mapa 2 en X e Y
          if xm2 >= 1575 : xm2 = 1575
          if ym2 >= 2807 : ym2 = 2807
    #Devolver las coordenadas actualizadas del mapa 2
    return xm2,ym2

#---------------------------------------------------------------------
# Update Mini_Mapa_3
#---------------------------------------------------------------------
def UpDate_Scroll_Mapa_3(nMx,nMy): #Definir los parametros (nMx y nMy) de la posicion en X e Y del cursor

    #Inicializar la coordenada X e Y del Mini Mapa 3 como variables globales
    global xm3 , ym3

    #Verificar si el cursor esta dentro de los limites del Mini Mapa 3
    if nMx in range(851,947):
       if nMy in range(322,418):

          #Calcular las coordenadas correspondientes en el Mini Mapa 3
          xm3 = int(1920*(nMx-851)/float(96)) #calcula la posicion en el eje X del area visible del mapa 3 en funcion de la posicion
          ym3 = int(1920*(nMy-322)/float(96)) #calcula la posicion en el eje Y del area visible del mapa 3 en funcion de la posicion

          #Actualizar el titulo de la ventana con las coordenadas del Mini Mapa 3
          PG.display.set_caption('[Coord Mapa_3]-> X: %d - Y: %d' %(xm3,ym3))

          #Limitar las coordenadas maximas permitidas en el Mini Mapa 3 en X e Y
          if xm3 >=  1323 : xm3 = 1323
          if ym3 >= 1601 : ym3 = 1601

    #Devolver las coordenadas actualizadas del mapa 3
    return xm3,ym3
#---------------------------------------------------------------------
# While Principal del Demo.-
#---------------------------------------------------------------------

# Display Main
sPanta = PyGame_Init();

# Tiles/Sprites
aSprt = Img_Init()

# Mapas....
sInfo  = Get_Surface(0345,0230);
sMap_1 = Get_Surface(3840,1920);
sMap_2 = Get_Surface(1920,3200);
sMap_3 = Get_Surface(1920,1920);

aMapTi_1 = Get_Tiles(3840,1920,(0,2)); Make_Mapa(sMap_1,aMapTi_1,(3840,1920))
aMapTi_2 = Get_Tiles(1920,3200,(3,5)); Make_Mapa(sMap_2,aMapTi_2,(1920,3200))
aMapTi_3 = Get_Tiles(1920,1920,(6,8)); Make_Mapa(sMap_3,aMapTi_3,(1920,1920))

aClk = [PG.time.Clock(),PG.time.Clock()] # Init Array de Cloks

nXd = nYd = 0

while lOK:
 cKey = PG.key.get_pressed()
 if cKey[PG.K_ESCAPE] : lOK = False
 if cKey[PG.K_p]      : Pausa()
 if cKey[PG.K_c]      : PG.image.save(sPanta,'foto.png')
 if cKey[PG.K_a]      : Mueve('D')
 if cKey[PG.K_s]      : Mueve('I')

 ev = PG.event.get()
 for e in ev:
  if e.type == QUIT           : lOK = False
  if e.type == PG.MOUSEMOTION : nMx,nMy = e.pos
  if e.type == PG.MOUSEBUTTONDOWN and e.button == nBTN_LEFT:
               xm1,ym1 = UpDate_Scroll_Mapa(nMx,nMy)
               xm2,ym2 = UpDate_Scroll_Mapa2(nMx,nMy)
               xm3,ym3 = UpDate_Scroll_Mapa3(nMx,nMy)

 Pinta_Panta()
 Pinta_Mapas()
 Pinta_Mmapa()
 Pinta_Regla()
 Pinta_Mouse()
 PG.display.flip()
 aClk[0].tick(100)

PG.quit






