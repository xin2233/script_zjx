#对比一个文件里的2列数据，将数据不同的地方在第三列的相同位置标记出来。

import xlrd
import xlwt
import openpyxl

#打开工作簿
wb = openpyxl.load_workbook(r'.\Test3.xlsx')
#选取sheet
sh = wb['Sheet1']
#定义两个用于存放数据的list
list1 = []
list2 = []
#将excel的两列存入list中
for data in list(sh.rows)[0:]: #如果需要去掉第一行的表头就从1开始
    print(data[1].value)
    list1.append(data[0].value) #将第一列数据存入list1
    list2.append(data[1].value) #将第一列数据存入list2
    
for i in range(len(list1)):
    if list1[i] != list2[i]:
        #将相同数据写入第三列，写在和第一列数据相同的位置
        sh.cell(row=i+1, column=4, value='xx')
        print('diff write')
#保存数据，关闭excel
wb.save(r'.\Test3.xlsx')
print('done!!!!!')