import pandas as pd
import numpy as np

import time


print("leyendo CSV")
laberin = pd.read_csv("laberinto1.txt", sep=" ", header = None)
#print(laberin)
#print(np.asarray(laberin)

class laberinto():
  def __init__(self,lab):
    self.lab=lab # laberinto completo
    self.inii=[] #inicio del laberinto
    self.fin=[]  #fin del laberinto
    self.fil = len(lab) #filas laberinto
    self.col = len(lab[0]) #columnas laberinto
    self.cel = np.zeros((self.fil * self.col)) # celd ocupadas
    self.porc = 0 #porcentaje de conocimiento 
    self.encontrar()

  def print_cel(self):
    cont = 0
    for n in range(self.fil):
      for m in range(self.col):
         print(int(self.cel[cont])," ", end='') 
         cont += 1
      print()   
    print()   

  def encontrar(self):
    labe = self.lab
    for i in range(self.fil):
      for j in range(self.col):
        if labe[i][j] == 'A':
          self.inii=[i,j]
        elif labe[i][j] == 'B':
          self.fin = [i,j]
        if self.inii != [] and self.fin != []:#detener el codigo evitar itera innecesa
          return(False)

  def llenar_cel(self, i, j, cl):# marcar 1 _ A marcar 2 #
      self.cel[(i*self.col)+j]=cl 
      cont = 0
      for elem in self.cel:
        if elem != 0:
          cont += 1
      self.porc = 100 * cont / (self.fil * self.col)    
      

  def vecinos(self,i,j,seguimiento):
    cord = []
    for v in range(i-1,i+2):
      for d in range(j-1,j+2):
        if v>=0 and d>=0 and v < self.fil and d< self.col:
         #print(v,d)
         elem = self.lab[v][d]
         if elem == '_' or elem == 'A' or elem == 'B':
           self.llenar_cel( v, d, 2)
           if elem != 'A':
              cord.append([v,d])
              
         elif elem == '#':
           self.llenar_cel( v, d, 1)
    #print("l57 el porcentaje es =",self.porc,cord)
    print('=>',cord)
    if cord != []:
       x,y = self.ele_cam(cord,i,j) 
       if x == self.fin[0] and y == self.fin[1] :
         print('😊 ha llegado a la meta')
         return(x,y,[])  
    else:
      
      print('Cord vacio')
      x,y,seguimiento = self.regresar(seguimiento)  
      print('2:',seguimiento)  
    return(x,y,seguimiento) 

  def regresar(self,seguimiento):
    print('1:',seguimiento)
    print('1.1:',seguimiento[-1])
    paso_anterior=seguimiento[-1]
    self.lab[paso_anterior[0],paso_anterior[1]]='X'
    pos_ante = seguimiento[-2]
    seg_menos = seguimiento[:-2]
    #print('Hola',pos_ante[0],pos_ante[1])
    return(pos_ante[0],pos_ante[1], seg_menos)  

  def ele_cam(self,cord,i,j):
    #print("l62 ele ",cord,i,j)
    for k in cord:
      kx,ky = k
      #print("l65 ",k,kx,ky,i,j)
      if kx == i and ky != j:
        x,y = k
        #print("l68 prim",x,y)
        return(x,y)
      elif kx != i and ky == j:
        x,y = k
        return(x,y)

  def rev_cel(self,i,j):
    cel = self.cel[(i*self.col)+j]
    #print("l75 rev_cel",cel)
    if cel ==1 or cel==2 :
      return(False)
    else:
      return(True)  

  def new_pos(self,x,y):
    # A=>inii
    # self.lab[self.inii[0],self.inii[1]] = '_'
    self.lab[x,y]='A'

  def printt(self):
     for i in range(self.fil):
       for j  in range(self.col):
         elem = self.lab[i][j]
         if elem == '#':
           print("▓▓",end='')  
         elif elem == '_':
           print("  ",end='') 
         elif elem == 'A': 
           print("😊",end='')  
         elif elem == 'B':
           print("🎁",end='') 
         elif elem == 'X':
           print("❌", end='')  
       print('')    

class jugador():
   def __init__(self,i,j):
     self.i = i
     self.j = j 
     self.seguim = []
     self.mover(i,j)

   def mover(self,x,y):
     self.i = x
     self.j = y 
     self.guardar_pos(x,y)

   def guardar_pos(self,x,y):
       self.seguim.append([x,y])
       #print("seguimiento ",self.seguim)

laber = laberinto(np.asarray(laberin))
#print(laber.fin)
jg = jugador(laber.inii[0], laber.inii[1])
laber.printt()
#laber.print_cel()
laber.llenar_cel(laber.inii[0], laber.inii[1],2)
#laber.print_cel()
#print("pre pos jg ",jg.i, jg.j)
x, y,jg.seguim = laber.vecinos(jg.i, jg.j,jg.seguim)
cont = 0
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
while x!=  laber.fin[0] or y!= laber.fin[1]:
  #print("inicia un nuevo ",x,y)
  jg.mover(x,y)
  laber.new_pos(x,y)
  laber.printt()
  #print("pos jg ",jg.i, jg.j)
  x, y,jg.seguim = laber.vecinos(jg.i, jg.j,jg.seguim)
  #laber.print_cel() 
  cont += 1
  time.sleep(1)
  print()
  print()
  print()
  print()
  print()
  print()
  print()
  print()
  print()
  if cont > 60:
    x = laber.fin[0]
    y = laber.fin[1]
# genera el camino pero se detiene cuando esta la pared no sabe que hacer de ahí en adelante