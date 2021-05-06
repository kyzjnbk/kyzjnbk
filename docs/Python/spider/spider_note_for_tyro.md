# Learning note of spider

## Directed by 施伟琦

## 基础知识
### 补充Urllib
#### 1.获得请求
```python
#-*-coding = utf-8 -*-
# httpbin.org    一个用来测试html请求 响应的网页

import urllib.request

# 获取一个get请求
response = urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))  #对获取到的网页源码进行utf-8解码



# 获取一个post请求
# 需要封装数据  用二进制的方式
import urllib.parse
data = bytes(urllib.parse.urlencode({'hello':'cyk'}),encoding='utf-8')
response = urllib.request.urlopen('http://httpbin.org/post',data=data) #post请求需要参数
print(response.read().decode('utf-8'))
```
#### 2.超时处理
```python
# 超时处理 在某个时间如果没有响应就采取相应措施，比如结束爬取
try:
    response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.01)  #get请求不需要参数
    print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
    print('time out!')
```
#### 3.获得某些信息
```python
response = urllib.request.urlopen('http://www.baidu.com') 
print(response.status)    # 会返回 200  叫做状态码
print(response.getheaders())  # 获得一些头部信息
print(response.getheader('Cache-Control'))   # 获得具体某个信息
```
#### 4.伪装成浏览器
```python
# 类似于豆瓣这样的网站不能直接请求，因为会被识破你是爬虫，所以需要封装一下，用浏览器去访问

# url = 'http://www.douban.com'
url = 'http://httpbin.org/post'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'


} 
# user-agent就是用户代理，也就是用户通过什么方式访问，我们需要把爬虫包装成浏览器
# 上面的内容来自于  用搜狗打开百度首页，fn+f12进入开发者模式，点network，找到最开始的蓝杠划到最下面
# 如果要伪装地更彻底，在键值对里面可以加入很多内容。例如accept
data = bytes(urllib.parse.urlencode({'hello':'swq'}),encoding='utf-8')
req = urllib.request.Request(url=url,data=data,headers=headers,method='POST') # POST要大写
# 这个req指数一个请求对象，像之前的是通过urlopen发出请求
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))


# 接下来用豆瓣做例子
url = 'http://www.douban.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'


} 
req = urllib.request.Request(url=url,headers=headers)   # 不是用的post就不用
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))
```

