# Exercise 3.26
continue the previous problem,and construct the phase-space plots as in Figures 3.16 and 3.17 in the different regimes.
## 实验报告
姓名：方昕
学号：2015301020137 
### 1、题目背景-洛伦兹模型
Lorenz系统作为第一个混沌模型，是混沌学发展史上的一个重要的里程碑，具有举足轻重的地位。
   
气象学家洛伦兹在1963年论文中提出的它的公式以表示天气模型。天气系统如此复杂，用数百万个变量来描述都不为过，但洛仑兹将其压缩到了三个变量：x，y和z，所以这只是一个玩具模型。这个玩具模型并不能准确的预测，只是一个十分简化的理论模型，但是对于他的论点来说，也许恰到好处。之前的天气模型大多是线性的，没有过多考虑各种因素之间的复杂关系，洛伦兹早认为这样的模型无法描述多变的天气。而他的模型，尽管只有三个随着时间变化的变量，但变量之间却有着非线性的联系，能够很好地诠释了因素之间的相互影响。

![chaos](https://github.com/Athanasiafx/compuational_physics_N2015301020137/blob/master/Exercise_07/chaos.png)

就在这样简单的Lorenz模型之下，出现了混沌现象。而且这种现象似乎是普遍的，因为在三个变量取值的大部分可能性下，系统演变的轨迹都会渐渐趋近于同一个产生混沌的区域，就像磁铁吸引着图钉，混沌的行为成为了必然。这就是人们发现的第一个混沌吸引子：洛伦兹吸引子。它的形状，就像一只蝴蝶；这大概也是洛伦兹将这种混沌的现象称为“蝴蝶效应”的原因。一只南美洲蝴蝶的扑翼，在蝴蝶效应的放大下，也许引起德克萨斯州的一场飓风。天气不可能准确预测，因为天气是混沌的，微小的扰动在长远看来是不可忽略的，而我们又无力去追踪无数的扰动，只能一边预计，一边修正。

### 2、公式
![CodeCogsEqn](https://github.com/Athanasiafx/compuational_physics_N2015301020137/blob/master/Exercise_07/CodeCogsEqn.png)

其反映了速度、温度、密度变量随时间演化的规律，其中r是表示温差影响，x，y，z分别表示流体温度、密度、速度。
温差是流体系统中的驱动力。虽然该模型简单适用于任何实际的sysytems，但这些方程中的行为表现为其他更复杂系统中的行为类型的指示。
这就是为什么我们研究混沌，我们不能完全模拟，但我们可以得到简化的版本，并获得对问题的有价值的见解。

### 3、计算机模拟
观察不同r值下的流体状态的演化。
由于Lorenz模型对r的依赖较为明显，试验中，我们只改变r值，在不同的r值下做出速度z随时间变化的曲线：

![first](https://github.com/Athanasiafx/compuational_physics_N2015301020137/blob/master/Exercise_07/model.png)

r =5时，有一个快速衰减，z稳定为一个常数。
r =10，衰减需要更长的时间。这两种情况对应于原始流体中的稳态对流运动。
但随着r上升，这意味着温度差变得越来越大，稳定的对流将转向混沌行为，转折点恰好是470/19，所以可以在r =25处看到完全不同的现象。

相空间图模拟

r=5

![r5](https://github.com/Athanasiafx/compuational_physics_N2015301020137/blob/master/Exercise_07/r5.png)

r=10

![r10](https://github.com/Athanasiafx/compuational_physics_N2015301020137/blob/master/Exercise_07/r10.png)

r=25

![r25](https://github.com/Athanasiafx/compuational_physics_N2015301020137/blob/master/Exercise_07/r25.png)


