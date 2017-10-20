# EXERCISES 2.19
  Model the effect of backspin on the range of a batted ball.Assume an angular velociy of 2000 rpm.
## 实验报告
姓名：方昕 学号：2015301020137

### 1、题目背景
    棒球在空中运动时会同时受重力和空气阻力的作用,如果棒球运动时伴随自旋，呈现的运动轨迹将会复杂多变。
    此题中先不考虑空气阻力，只考虑棒球受到重力影响，在初始情况有自旋角速度的情况下的运动。
    这时棒球旋转将使其受到额外的Magnus力，因而棒球的轨迹会变得十分复杂。
### 2、公式推导
$$\vec{F}=S_{0}\vec{\omega}\times\vec{v}$$
$$\frac{d_{x}}{d_{t}}=v_{x}$$
$$\frac{dv_{x}}{d_{t}}=-\frac{B2}{m}vv_{x}$$
$$\frac{dy}{dt}=v_{y}$$
$$\frac{dv_{y}}{dt}=-g$$
$$\frac{dz}{dt}=v_{z}$$
$$\frac{dv_{z}}{dt}=-\frac{S_{0}v_{x}\omega }{m}$$
### 3、图片模拟
通过matplotlib模拟运行轨迹
假设棒球半径为0.1m并且角速度为2000rpm，沿着X轴正方向运动，初速度为31m/s。
运行代码，用matplotlib得到在三维情况下的运行轨迹如图,其中红色为 起始位置，黑色为最终位置:
![battedball](https://pan.baidu.com/s/1nv9R2kD)
### 4、[代码](https://github.com/Athanasiafx/compuational_physics_N2015301020137/blob/master/Exercise_05/code.py)
### 5、总结
从图中可以初始情况存在自旋时可以看到有明显的偏移。本次作业主要模拟了棒球在忽略空气阻力情况下Magnus力对棒球运动的影响。在之前习题中我们已经知道，空气阻力对抛体运动射程的影响极大其中前者的影响极为显著，并且明显地改变被抛射物体的轨迹，然而通过本次作业可以发现棒球初始时自旋对棒球轨迹也有很大影响，棒球旋转方向不同，其偏移也会发生变化。通过查阅资料可以得出结论：棒球在自旋方向一定的情况下，自旋速度的变化也会使得棒球偏移量不同。通过控制自旋方向和出手时的自旋速度可以在一定程度上控制棒球运动轨迹。
