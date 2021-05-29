# Tyro Learning Note 菜鸟笔记

## Directed by 施伟琦

<br />

## 程序语言
### 导入函数
import 导入函数库之类的  
```python
import numpy as np
import pandas as pd
```
### 数据类型
1、number：数值类型   （就是数字，支持int\float\bool\complex类型）

1,2,3,4,1.2e


2、str：字符串类型   （是有数字、字母、下划线组成的一串字符，用于对应显示当中的数据。创建方法：通过用引号括起来的一串字符用“=”指向一个变量）


a = "object"


3、list: 列表  （有序、可变的序列集合。创建方法：将所有的元素放在[ ] 并用“=”指向一个变量即创建了一个列表）


list_su = [ 1,2,3,4,'name','password']


4、tuple：元组   （不可变的list有序序列，一旦创建无法修改。创建方式：将所有元素放在 （）当中并用“=”指向一个变量）


tup_m = ( 23,34,45,'a','b')


5、set : 集合   （是python基本的数据类型之一，分为可变set（）和不可变（frozenset）两种，一般应用比较少）


6、dict：字典   （基于哈希表存储键值对的一种映射机构数据类型。 创建方式：将键值对元素放入{ }当中并用“=”指向一个变量）


dic = { 'name1': 123 , 'name2':456 , 'name3':789 }
### 定义函数
def 函数名(自变量1，2，.....)  定义一个函数(函数名随意)

为了不与函数库的函数名冲突，可在前加my_
```python
def my_tran(m)
def swq(a, b, c)
```

### 关于print和%
print("")  输出你想要的结果(括号里有引号输出的是引号里的东西，也就是字符串，括号里无引号输出的东西与前面的逻辑有关，也就是会输出变量)

如果想在输出的字符串里调用变量的值，就可以用%
```python
i=1
print("我拿到了%s个"%i)
# 我拿到了1个
# %和i不是一个整体，%相当于一个分隔符
```



### if逻辑

if elif else  是在定义了一个函数之后的下一层逻辑(注意不同层次的逻辑用":"区分)



if的判断里，只要不是0就是真的
```python
def tran(m):
    if m==1:
        print("Jan")
    elif m==2:
        print("Feb")
    elif m==3:
        print("Mar")
    elif m==4:
        print("Apr")
    elif m==5:
        print("May")  
    elif m==6:
        print("Jun") 
    elif m==7:
        print("Jul") 
    elif m==8:
        print("Aug")
    elif m==9:
        print("Sept")
    elif m==10:
        print("Oct")
    elif m==11:
        print("Nov")
    elif m==12:
        print("Dec")
    else:
        print("error")
m=5
tran(m)
```

return res   返回res这个计算结果，例如可以把res设置成加减乘除的计算
```python
def calc(a, b, n):
    if n==1:
        res=a+b
    elif n==2:
        res=a-b
    elif n==3:
        res=a*b
    elif n==4:
        res=a/b
    else: 
        res=-1
        print("error")
    return res
res=calc(5, 7, 2)
print(res)
```

### for循环结构
l=[1, 2, 3, 4]中  l[ 0 ]=1   l[ 1 ]=2,以此类推

l=[[3, 5, 7], [1, 4, 6,], [6, 2, 8]]中每一个小中括号都代表一个一个list，所以如果有命令，会按照顺序一个个算，第一个l[ 0 ]=3,l[ 1 ]=5,l[ 2 ]=7

for x in[  ]  就是把中括号的的对象分配给x，一次一个，然后为每个x值执行命令

```python
def calc(a, b, n):
    if n==1:
        res=a+b
    elif n==2:
        res=a-b
    elif n==3:
        res=a*b
    elif n==4:
        res=a/b
    else: 
        res=-1
        print("error")
    return res
for l in[[5, 7, 2], [3, 8, 6],[2, 8, 0]]:  
    a = l[0]
    b = l[1]
    n = l[2]
    res = calc(a, b, n)
    print(res)
```
```python
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print ('%d 等于 %d * %d' % (num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print(num, '是一个质数')
# 第一个循环，num从10开始，进入第二个循环，i从2开始，能够整除，则输出10=2*5 并且跳出第二个循环
# 接着num变成了11，遍历了第二个循环中的所有数都不能整除，输出num是一个质数
# 再接着第一个循环num变成了12，以此类推
# 注：只要满足了整除就跳出循环，所以不用怕遍历第二个循环中的所有数
```

### while循环结构
只要给定条件的值为true, while循环就会执行未知次数的语句。

