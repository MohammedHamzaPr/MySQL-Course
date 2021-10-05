import mysql.connector as mysql
connect = mysql.connect(host='localhost',user='root',passwd='toor',database='youtube')

cursor = connect.cursor()
cursor.execute("drop table data")


print('Done')
input("Press Enter For Exit[+]")