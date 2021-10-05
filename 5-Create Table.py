import mysql.connector as mysql
connect = mysql.connect(host='localhost',user='root',passwd='toor',database='youtube')
cursor = connect.cursor()
cursor.execute('create table data(id varchar(100),name varchar(30),pn varchar(20),emil varchar(30),address varchar(100))')
print('Done Create')
print('Press Enter For Exit[+]')
