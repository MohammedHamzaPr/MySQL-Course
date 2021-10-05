import mysql.connector as mysql
connect = mysql.connect(host='localhost',user='root',passwd='toor')

cursor = connect.cursor()
cursor.execute("show tables from youtube")

for tables in cursor:
	print(tables)

print('Done')
input("Press Enter For Exit[+]")