import mysql.connector as mysql
connect = mysql.connect(host='localhost',user='root',passwd='')
cursor = connect.cursor()
cursoe.execute('create database youtube')
print('Done Create')
print('press Enter for exit')
