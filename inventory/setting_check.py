import cx_Oracle
from inventory import database
import sys
import xlrd

con = database.returnConn('act')
cursor = con.cursor()
sql = 'select * from wm_tran_order where rownum <= 1'
cursor.execute(sql)
result = cursor.fetchall()
print(result)
# cursor.


excel = xlrd.open_workbook("../../CSCR5-4384_鼎新電腦-new-Rochelle.xlsx")
table = excel.sheets()[0]
rownum = table.nrows
print('row:', rownum)
list = {}
for i in range(rownum):
    if i <= 1:
        continue
    sql = ''
    print(sql)
