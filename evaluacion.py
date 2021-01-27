"""
Alumna: Brito Barredo Ingrid Dumary
NoControl: 18390017

Line intersecting a Triangular Plane
"""
import numpy as np
import matplotlib.pyplot as plt
from math import cos,sin,radians,sqrt #o usar lo que ya trae numpy
import tools3D as Tools


#----------Lista de coordenadas iniciales
xg=[]
yg=[]
zg=[]

#-----------Centro
xc=80
yc=40
zc=40

#Coordenadas del sistema local plano y la linea
x=[]
y=[]
z=[]

def plotSquareLine(x,y,z,xg,yg,zg,hpx,hpy):
    x=[40,30,80,hpx] #-----Integre la asignacion de las coordenadas aqui Debido a que el hitpoint o coordenada 3 es dada por el usuario
    y=[60,10,60,hpy] 
    z=[0,0,0,0]
  
    for i in range(len(x)):
        xg.append( x[i]+xc )
        yg.append( y[i]+yc )
        zg.append( z[i]+zc )
    

    plt.axis([0,250,200,0])
    plt.axis('on')
    plt.grid(True)

    plt.text(xg[3]+5,yg[3]+5,'Hitpoint')
    plt.text(xg[3],yg[3],'3')
    plt.text(xg[0],yg[0],'0')
    plt.text(xg[2],yg[2],'2')
    plt.text(xg[1],yg[1],'1')
    
    plt.plot([xg[0],xg[2]],[yg[0],yg[2]],color='k')#ploteo del plano o triangulo A
    plt.plot([xg[2],xg[1]],[yg[2],yg[1]],color='k')
    plt.plot([xg[1],xg[0]],[yg[1],yg[0]],color='k')

    plt.plot([xg[3],xg[0]],[yg[3],yg[0]],color='steelblue')#ploteo del plano A2
    plt.plot([xg[3],xg[1]],[yg[3],yg[1]],color='steelblue')
    plt.plot([xg[1],xg[0]],[yg[1],yg[0]],color='steelblue')

    plt.plot([xg[0],xg[2]],[yg[0],yg[2]],color='g')#ploteo del plano A1
    plt.plot([xg[3],xg[2]],[yg[3],yg[2]],color='g')
    plt.plot([xg[3],xg[0]],[yg[3],yg[0]],color='g')


     #-----la distancia entre puntos  
    d01=( (x[0]-x[1])**2 + (y[0]-y[1])**2 )**(0.5)
    d12=( (x[1]-x[2])**2 + (y[1]-y[2])**2 )**(1/2)
    d20=( (x[0]-x[2])**2 + (y[0]-y[2])**2 )**(1/2)
    d13=( (x[1]-x[3])**2 + (y[1]-y[3])**2 )**(1/2)
    d30=( (x[3]-x[0])**2 + (y[3]-y[0])**2 )**(1/2)
    d32=( (x[3]-x[2])**2 + (y[3]-y[2])**2 )**(1/2)

    #-------calculamos el semiperimetro de cada triangulo
    sa=(d01+d12+d20)/2
    sa1=(d01+d13+d30)/2
    sa2=(d20+d30+d32)/2

    #-------calculamos el area de cada triangulo
    #____Triangulo A
    a1=sa*(sa-d01)*(sa-d12)*(sa-d20)
    AreaA=(a1)**(1/2)
    #____Triangulo A1
    AreaA1=(sa1*(sa1-d01)*(sa1-d13)*(sa1-d30))**(1/2)
    # ____Triangulo A2
    AreaA2=(sa2*(sa2-d20)*(sa2-d30)*(sa2-d32))**(1/2)

#___________-ETIQUETAS DE LAS AREAS
    plt.text(10,150,'Area del T1 es: ' + str(AreaA),color ='k')
    plt.text(10,160,'Area del T2 es: ' + str(AreaA1),color='g')
    plt.text(10,170,'Area del T3 es: ' + str(AreaA2),color ='steelblue')
    AT=AreaA2+AreaA1
    plt.text(10,180,'T2 + T3 = ' + str(AT))

#___________DEFINIMOS SI EL HITPOINT ESTA IN o OUT
    if(AreaA1+AreaA2 > AreaA):
        plt.text(10,10,'OUT: EL HITPOINT ESTA FUERA DE LOS LIMITES',color ='r')
        plt.scatter(xg[3],yg[3],s=20,color='red') #marco el hitpoint
    elif (AreaA1+AreaA2 < AreaA):
        plt.text(10,10,'IN: EL HITPOINT ESTA FUERA DE LOS LIMITES',color ='r')
        plt.scatter(xg[3],yg[3],s=20,color='yellow') #marco el hitpoint


    plt.title("Line intersecting a Triangular Plane")
    plt.show()

      

#--------plotear la figura 
 
while True:
    axis=input('Press any key to define the hitpoint coordinates. Pulse 18390017 to exit: ')
    if axis=='18390017':
        break
    elif axis!="":
        hpx=(float(input('Coordinate X: ')))
        hpy=(float(input('Coordinate Y: ')))
        plotSquareLine(x,y,z,xg,yg,zg,hpx,hpy)


