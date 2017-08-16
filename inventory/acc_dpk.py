import sys
import xlrd

#dpk匝出
#第二行开始

excel = xlrd.open_workbook("../../acc.xlsx")
table = excel.sheets()[0]
rownum = table.nrows
print('row:', rownum)
list = {}
for i in range(rownum):
    if i == 0:
        continue
    if table.row_values(i)[4] not in list.keys():
        list[table.row_values(i)[4]] = table.row_values(i)[5]
    else:
        list[table.row_values(i)[4]] = list[table.row_values(i)[4]] + table.row_values(i)[5]

excel = xlrd.open_workbook("../act.xlsx")
table = excel.sheets()[0]
rownum = table.nrows

for i in range(rownum):
    if i == 0:
        continue
    if table.row_values(i)[4] not in list.keys():
        list[table.row_values(i)[4]] = table.row_values(i)[5]
    else:
        list[table.row_values(i)[4]] = list[table.row_values(i)[4]] + table.row_values(i)[5]

total = 0

for key in list:
    total += list[key]
    print(key + ":", list[key])

print("共：", total)