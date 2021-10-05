import mysql.connector as mysql
connect = mysql.connect(host='localhost',user='root',passwd='toor')

cursor = connect.cursor()
cursor.execute("drop database youtube")


print('Done')
input("Press Enter For Exit[+]")