### 补充BS4
#### 简介
```python
# BeautifulSoup4  将复杂的html文档转换成一个复杂的树形结构，每个节点都是python对象，归为四种
# -Tag  
# -NavigableString
# -BeautifulSoup
# -Comment
from bs4 import BeautifulSoup
```
#### 1.Tag
```python
file = open('/home/lefulan/desktop/test/baidu.html','rb')  
# ./ 表示在当前文件夹 ,如果找不到文件，也可以用copy path寻找 'rb'表示read bytes
html = file.read()
bs = BeautifulSoup(html,'html.parser') # 用BS这个方法解析html，用的解析器是parser，并给到bs这个对象
print(bs.title)
print(bs.a)
print(bs.head)  # 返回的都是第一个捕获到的标签
print(type(bs.a))  # 得到的是bs4里元素的标签

# 1.Tag  标签及其内容；但是只能拿到他所找到的第一个内容
```
#### 2.NavigableString
```python
print(bs.title.string)
print(type(bs.title.string))

# 2.NavigableString   标签里的内容（字符串）

print(bs.a.attrs)  #得到一个标签里的所有属性，用字典呈现，里面的键值对就是属性
```
#### 3.BeautifulSoup
```python
print(type(bs))
# 3.BeautifulSoup  表示整个文档
print(bs)    # 就会出现整个文档的代码
```
#### 4.Comment
```python
print(bs.a.string)
print(type(bs.a.string))
# 4.Comment  是一个特殊的NavigableString，输出的内容不包括注释符号，即！-- --
```
#### 应用
```python
# 1.文档的遍历
print(bs.head.contents)  # 得到的是一个head标签里的内容并做成列表的形式
print(bs.head.contents[1])
```
```python
# 2.文档的搜索
# (1)find_all()  
# 字符串过滤：会查找与字符串完全匹配的内容，是一个list
t_list = bs.find_all('a')

# 正则表达式搜索：使用search()方法来匹配内容
import re 
t_list1 =bs.find_all(re.compile('a'))  # 只要标签里含有a，就把标签及其内容作为列表返回

# 方法：传入一个函数（方法），根据函数要求搜索

def name_is_existe(tag):
    return tag.has_attr('name')  #定义一个函数返回存在属性name的标签及其内容
t_list2 = bs.find_all(name_is_existe)
for item in t_list2:
    print(item)  # 为了美观

# 以上为find_all方法，配合字符串、正则表达式、自己定义的函数进行搜索



# (2)  kwargs  参数
t_list = bs.find_all(id='head')  # find_all里面给的不是规则，而是参数

t_list1 = bs.find_all(class_=True)



#(3) text 参数
t_list = bs.find_all(text = 'hao123')
t_list1 = bs.find_all(text = ['hao123','地图','贴吧'])
for item in t_list1:
    print(item)
t_list3 = bs.find_all(text = re.compile('\d')) 
 # 应用正则表达式来查找包含特定文本的内容（标签里的字符串）  \d 表示有数字内容
print(t_list,t_list1,t_list3)


# (4) limit   参数
t_list = bs.find_all('a',limit=3)   # 限制数量
```
```python
# css 选择器
t_list = bs.select('title')   # 通过标签来查找
t_list = bs.select('.mnav')    # .表示通过类名来查找
t_list = bs.select('#u1')         # 通过id来查找
t_list = bs.select("a[class='bri']")   # 通过属性来查找
t_list = bs.select('head > title')    # 通过子标签来查找
t_list = bs.select('.mnav ~ .bri')    # 通过兄弟标签来查找
print(t_list[0].get_text())  # 拿到bri这个兄弟标签里面的文本，因为只有一个元素所以是0
for item in t_list:
    print(item)
```
### 补充正则表达式(实际上是一种规范)
#### 基本内容
```python
# 正则表达式补充
.             #表示任何单个字符
[]            #字符集，对单个字符给出取值范围 [abc]表示a、b、c，[a-z]表示a-
[^]           #非字符集，对单个字符给出排除范围  [^abc]表示非a、b、c的单个字符
*             #前一个字符的0次或无限次扩展  abc*表示ab、abc、abcc、abccc等
+             #前一个字符的1次或无限次扩展  abc+表示ab、abc、abcc、abccc等
?             #前一个字符的0次或1次扩展     abc?表示ab、abc
|             #左右表达式任意一个           abc|def 表示abc、def
{m}           #扩展前一个字符m次            ab{2}c表示abbc
{m,n}         #扩展前一个字符m至n次(含n)    ab{1,2}c表示abc、abbc
^             #匹配字符串开头               ^abc表示abc且在一个字符串的开头
$             #匹配字符串的结尾             abc$表示abc且在一个字符串的结尾
()            #分组标记，内部只能使用|操作符 (abc)表示abc，(abc|def)表示abc、def
\d            #数字，等价于[0-9]
\w            #单词字符，等价于[A-Za-z0-9_]
```
```python
# re 库主要功能
re.search()          #在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
re.match()           #从一个字符串的开始位置起匹配正则表达式，返回match对象
re.findall()         #搜索字符串，以列表类型返回全部能匹配的子串
re.split()           #将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
re.finditer()        #搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
re.sub()             #在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串
```
```python
# 一些修饰符，可以控制匹配的模式
re.l             #使匹配对大小写不敏感
re.L             #使本地化识别(locale-aware)匹配
re.M             #多行匹配，影响^和$
re.S             #使. 匹配包括换行在内的所有字符
re.U             #根据Unicode字符集解析字符。这个标志影响\w,\W,\b,\B
re.X             #该标志通过给予你更灵活的格式以便你将正则表达式写的易于理解
```
### 关于xwlt
保存数据到excel
```python
import xlwt
workbook = xlwt.Workbook(encoding='utf-8')        # 创建worbook对象
worksheet = workbook.add_sheet('sheet1')          # 创建工作表
worksheet.write(0,0,'hello')                 
# 写入数据，第一个参数“行”，第二个参数“列”，第三个参数内容
workbook.save('student.xls')
```

```python
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('sheet1') 
for i in range(0,9):                          # excel中第一行第一列表示成矩阵是（0，0）
    for j in range(0,i+1):
        worksheet.write(i,j,'%s * %s =%s'%(i+1,j+1,(i+1)*(j+1)))
workbook.save('student.xls')
```

