import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="AmbikaRajendran",database="productsdata")
mycursor = mydb.cursor()
mycursor.execute("select name,count(name) from products group by name")
for i in mycursor:
	print(i)