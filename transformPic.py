import urllib.request
import xlrd

def main():
    transform()

def getPicUrlFromExcel():
    worksheet = xlrd.open_workbook(u'picture.xls')
    sheet_names = worksheet.sheet_names()
    for sheet_name in sheet_names:
        sheet = worksheet.sheet_by_name(sheet_name)
        row = []
        for i in range(1,sheet.nrows):
            row.append(sheet.row_values(i))
    return row

def transform():
    rows = getPicUrlFromExcel()
    print(rows)
    num = 99
    for i in range(102,len(rows)):
        num = num + 1
        print(i)
        url = str(rows[i][0])
        print(url)
        if url == '':
            break
        path = str('E:\desired\crawler\picture\{id}.jpg'.format(id=num))
        urllib.request.urlretrieve(url,path)
        print('第{index}张图片下载ok'.format(index=num))

if __name__ == "__main__":
    main()