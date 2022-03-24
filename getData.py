import re
from askURL import askURL
from bs4 import BeautifulSoup


#图片链接的正则
findLink = re.compile(r'<a.*href="(.*?)">')  #创建正则表达式对象，表示规则（字符串的模式）.表示一个字符，*表示0个或多个字符，？表示链接中间这个网址会出现一次或0次，意思是最小匹配，尽可能的少重复

#爬取网页+解析数据
def getData(baseurl):
    datalist = []
    html = askURL(baseurl)  #保存获取到的网页源码
    # 逐一解析数据
    soup = BeautifulSoup(html,"html.parser")
    for item in soup.find_all('tr'): #查找符合要求的字符，形成列表
        data = []  #保存一部电影的所有信息
        item = str(item)

        pre_link = str(baseurl)
        link = re.findall(findLink,item) #re库用来通过正则表达式查找指定的字符串
        if len(link)>0:
            link = pre_link + link[0]
        else:
            link = ''
        data.append(link)
        datalist.append(data)
    # print(datalist)
    return datalist