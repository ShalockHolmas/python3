import sys
import xlrd
#检查disassembly设定
#disassembly 第三行开始捞取数据
excel = xlrd.open_workbook("../../eLM+disassembly+Rule+wk30+Shan.xlsx")
table = excel.sheets()[0]
rownum = table.nrows
print('row:', rownum)
list = {}
for i in range(rownum):
    if i <= 1:
        continue
    sql = "select * from wm_disassembly_rules where PN90_LIKE = '" + table.row_values(i)[0] +"' and rule = '" + str(int(table.row_values(i)[2])) +"' and in_part_no = '" + table.row_values(i)[3] +"' and rule_seq= '" + str(int(table.row_values(i)[4])) +"' and in_qty = '" + str(int(table.row_values(i)[5])) +"' and active = '" + table.row_values(i)[6] +"' and prod_code = '" + table.row_values(i)[7] +"';"
    print(sql)