在执行语句之前先评估条件。 如果条件评估为真，则执行。 否则，如果条件评估为false，则循环终止，并将程序控制传递给后面的语句。

break语句终止当前循环，并将程序控制权传递给终止循环之后的语句。 最常见的情况是在满足特定条件时使用break终止循环。

Continue语句退出循环的当前迭代，并将程序控制传递给循环的下一个迭代

```python
i=0
while i<10:
    i+=1
    print("num:", i)
# i从0开始，先判断i<10 这个条件，为真执行下面的语句，i=i+1，并且输出当前的i值

# 注：此时的print在while的逻辑下面，所以会输出每一次循环迭代的值，如果print和while在同一层逻辑，则只输出最后一次循环迭代的值



i=0
while i<10:
    i+=1
    if i==6:
        break
    print("num:", i)
# break即终止当前循环，当i=5 时，i+1=6，if的判断为真，终止，所以只能输出1-5 的值


i=0
while i<10:
    i+=1
    if i==6:
        continue
    print("num:", i)
# continue表示当if的判断为真时，退出此时的迭代，直接返回循环开头重新迭代，即i=6 并不输出


i=0
while i<10:
    i+=1
    if i==6:
        break
    print("num:", i)
else:
    print("qwer")
# 由于i=6 时循环终止，所以不会出现i>10 的情况，else的语句不执行




while True:
    i=input("你觉得呢:")
    if i=="我觉得你说的对":
        break
# 这是无限while循环，只有当输入为 我觉得你说得对 时，循环才终止

```



### list常用增删
（1）添加
```python
my_list=[1, 2, 3, "A", "B", "C"]
my_list.append(4)
print(my_list)
# 向列表末尾添加'4'
# [1, 2, 3, A, B, C, 4]


my_list.extend(["X", "Y", "Z"])
print(my_list)
# 向列表末尾添加新列表
# [1, 2, 3, 'A', 'B', 'C', 4, 'X', 'Y', 'Z']

my_list.insert(2, "apple")
print(my_list)
# 在索引2处插入'apple'
# [1, 2, 'apple', 3, 'A', 'B', 'C', 4, 'X', 'Y', 'Z'
```

（2）删除

```python
my_list = [1, 2, 3, "A", "B", "C"]
del myList[2]
# 删除索引2处的元素
# [1, 2, 'A', 'B', 'C']

del myList[0:2]
# 删除索引0到索引2(不包括索引2)的所有元素
# ['A', 'B', 'C']
```

### 关于“=”
一个"="意思是赋值，两个"=="意思是判断

```python
l1=[1, 32, 2, 24, 4]
res=min(l1)
print(res)

l1=[2, 21, 54, 21, 54, 12]
l2=[]
if l1[0]==min(l1):
    l2.append(l1[0])
```
### 关于range和arange
```python
range(1， 5)
>>>:[1, 2, 3, 4]
import numpy as np
np.arange(1, 5, 1)
>>>:array([1, 2, 3, 4])
# range返回的是一个list
# arange返回一个array对象，也就是数组，但是其中元素跟range一样
# arange中括号里三个数字分别代表起始值，终值，步长
```

### 关于np.linspace(主要用来创建等差数列)与np.random.uniform（随机均匀分布）