### 关于sqlite 数据库
我们可以把数据存到excel，也可以存到数据库，sqlite就是一个能存数据的数据库
```python
import sqlite3
# 1.连接数据库
cnn = sqlite3.connect('text.db')             # 打开或创建数据库文件
print('Opened database successfully')
```
```python
# 2.创建数据表
conn = sqlite3.connect('text.db')             # 打开或创建数据库文件
print('成功打开数据库')

c = conn.cursor()       # 获取游标

sql = '''
    create table company
        (id int primary key not null,
        name text not null,
        age int not null,
        address char(50),
        salary real);

'''

c.execute(sql)          # 执行sql语句
conn.commit()           #  提交数据库操作
conn.close()            # 关闭数据库连接

print('成功建表')
```
```python
# 3. 插入数据
conn = sqlite3.connect('text.db')             # 打开或创建数据库文件
print('成功打开数据库')

c = conn.cursor()       # 获取游标

sql1 = '''
    insert into company (id,name,age,address,salary)
    values (1,'swq',20,'jh',10000)

'''
sql2 = '''
    insert into company (id,name,age,address,salary)
    values (2,'cyk',20,'jh',15000)

'''
c.execute(sql1)          # 执行sql语句
c.execute(sql2) 
conn.commit()           #  提交数据库操作
conn.close()            # 关闭数据库连接

print('插入数据完毕')
```
```python
# 4. 查询数据
conn = sqlite3.connect('text.db')             # 打开或创建数据库文件
print('成功打开数据库')

c = conn.cursor()       # 获取游标

sql = 'select id,name,address,salary from company'

cursor = c.execute(sql)          # 执行sql语句

for row in cursor:
    print('id = ',row[0])
    print('name = ',row[1])
    print('address = ',row[2])
    print('salary = ',row[3])

conn.commit()           #  提交数据库操作
conn.close()            # 关闭数据库连接

print('查询完毕')
```

### 关于wordcloud  词云
一些参数
```python
import jieba   # 把句子分成几个词
import matplotlib.pyplot as plt   # 绘图
from wordcloud import WordCloud   # 词云
from PIL import Image             # 图片处理
import numpy as np
import sqlite3                    # 数据库
# 这些模块可以在你爬取了某个网站的数据之后想做数据可视化操作所用的模块


font_path : string  #字体路径，需要展现什么字体就把该字体路径+后缀名写上，如：font_path = '黑体.ttf'
# 注意字体可能需要从windows里放到vscode才能找到
 
width : int (default=400) #输出的画布宽度，默认为400像素
 
height : int (default=200) #输出的画布高度，默认为200像素
 
prefer_horizontal : float (default=0.90) #词语水平方向排版出现的频率，默认 0.9 （所以词语垂直方向排版出现频率为 0.1 ）
 
mask : nd-array or None (default=None) #如果参数为空，则使用二维遮罩绘制词云。如果 mask 非空，设置的宽高值将被忽略，遮罩形状被 mask 取代。除全白（#FFFFFF）的部分将不会绘制，其余部分会用于绘制词云。如：bg_pic = imread('读取一张图片.png')，背景图片的画布一定要设置为白色（#FFFFFF），然后显示的形状为不是白色的其他颜色。可以用ps工具将自己要显示的形状复制到一个纯白色的画布上再保存，就ok了。
 
scale : float (default=1) #按照比例进行放大画布，如设置为1.5，则长和宽都是原来画布的1.5倍
 
min_font_size : int (default=4) #显示的最小的字体大小
 
font_step : int (default=1) #字体步长，如果步长大于1，会加快运算但是可能导致结果出现较大的误差
 
max_words : number (default=200) #要显示的词的最大个数
 
stopwords : set of strings or None #设置需要屏蔽的词，如果为空，则使用内置的STOPWORDS
 
background_color : color value (default=”black”) #背景颜色，如background_color='white',背景颜色为白色
 
max_font_size : int or None (default=None) #显示的最大的字体大小
 
mode : string (default=”RGB”) #当参数为“RGBA”并且background_color不为空时，背景为透明
 
relative_scaling : float (default=.5) #词频和字体大小的关联性
 
color_func : callable, default=None #生成新颜色的函数，如果为空，则使用 self.color_func
 
regexp : string or None (optional) #使用正则表达式分隔输入的文本
 
collocations : bool, default=True #是否包括两个词的搭配
 
colormap : string or matplotlib colormap, default=”viridis” #给每个单词随机分配颜色，若指定color_func，则忽略该方法
 
random_state : int or None  #为每个单词返回一个PIL颜色
fit_words(frequencies)  #根据词频生成词云

generate(text)  #根据文本生成词云

generate_from_frequencies(frequencies[, ...])   #根据词频生成词云

generate_from_text(text)    #根据文本生成词云

process_text(text)  #将长文本分词并去除屏蔽词（此处指英语，中文分词还是需要自己用别的库先行实现，使用上面的 fit_words(frequencies) ）

recolor([random_state, color_func, colormap])   #对现有输出重新着色。重新上色会比重新生成整个词云快很多

to_array()  #转化为 numpy array

to_file(filename)   #输出到文件
```
