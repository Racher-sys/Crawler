import xlwt #进行excel操作

#保存数据
def saveData(datalist,savepath):
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet('图片保存',cell_overwrite_ok=True)  # 创建工作表
    col = ("图片链接")
    for i in range(0,1):
        sheet.write(0,i,col[i])
    for i in range(0, len(datalist)):
        print("第%d条"%(i+1))
        data = datalist[i]
        for j in range(0,1):
            sheet.write(i+1,j,data[j])
    book.save(savepath)