```python
import numpy as np
np.linspace(start, stop, num=50, endpoint=True, retstep=False, )
# "start"表示起始数值
# "stop"表示终止数值，所以输出的数一定是递增的
# "num"表示等分成多少份
# "endpoint"如果是True，则包括end的数，否则不包括
# "retstep"如果是True，则结果会给出数据间隔
# 默认输出的是array类型
>>> np.linspace(2.0, 3.0, num=5)
array([ 2.  ,  2.25,  2.5 ,  2.75,  3.  ])
>>> np.linspace(2.0, 3.0, num=5, endpoint=False)
array([ 2. ,  2.2,  2.4,  2.6,  2.8])
>>> np.linspace(2.0, 3.0, num=5, retstep=True)
(array([ 2.  ,  2.25,  2.5 ,  2.75,  3.  ]), 0.25)




np.random.uniform(low,high,size)
#产生具有均匀分布的数组,low起始值,high结束值,size形状
u = np.random.uniform(0, 10, (3, 4))
array([[9.83020867, 4.67403279, 8.75744495, 2.96068699],
    [1.31291053, 8.42817933, 6.59036304, 5.95439605],
    [4.36353698, 3.56250327, 5.87130925, 1.49471337]])
# 表示的是从0-10 范围里随机均匀取12个数，3组，每组4个数，也可以直接输入需要产生的样本数，比如10,100
# 当输入需要产生的样本数时，与np.linspace不同的是不是递增的数，所以如果画点线图在数据少的时候的线是会突然从小到大或者从大到小，数据大时画出来的是一个区域。



np.random.rand(d0,d1,d2,...,dn)
# 根据d0‐dn创建随机数数组，浮点数， [0,1)，均匀分布,属于均匀分布的特例
np.random.rand(2,2,3,4)
array([[[[0.3818632  0.99801152 0.8672531  0.16977651]
[0.59666817 0.1846709  0.89619537 0.5810534 ]
[0.57425433 0.55049493 0.88593566 0.97037169]]

[[0.68715174 0.7605472  0.82520771 0.56405194]
[0.45836909 0.15769316 0.50151969 0.55992049]
[0.11654268 0.81187865 0.40467584 0.01792217]]]


[[[0.34205273 0.92811353 0.36435182 0.53636628]
[0.39752732 0.92968223 0.49777968 0.62329687]
[0.38694952 0.76654153 0.78061539 0.2124096 ]]

[[0.37214718 0.34325525 0.1102437  0.0873236 ]
[0.28623688 0.45087316 0.3608912  0.40583037]
[0.81546176 0.7554547  0.37529309 0.96822229]]]])
```


### input函数
input函数是输入函数，当你在函数的括号内写下问题时，它会在终端打印出来等待你的输入，在你输入后，计算机会根据你的回答进行判断。

input函数接受一个标准输入数据，返回为string类型。不管我们输入的回答是什么，不管你输入的是整数，还是字符串，input()函数的输入值（搜集到的回答），永远会被【强制性】地转换为【字符串】类型。

在进行input函数的判断时，if 变量名==" "  输入的必须是字符串型，如果想要输入整数型，则可以在变量赋值时在input前面加上int（当我们想要的结果是数字的时候，例如年龄工资等）

字符串

```python
name=input('账号:')
# 终端会先出现  账号：
password=input('密码:')
# 终端再出现    密码：
if name=="agen" and password=='123':
    print('登陆成功')
else:
    print('登陆失败')
# 注意if后面的agen  123 的输入都是字符串型，否则会出现变量没有定义的情况
```

整数型

```python
age=int(input("你的年龄是："))
# 此时代表字符串型被转化成了整数型
if 0<age<18:
    print("A组")
else:
    print("B组")
# 所以if后面可以用整数型的判断
```

### 结合了input  if  for  while函数的简单代码

```python
name=input("用户名:")   #终端输入用户名
password=input("密码:") #终端输入密码
if name=="zhj" and password=="lefulan": #用户名和密码输入正确进入下一层
    def cdd(a,b):  #定义了一个自变量为a b 的函数
        if b>a:   #如果b大于a成立，进入for循环
            for i in range(1,15): #对于i从1开始到14，一个个给i赋值
                while i<10:  #判断i是否小于10，小于10则进入if语句
                    if i%3==0: #判断i除以3的余数是否为0，为0则执行下面的命令
                        print("chl叫了%s次爸爸"%i)#s随着i的变化而变化
                        break # 执行完之后退出while循环，继续for循环赋值
                    else:  #此命令在i除以3的余数不为0的情况下执行
                        print("chl泡了%s个妹妹"%i)
                        break #执行完之后退出此时while循环，继续for循环赋值
                else:  # 此命令在i大于10时执行
                    print("hjc拿了%s个offer请我吃饭"%i)
        else:  # 如果b大于a不成立，输出"请重新输入"
            print("请重新输入")
    cdd(3,7)
else:
    print("登陆失败")  #用户名和密码有一个不正确就登陆失败

# 假设用户名密码正确，7>3 首先i等于1，小于10判断为真，除以3余数不为0，所以执行while循环里的else语句，并且退出while循环，继续进入for循环，赋值为2，以此类推
# 当i赋值为10，while判断不为真，进入for循环的else语句，假设在else语句下输入break，则for循环结束，往后的11  12  13  14 将不会出现
```

### 关于linux系统命令
cd：进入用户主目录

cd ..:返回上一级目录

cd -:返回进入此目录之前所在目录

cd /:进入根目录

mkdir [目录名]：创建新目录

mkdir a:在当前目录下创建一个新的目录

mkdir a/{a1,a2}:在当前目录下的a目录下创建a1 a2目录

