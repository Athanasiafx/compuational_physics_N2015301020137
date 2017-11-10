# Exercise 3.31
Study the behavior for other types of tables.One interesting possibility is a square table with a circular interior wall located either in the center,or slighthy off-center.Another possibility is an elliptical table.
## 1、题目背景-台球模型
书中给出了在矩形边界内碰撞的例子,我们要讨论的是其他种类的桌面上，小球的运动状态。
![1-1](https://github.com/Athanasiafx/compuational_physics_N2015301020137/blob/master/Exercise_09/eg11.png)
![1-2](https://github.com/Athanasiafx/compuational_physics_N2015301020137/blob/master/Exercise_09/eg12.png)
![1-3](https://github.com/Athanasiafx/compuational_physics_N2015301020137/blob/master/Exercise_09/eg13.png)
## 2、公式
> * 因为不考虑摩擦损耗，小球的碰撞可以看做是完全弹性的，此时速度不变。所以有
> ![fomula1](https://github.com/Athanasiafx/compuational_physics_N2015301020137/blob/master/Exercise_09/fomula1.png)
> * 在碰撞点，速度的垂直分量和水平分量分别为
![fomula2](https://github.com/Athanasiafx/compuational_physics_N2015301020137/blob/master/Exercise_09/fomula2.png)
> * 反射后的速度关系
![fomula3](https://github.com/Athanasiafx/compuational_physics_N2015301020137/blob/master/Exercise_09/fomula3.png)

### 3、计算机模拟
> 本实验通过Vpython模拟。

> (1) 圆形边界
> ![gif1](https://github.com/Athanasiafx/compuational_physics_N2015301020137/blob/master/Exercise_09/gif1.gif)
> 平面图
> ![pingmian](https://github.com/Athanasiafx/compuational_physics_N2015301020137/blob/master/Exercise_09/pingmian.png)
> 在y=0扫描的相空间图像
> ![xkj](https://github.com/Athanasiafx/compuational_physics_N2015301020137/blob/master/Exercise_09/y0xkj.png)
> 可见轨迹是对称的，是一个周期性系统而不是混沌系统。

> (2) 圆环形边界
> ![huan](https://github.com/Athanasiafx/compuational_physics_N2015301020137/blob/master/Exercise_09/yuanhuan.png)
> 仍是一个周期性系统。

## 4、[代码](https://github.com/Athanasiafx/compuational_physics_N2015301020137/blob/master/Exercise_09/code1.py)

## 5、结论
当桌面对称性很大的时候桌球周期性比较明显

