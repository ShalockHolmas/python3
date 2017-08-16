import pymysql

db = pymysql.connect('localhost', 'root', 'root', 'test')
cursor = db.cursor()
cursor.execute('select version()')

data = cursor.fetchone()

print(data)

db.close()