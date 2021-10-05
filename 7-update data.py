import mysql.connector as mysql
connect = mysql.connect(host='localhost',user='root',passwd='toor',database='youtube')

cursor = connect.cursor()


cursor.execute("update data set pn='07707011856' where name='mohamed'")
connect.commit()

print("Done insert")
input("Press Enter for Exit[+]")
