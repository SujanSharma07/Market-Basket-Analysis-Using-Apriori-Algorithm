import csv
import mysql.connector
import time

csvfile= open('test.csv')
readCSV = csv.reader(csvfile, delimiter=',')

mydb = mysql.connector.connect(host='127.0.0.1', user='root',passwd='9680', database='market')
mycursor = mydb.cursor()


c=0
mycursor.execute("DROP TABLE IF EXISTS `groceries`")
mycursor.execute('create table groceries(product_1 varchar(45))')
for i in readCSV:

    a=len(i)
    b=c
    if(b>a):
        c=b
    else:
        c=a


for p in range(2,c):
    mycursor.execute('ALTER TABLE groceries ADD COLUMN product_{} VARCHAR(45);'.format(p))


for i in readCSV:
    for p in range(len(i)):

        mycursor.execute("insert into groceries(product_{}) value('{}')".format(p,i[p]))
        mydb.commit()
