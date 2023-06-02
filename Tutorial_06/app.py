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
    aImg.append(Load_Image('mm3.png',False )) #Minimapa2(esta imagen corresponde a la que usamos en el minimapa 2 esto nos permitira cargarla en pantalla mas adelante)
    aImg.append(Load_Image('mm2.png',False )) #Minimapa3(esta imagen corresponde a la que usamos en el minimapa 3 esto nos permitira cargarla en pantalla mas adelante)
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
    sPanta.blit(aSprt[12],(820,8))#pintamos en su posision los minimapas esto usando su posision en la lista  que almacena las imagenes
    sPanta.blit(aSprt[13],(820,320))#los minimapas 1 y 3 estan a la misma distancia x en el display por lo que estos solo difieren en la posision de y siendo que el minimapa 3 esta mas abajo que el 1
    sPanta.blit(aSprt[14],(244,244))#los minimapas 1 y 3 son distintos a el mini mapa 2 en su forma y posision por ende al calcular la posision que usara valorres distintos
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
    xm1 = 0 ; ym1 = 0
    if nMx in range(820,952): # Si nMx esta en el rango de 820 a 952
       if nMy in range(8,105): # y nMy esta en el rango de 8 a 105
          xm1 = int(3840*(nMx-820)/float(132)) # Calcula la coordenada x del mapa
          ym1 = int(1920*(nMy-8)/float(97)) # Calcula la coordenada y del mapa
          PG.display.set_caption('[Coord Mapa]-> X: %d1 - Y: %d1' %(xm1,ym1))
          if xm1 >= 3243: xm1 = 3243 # Si xm1 es mayor o igual a 3243, establece xm1 en 3243
          if ym1 >= 1616: ym1 = 1616 # Si ym1 es mayor o igual a 1616, establece ym1 en 1616
    return xm1,ym1  # Devuelve las coordenadas del mapa
#---------------------------------------------------------------------
# update mapa_2
#---------------------------------------------------------------------
def UpDate_Scroll_Mapa2(nMx,nMy):
    xm2 = 0 ; ym2 = 0
    if nMx in range(245,345):# Verificar si nMx esta en el rango de 245 a 345
       if nMy in range(245,437):# Verificar si nMy esta en el rango de 245 a 437
          xm2 = int(1920*(nMx-245)/float(97))# Calcular xm2 e ym2
          ym2 = int(1920*(nMy-245)/float(160))
          PG.display.set_caption('[Coord Mapa]-> X: %d1 - Y: %d1' %(xm2,ym2))
          if xm2 >= 1616: xm2 = 1616# Si xm2 es mayor o igual a 1616, establecer xm2 en 1616
          if ym2 >= 1616: ym2 = 1616# Si ym2 es mayor o igual a 1616, establecer ym2 en 1616
    return xm2,ym2# Devolver los valores de xm2 e ym2
#---------------------------------------------------------------------
# update mapa_3
#---------------------------------------------------------------------
def UpDate_Scroll_Mapa3(nMx,nMy):
    xm3 = 0 ; ym3 = 0  # Inicializa las variables xm3 e ym3 en cero.
    if nMx in range(820,917):  # Si nMx esta en el rango de 820 a 917:
        if nMy in range(320,512):  # Si nMy esta en el rango de 320 a 512:
          xm3 = int(1920*(nMx-820)/float(132))  # Calcula xm3.
          ym3 = int(3840*(nMy-320)/float(97))  # Calcula ym3.
          PG.display.set_caption('[Coord Mapa]-> X: %d1 - Y: %d1' %(xm3,ym3))
          if xm3 >= 3243: xm3 = 3243# Si xm3 es mayor o igual a 3243 Establece xm3 en 3243.
          if ym3 >= 1601: ym3 = 1601# Si ym3 es mayor o igual a 1601 Establece ym3 en 1601.
    return xm3,ym3# Devuelve los valores de xm3 e ym3.
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






