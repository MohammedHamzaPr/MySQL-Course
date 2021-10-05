import mysql.connector as mysql
connect = mysql.connect(host='localhost',user='root',passwd='toor',database='youtube')
cursor = connect.cursor()



cursor.execute("delete from data where id = '3'")

connect.commit()

print('Done')
input('press Enter for exit')
