import xlrd
#导入xlrd模块
data = xlrd.open_workbook(r'D:\xx.xls') 
#打开excel文件
data.sheet_names()
print('sheet:'+str(data.sheet_names()))      
#查看py_tst.xlsx文件中的工作表
table1 = data.sheet_by_index(0)
table2 = data.sheet_by_index(1)
# 打印data.sheet_names()可发现，返回的值为一个列表，通过对列表索引操作获得工作表1,工作表2
col1 = table1.col_values(0)
col2  = table2.col_values(0)
diff = []
for i in col1:
    if i not in col2:
        diff.append(i)
print(diff)

data = open(r"D:\diff.xlsx",'w',encoding='utf-8')
data.write("different\n")
for m in range(len(diff)):
    data.write(str(diff[m]))
    data.write('\n')
data.close()
