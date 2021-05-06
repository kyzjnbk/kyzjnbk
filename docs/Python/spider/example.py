# coding=utf-8
# %%
from bs4 import BeautifulSoup   #网页解析，获取数据
import re    #正则表达式，进行文字匹配
import urllib.request,urllib.error     #指定URL，获取网页数据
import xlwt     #进行excel操作
import sqlite3   #进行SQLite数据库操作
# %%

def main():
    baseurl='https://movie.douban.com/top250?start='
    #1.爬取网页
    datalist = getData(baseurl)
    #savepath = '豆瓣电影TOP250.xls' #保存在一个excel文件里，也可以用'./' 表示保存在当前文件 
    dbpath = 'moive.db'
    #3.保存数据
    #saveData(savepath,datalist)
    saveData2DB(datalist,dbpath)
    # askURL('https://movie.douban.com/top250?start=')

# 影片详情链接的规则
findlink = re.compile(r'<a href="(.*?)">')  #创建正则表达式对象，表示规则（字符串的模式）
# 影片图片
findimgsrc = re.compile(r'<img.*src="(.*?)"',re.S) #re.S让换行符包含在字符中
# 最后查找到的内容是双引号里面的，前面.*不是我们要找的内容所以不加括号
# 影片片名
findtitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findrating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 找到评价人数
findjudge = re.compile(r'<span>(\d*)人评价</span>')
# 找到概况
findinq = re.compile(r'<span class="inq">(.*)</span>')
# 找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)



# 爬取网页
def getData(baseurl):
    datalist=[]
    for i in range(0,10):    # 调用获取信息的函数，10次，每页是25条
        url = baseurl + str(i*25)
        html = askURL(url)   # 执行一次循环就获取一页，保存获取到的网页源码
        #2.逐一解析数据，是在for循环里的，因为每一页都要解析
        soup = BeautifulSoup(html,'html.parser') # 解析成soup这么一个树形对象
        for item in soup.find_all('div',class_='item'):
            #或者用select("div[class='item']") #soup.find_all就是查找符合要求的字符串，形成列表
            # print(item)   #测试：查看电影item全部信息
            data = []     # 保存一部电影的所有信息
            item = str(item)
            # 获取影片详情的超链接
            link = re.findall(findlink,item)[0]   # re库用来通过正则表达式查找指定字符串            
            data.append(link)                     # 添加链接
            # print(link)
            
            imgsrc = re.findall(findimgsrc,item)[0]
            data.append(imgsrc)                   # 添加图片
            
            titles = re.findall(findtitle,item)   # 片名可能还有外文名
            if(len(titles)==2):
                ctitle = titles[0] 
                data.append(ctitle)                 # 添加中文名
                otitle = titles[1].replace('/','')  #去掉无关的符号
                data.append(otitle)                 # 添加外国名
            else:
                data.append(titles[0])
                data.append(' ')    # 外国名字留空，就算没有元素也要留位置，因为最后要做成表格

          
            rating = re.findall(findrating,item)[0]
            data.append(rating)             # 添加评分

            judgenum = re.findall(findjudge,item)[0]
            data.append(judgenum)              # 添加评价人数

            inq = re.findall(findinq,item)
            if len(inq) != 0:
                inq = inq[0].replace('。','')    # 去掉句号
                data.append(inq)                   # 添加概述
            else:
                data.append(' ')                  # 留空
            
            bd = re.findall(findBd,item)[0]
            bd = re.sub(r'<br(\s+)?/>(\s+)?',' ',bd)   # 去掉<br/>，\s表示空格
            bd = re.sub('/',' ',bd)                  # 替换/
            data.append(bd.strip())                 # 去掉前后的空格

            datalist.append(data)               # 把处理好的一部电影信息放入datalist
    # print(datalist)
    return datalist  
    
    



# 得到指定一个URL的网页内容
def askURL(url):
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0'
# 模拟浏览器头部信息，向豆瓣服务器发送消息
# 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器
# 本质上是告诉浏览器，我们可以接收什么水平的文件内容
    }
    request = urllib.request.Request(url,headers=head)
    html = ''
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        # print(html)
    except urllib.error.HTTPError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)

    return html



# 保存数据
def saveData(savepath,datalist):
    print('save...')
    book = xlwt.Workbook(encoding='utf-8',style_compression=0)   #创建book对象
    sheet = book.add_sheet('豆瓣电影TOP250',cell_overwrite_ok=True)  # 创建工作表
    col = ('电影详情链接','图片链接','影片中文名','影片外国名','评分','评价数','概况','相关信息')
    for i in range(0,8):
        sheet.write(0,i,col[i])           # 列名
    for i in range(0,250):
        print('第%s条'%(i+1))
        data = datalist[i]       # datalist中有250部电影的信息，每个电影信息又是一个list，其中就有8个要素
        for j in range(0,8):
            sheet.write(i+1,j,data[j])  # 第一行是列名，所以从下一行开始，内容就是每部电影list的内容
    book.save(savepath)      # 保存
    


def saveData2DB(datalist,dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"'+ data[index]+'"'
        sql = '''
                insert into movie250 (
                info_link,pic_link,cname,ename,score,rate,instroduction,info) 
                values(%s)'''%",".join(data)
        # sql语句应该和第二个for循环同级，每拼好一次data，就执行一次sql语句
        # 因为data是一行数据，而sql的values赋值是需要逗号的
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()        
            
    print('..')


# conn = sqlite3.connect('moive.db')             # 打开或创建数据库文件
# print('成功打开数据库')

# c = conn.cursor()       # 获取游标

# sql = 'select info_link,pic_link,cname,ename from movie250'

# cursor = c.execute(sql)          # 执行sql语句

# for row in cursor:
#     print('info_link = ',row[0])
#     print('pic_link = ',row[1])
#     print('cname = ',row[2])
#     print('ename = ',row[3])

# conn.commit()           #  提交数据库操作
# conn.close()            # 关闭数据库连接



# print('查询完毕')











def init_db(dbpath):
    sql = '''
        create table movie250
        (id integer primary key autoincrement,   
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric,
        rate numeric,
        instroduction text,
        info text
        )
    
    '''     # 创建数据表  autoincrement 是自动编号的意思
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()







if __name__ == '__main__':   #当程序执行时，调用函数
    main()
    #init_db('movie250.db')
    print('爬取完毕')
# %%
a=('s' 'w' 'q')

for index in a:
    print('%s'%",".join(a))
# %%