rm -rf:强制删除当前目录下的文件，"rm"是删除命令，"r"是一种递归特性，当目标为我文件夹时，删除文件夹下所有数据，"f"是强制特性，不需询问直接删除。

sudo:以系统管理者的身份执行指令

apt:提供了查找、安装、升级、删除某一个、一组甚至全部软件包的命令

sudo apt update:更新源

sudo apt install < >:安装指定的软件

sudo apt remove <  >:删除软件包

cp:复制文件或目录

cp -r test/newtest:当前目录test/下的所有文件复制到新目录newtest下,"-r"是一个参数，指的是若给出的源文件是一个目录文件，此时将复制该目录下所有的子目录和文件。

pip:用于下载安装一些基础包

pip install numpy/pandas/paramiko

### 关于画图
首先需要导入一个模块

```python
import matplotlib.pyplot as plt
```

1、plt.plot()  点线图

```python
plt.plot(x , y, format_string, **kwargs)
# x表示二维坐标中X轴数据
# y表示二维坐标中Y轴数据
# format_string表示可以设置的包括线条颜色、标识等
# **kwargs表示第二组或更多（x,y,format_string），也就是可以在一幅图中绘制多条曲线
import matplotlib.pyplot as plt
x= [0, 1, 2, 3, 4]
y= [2, 3, -1, 1, -2]
# x和y分别是相互对应的,如果涉及到幂次运算，则需要把list数据类型转变为array，如x=np.array(x)
plt.xlable("year")
# x轴坐标含义
plt.ylable("gdp")
# y轴坐标含义
plt.title("2021")
# 标题
plt.plot(n, m, 
         color = 'r',
         # "r"表示线条颜色是红色，可以用"y w b"等
         linestyle = ':',
         # ":"表示的是线条是虚线，可以用"-""-."等
         linewidth = 3,
         # "3"表示线条宽度
         marker = 's',
         # "s"表示实心方形标记，可以用"1 2 3 4 o"等
         markersize = 15,
         # "15"表示标识大小
         markeredgecolor = 'b',
        #  "b"表示标识的轮廓颜色
         markerfacecolor = 'r')
        #  "r"表示标识的填充颜色
plt.grid()   #显示坐标轴中的网格线，默认显示
plt.minorticks_on()   #在坐标轴上显示次刻度
plt.xlim(0,4)  # 设置x轴上下限
plt.ylim(-2,3)  # 设置y轴上下限
plt.xticks(np.arange(0 ,5, step=1))   # 设置x轴精准刻度
plt.lengend(loc="best")   # 图例放在最佳位置
plt.show()

```

2、plt.scatter()   散点图

```python
plt.scatter(x,y,s,c,marker)
# s表示散点图标的大小，默认为20
# c表示颜色
x=[2, 4, 5, 1, 8]
x=np.array(x)
# 将x转变为可以进行幂次运算的array数据类型
plt.figure()
plt.xlabel("t")
plt.ylabel("v")
plt.title("guess")
plt.scatter(x, x**3, s=50, c="b", marker="X",label="heihei")
#label表示图例
plt.legend(loc="best")  #使得图例处于最佳位置
plt.show()
```

3、plt.fill_between()  用颜色填充两条曲线之间的区域

```python
plt.fill_between(x,y1,y2,facecolor="",alpha=)


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0, 3*np.pi, 0.01)
# x从0-3 pi，间距为0.01
y1=np.cos(x)
y2 = np.sin(x)
plt.figure()
plt.xlabel("x")
plt.ylabel("y")
plt.title("2021")
plt.plot(x,y1,"rs-",label="gaga")
plt.plot(x,y2,"go-")
# 用不同的颜色画出sinx和cosx两条曲线
plt.legend(loc="best")
plt.fill_between(x,y1,y2,where=(2.1<x) & (x<3.5),facecolor="blue",alpha=0.3)
# "x"参数表示覆盖的区域，表示整个x都覆盖
# "y1"参数表示覆盖的下限是y1这条曲线
# "y2"参数表示覆盖的上限是y2这个曲线
# "where"参数表示填充的x的范围
# "facecolor"表示覆盖区域的颜色
# "alpha"表示覆盖区域的透明度[0,1],其值越大，表示越不透明
plt.fill_between(x,y1,y2,where=(5.7<x) & (x<7.9),facecolor="yellow")
plt.show()



# 实现数据高亮功能
import numpy as np
import matplotlib.pyplot as plt
x=np.array([i for i in range(30)])
y=np.random.rand(30)
# y是在0-1 中随机选取30个数
position=[[1,6],[12,14],[15,20]]
plt.plot(x,y,"ro-")
for i in position:
    plt.fill_between(x[i[0]:i[1]],0,1,facecolor="blue")
plt.show()
```


