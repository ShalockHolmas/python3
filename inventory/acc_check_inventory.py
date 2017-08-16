from inventory import database
import cx_Oracle

from inventory import database

#acc单据merge单过账信息错误脚本
#root cause：原单中merge name与detail中merge name不对应，造成未产merge单 或者 merge单过账储位错误
#修改part no后执行


handle = cx_Oracle.connect(database.username, database.password, database.link)

sql = "SELECT b.ori_profile_id,b.dest_profile_id,b.int_ref_no,b.tran_no,b.ori_merge_name,b.dest_merge_name,b.ext_ref_no3,a.fm_warehouse,a.fm_location,a.fm_lot,a.to_warehouse,a.to_location,a.to_lot FROM WM_TRAN_ORDER_DETAIL a LEFT JOIN wm_tran_order b on a.tran_no = b.tran_no WHERE (a.PART_NO = '60NB01E0-MB3010' OR a.ALT_PART_NO = '60NB01E0-MB3010') and (not (a.fm_warehouse in('G52','C50','A51') and a.to_warehouse IN ('G52','C50','A51'))) and b.status='007'"
# handle.close(sql)
cursor = handle.cursor()
cursor.execute(sql)
result = cursor.fetchall()

# print(result[0])
for row in result:
    # sql = "select merge_name from wm_territory where profile_id = '"+ row[0] + "' and warehouse= '" + row[4] + "' and location = '" + row[5] + "' "
    sql = "select a.merge_name from wm_territory a LEFT JOIN wm_tran_order_detail b ON a.warehouse=b.fm_warehouse and nvl(a.location,'1') = nvl(b.fm_location,'1') and nvl(a.lot,'1') = NVL(b.fm_lot,'1') WHERE b.tran_no = '" + \
          row[3] + "'"
    cursor.execute(sql)
    mergeNameList = cursor.fetchall()
    for mergeNames in mergeNameList:
        for mergeName in mergeNames:
            if mergeName != row[4]:
                print(row[2])
                print(mergeName)
                print(row[4])
                # sys.exit(0)

cursor.close()
handle.close()
