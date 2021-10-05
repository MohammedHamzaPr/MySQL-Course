import mysql.connector as mysql
connect = mysql.connect(host='localhost',
	user='root',
	passwd='toor',
	database='youtube')

cursor = connect.cursor()
cursor.execute("select * from data")
#connect.commit()

for i in cursor:
	print(i)


print('Done')
input("Press Enter For Exit[+]")