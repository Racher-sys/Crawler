from getData import getData
from saveData import saveData


def main():
    baseurl = "http://people.csail.mit.edu/brussell/research/LabelMe/Images/05june05_static_street_boston/"
    datalist = getData(baseurl)  #爬取网页
    print(datalist)
    savepath = ".\\picture.xls"
    saveData(datalist,savepath)  #保存数据

if __name__ == "__main__":
    main()  #调用函数
