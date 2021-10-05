import mysql.connector as mysql
connect = mysql.connect(host='localhost',user='root',passwd='toor',database='youtube')

Id = input("Enter your ID: ")
name = input("Enter your name: ")
pn = input("Enter a number: ")
em = input("Enter your emil: ")
add = input("Enter your address: ")
command = "insert into data(id,name,pn,emil,address)values(%s,%s,%s,%s,%s)"
data = (Id,name,pn,em,add)

cursor = connect.cursor()

cursor.execute(command,data)
connect.commit()

print("Done insert")
input("Press Enter for Exit[+]")
