import mysql.connector as mysql

connect = mysql.connect(host='localhost',user='root',passwd='')

cursor = connect.cursor()

cursoe.execute('show databases')

for i in cursor:
    
    print(i)