4、plt.errorbar()    画误差曲线
```python
plt.errorbar(x, y, yerr=None, xerr=None, fmt='', ecolor=None, elinewidth=None, capsize=None, capthick=None )
# x：横坐标的值，y：纵坐标的值，yerr：y值的误差范围，xerr：x值的误差范围
# fmt：数据点的标记样式以及相互之间连接线样式
# ecolor: 误差棒的线条颜色
# elinewidth: 误差棒的线条粗细
# capsize: 误差棒边界横杠的大小
# capthick: 误差棒边界横杠的厚度

import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(1,10,num=10)
# 1-10 分成10等分
y=np.sin(x)
plt.figure()
plt.errorbar(x,y,yerr=0.3,xerr=0.05,fmt="ro-",ecolor="green",elinewidth=3,capsize=2,)
plt.show()
```
### 蒙特卡洛模拟
原理：用计算机模拟的方法产生抽样结果，根据抽样计算参数值，根据模拟次数的增多提高参数值估计的准确性

1、用蒙特卡洛模拟的方法估计π值

```python 
import numpy as np
import matplotlib.pyplot as plt 
n = 10000 # num of throw 样本点的数目
# def a circle 定义一个圆
r = 1 # radius 半径是1
a = 0 # center 圆心是（0,0）
b = 0


# def a rectangular 定义一个矩形范围
x_min, x_max = a-r, a+r   # 此矩形的长是2r
y_min, y_max = b-r, b+r   # 此矩形的宽是2r

# random throw in the rectangular  随机将点撒在矩形中
x = np.random.uniform(x_min, x_max, n) # 在x的取值范围内撒n个点，随机均匀撒点
y = np.random.uniform(y_min, y_max, n) # 在y的取值范围内撒n个点，相当于有n个坐标

# calc distance between throw and center of the circle
d = np.sqrt((x-a)**2 + (y-b)**2) #计算这些点和圆心的距离

# num of throw in the circle
#res = sum(np.where(d<r, 1, 0))

res=0

for i in range(len(d)):
    if d[i] < r:
        res += 1
# 根据距离公式计算在圆里的点，一个有n个d，算出处于圆内的点的数目
# calc value of pi
pi = 4 * res / n
# 根据圆内点的数目比上总点数等于圆的面积比上矩形面积，近似求出π
print('approximate value of pi: ', pi)

# %%
plt.figure()
plt.plot(x, y, 'ro', markersize=1)
# 用红色圆点画出矩形区域内的n个随机点
plt.axis('equal')
# 保持坐标轴属性一致，也就是单位长度的距离一致

x_c = np.linspace(-r, r, 1000)
# 在-1 到1 之间分成1000等分
y_c = (r**2 - x_c**2)**(0.5)
# 对应的y值根据公式得出
plt.plot(x_c, y_c, 'b-')
# 画出上半部分圆
plt.plot(x_c, -y_c, 'b-')
# 画出下半部分圆
plt.show
```

2、用蒙特卡洛模拟计算y=x²在0-1的积分

```python
import numpy as np
import matplotlib.pyplot as plt 
n=10000  #样本点数目
x_min,x_max=0.0,1.0  # 构造一个长宽均为1的矩形
y_min,y_max=0.0,1.0
x=np.random.uniform(x_min,x_max,n)#在x取值范围内撒n个点，是随机均匀撒点
y=np.random.uniform(y_min,y_max,n)
res=0
for i in range(n):
    if x[i]**2>y[i]:#x和y都是array类型的数组，无法直接比较大小
        res+=1  #求出在x²下面的点的个数
jifen=res/n   #积分值就是x²下面的面积比上矩形面积，也就是x²下面的点的个数比上总数
print("积分值",jifen)
plt.figure()
plt.plot(x,y,"ro",markersize=1) 
plt.axis("equal")
x_c=np.linspace(0,1,10000) #在0-1之间把x分成10000等分，且这个数组的x值是递增的
y_c=x_c**2
plt.plot(x_c,y_c,"b-") #画出y=x²这个函数
plt.show()
# d=x**2-y   这是第二种方法，将d数组中的数与0比较，也可以得出答案
```



## 作业 
1、对两个有序数组重新排序

