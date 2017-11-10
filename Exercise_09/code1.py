动画【1】
from visual import *
from math import *

shape=Polygon([(-0.5,-0.5),(-0.5,0.5),(0.5,0.5),(0.5,-0.5)])
path=paths.arc(radius=20.5,angle2=2*pi)
tableup=extrusion(pos=path,shape=shape,material=materials.wood,color=color.green)
tabledo=cylinder(pos=(0,-1,0),axis=(0,1,0),material=materials.wood,radius=20)
ball=sphere(pos=(2,0.5,0),radius=0.5,color=color.yellow,make_trail=True,material=materials.emissive)
ball.tho=1
ball.the=0
ball.vtho=sqrt(2)
ball.vthe=pi/4
ball.vx=taiqiu.vtho*cos(taiqiu.vthe)
ball.vz=taiqiu.vtho*sin(taiqiu.vthe)
dt=0.01
while True:
    rate(10000)
    
    if ball.x**2+ball.z**2>400:
        ball.vthe=pi-ball.vthe+2*ball.the
    
    ball.vx=ball.vtho*cos(ball.vthe)
    ball.vz=ball.vtho*sin(ball.vthe)
    
    ball.x=ball.x+ball.vx*dt
    ball.z=ball.z+ball.vz*dt
    ball.tho=sqrt(ball.x**2+ball.z**2)
    ball.the=arctan(float(ball.z/ball.x))
    
    
动画【2】
from visual import *
shape=Polygon([(-0.5,-0.5),(-0.5,0.5),(0.5,0.5),(0.5,-0.5)])
path1=paths.arc(radius=4.5,angle2=2*pi)
path2=[(10.5,0,10.5),(10.5,0,-10.5),(-10.5,0,-10.5),(-10.5,0,10.5),(10.5,0,10.5)]
table1=extrusion(pos=path1,shape=shape,material=materials.wood,color=color.red)
table2=extrusion(pos=path2,shape=shape,material=materials.wood,color=color.green)
table3=box(pos=(0,-1,0),size=(20,1,20),material=materials.wood)

ball=sphere(pos=(7.5,0.5,0),radius=0.1,color=color.yellow,make_trail=True,material=materials.emissive)
ball.tho=1
ball.the=0
ball.vtho=1
ball.vthe=pi/12
ball.vx=ball.vtho*cos(ball.vthe)
ball.vz=ball.vtho*sin(ball.vthe)dt=0.001
while True:
    rate(10000)
    if ball.x**2+ball.z**2<=25:
        ball.vthe=pi-ball.vthe+2*ball.the
        while ball.vthe>=2*pi:
            ball.vthe-=2*pi
        while ball.vthe<=0:
            ball.vthe+=2*pi
        ball.vx=ball.vtho*cos(ball.vthe)
            ball.vz=ball.vtho*sin(ball.vthe)
    if ball.x>=10:
        ball.vx=-ball.vx
        ball.vthe=pi
    if ball.x<=-10:
        ball.vx=-ball.vx
        ball.vthe=0
    if ball.z>=10:
        ball.vz=-ball.vz
        ball.vthe=3*pi/2
    if ball.z<=-10:
        ball.vz=-ball.vz
        ball.vthe=pi/2
        
    ball.x=ball.x+ball.vx*dt
    ball.z=ball.z+ball.vz*dt
    ball.tho=sqrt(ball.x**2+ball.z**2)
    ball.the=arctan(float(ball.z/ball.x))