```python
l2=[92, 93, 96, 98, 101, 102, 103, 104]
l1=[91, 95, 97, 99, 100]
l3=[]
if l1[0]>=l2[0]:
    l3.append(l2[0])
else:
    l3.append(l1[0])
# 经过比较之后l3=[91]
if l2[0]==min(l2) and  l2[0]<=l1[1] and l2[0]<=l1[2] and l2[0]<=l1[3] and l2[0]<=l1[4]:
    l3.append(l2[0])
# 经过判断之后，为真，所以l3=[91,92]
order=0
# 相当于给order赋值一个0，下面的order+=1 表示order=order+1
for s2 in l2:
    order += 1
    if order<=len(l2)-1:
        for s1 in l1:
            if s1>=s2 and s1<=l2[order]:
                l3.append(s1) 
        l3.append(l2[order])                      
print(l3)
# 两个循环，外置循环表示order从1开始赋值
# 内置循环表示在order<l2长度减1的条件下，把l1中的每个数与l2中外置循环条件下的数比较
# 最开始的两步已经把91  92 排好了顺序
# 第一层，order=1，s2=92，符合开始内置循环的条件，s1中的每个数和92以及l2[order]比较，最终不符合添加s1的条件，所以添加s2[order],也就是93
# 第二层，order=2,s2=93......
```








2、对两个乱序数组重新排序

```python
l1=[12, 3, 57, 68, 30]
l2=[18, 4, 21, 1, 29]
l3=l1+l2                  
# l3就变成了【12， 3， 57， 68， 30， 18， 4， 21， 1， 29】
for i in range(len(l3)-1):
    for j in range(i+1,len(l3)):
        if l3[i]>l3[j]:
            l3[i],l3[j]=l3[j],l3[i]
print(l3)
# 有两个循环，外置循环代表i从0开始到8（range（9）代表0-8）
# 内置循环代表j从i＋1 开始到9，i和j都是代表l3的下标
# 第一层，当i=0 时，j从l3[1]开始到l3[9],分别和l3[0]比较，并把最小的放在前面
# 第二层，当i=1 时，j从l3[2]开始到l3[9],分别和l3[1]比较，找到剩下元素中最小的
```


3、如果：成绩>=90，那么：优秀，如果成绩>=80且<90,那么：良好，如果成绩>=70且<80,那么：普通，其他情况：很差，并且到很差的时候退出

```python
while True:
    score=int(input(">>>:"))
    if score>=90:
        print("优秀")
    elif score>=80 and score<90:
        print("良好")
    elif score>=70 and score<80:
        print("普通")
    else:
        print("很差")
        break
# score被强制转换成了整数，这是while无限循环的例子，只有分数小于70才会终止循环
```


4、猜身高，最多可以猜三次  

```python
i=1
while i<=3:
    height=178
    guess=int(input(">>>:"))
    if guess>height:
        print("太高了，可以猜3次，这是第%s次"%i)
    elif guess<height:
        print("太矮了，可以猜3次，这是第%s次"%i)
    else:
        print("恭喜你，答对了！")
        break
    i+=1
```

5、

```python
name='egon'
password='123'
while True:
    inp_name=input('用户名: ')
    inp_pwd=input('密码: ')
    if inp_name == name and inp_pwd == password:
        while True:
            cmd=input('>>: ')
            if not cmd:
                continue
            if cmd == 'quit':
                break
            print('run <%s>' %cmd)
    else:
        print('用户名或密码错误')
        continue
    break
# 有两个while的循环，第一层循环如果用户名和密码错误，则会执行else的语句并且一直重复输入用户名和密码

# 第二个while循环中，if not cmd表示的是  >>:   未输入任何东西，即not  cmd为真，执行continue的语句，返回循环最开始

# 如果输入了内容，但是内容不是quit，那就执行print的命令

# 注：无限while循环记得在最后输入break，否则会一直循环下去
```

6、升级版猜年龄问题要求：

允许用户最多尝试3次


每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y或y, 就继续让其猜3次，以此往复，不是就退出程序


如果猜对了，就直接退出 

```python
count=1
while True:
    if count<=3 :
        age=int(input('age:'))
        if age > 18:
            print('猜大了,可以重试3次，第 %s 次' %count)
        elif age < 18:
            print('猜小了,可以重试3次，第 %s 次' %count)
        else:
            print('猜中了，successful')
            break
        count += 1
    else:
        judge = input('是否继续(Y/N):')
        if judge in ['Y','y']:
            count = 1
        else:
            break
# 这是一个无限while循环，如果count大于3，执行else语句，如果输入了Y或者y，则需要重新给三次机会，所以最重要的就是重置count的值
```
