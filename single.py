import csv
import mysql.connector
def confidencevalue():
    Confidence_value = int(input("Enter Confidence Value \t \n"))
    mydb110 = mysql.connector.connect(host='127.0.0.1', user='root', passwd='9680', database='market')
    mycursor110 = mydb110.cursor()
    mycursor110.execute('truncate confidence')
    mycursor110.execute('insert into confidence value({})'.format(Confidence_value))
    mydb110.commit()


csvfile= open('test.csv')
readCSV = csv.reader(csvfile, delimiter=',')
mydb = mysql.connector.connect(host='127.0.0.1', user='root',passwd='9680')
print("Erasing Previous DATABASE and CREATING NEW DATABASE")
mycursor=mydb.cursor()
mycursor.execute("DROP SCHEMA IF EXISTS market;create database market;use market;create table allproducts(product varchar(45))")

mydb = mysql.connector.connect(host='127.0.0.1', user='root',passwd='9680',database='market')
mycursor=mydb.cursor()
mycursor.execute("create table confidence(confidence int(11));create table dublet(product_1 varchar(45),product_2 varchar(45));create table products(product varchar(45),count int(11))")
mydb = mysql.connector.connect(host='127.0.0.1', user='root',passwd='9680',database='market')
mycursor=mydb.cursor()
mycursor.execute("create table quardruple(product_1 varchar(45),product_2 varchar(45),product_3 varchar(45),product_4 varchar(45));create table secondset2(product_1 varchar(45),product_2 varchar(45),count int(11));")
mydb = mysql.connector.connect(host='127.0.0.1', user='root',passwd='9680',database='market')
mycursor=mydb.cursor()
mycursor.execute("create table setcount3(product_A varchar(45),product_B varchar(45),product_C varchar(45),counts int(11));")
mydb = mysql.connector.connect(host='127.0.0.1', user='root',passwd='9680',database='market')
mycursor=mydb.cursor()
mycursor.execute("create table setcount4(product_a varchar(45),product_b varchar(45),product_c varchar(45),product_d varchar(45),counts int(11));")
mydb = mysql.connector.connect(host='127.0.0.1', user='root',passwd='9680',database='market')
mycursor=mydb.cursor()
mycursor.execute("create table triplet(product_1 varchar(45),product_2 varchar(45),product_3 varchar(45));")
print("\nNEW DATABASE CREATED\n")

mydb = mysql.connector.connect(host='127.0.0.1', user='root',passwd='9680', database='market')
mydb1 = mysql.connector.connect(host='127.0.0.1', user='root',passwd='9680', database='market')
mycursor = mydb.cursor()
mycursor1 = mydb1.cursor()
mycursor.execute('truncate allproducts')
mycursor.execute('truncate products')
print("VALUES MUST BE FROM 0 TO 100 ONLY\n")
support=int(input("Enter Support Value\t \n"))
confidencevalue()
print("\nprocessing for single item")


for row in readCSV:
 for a in row:
     if(a!=''):
         mycursor.execute("insert into allproducts(product) value('{}')".format(a))

mycursor.execute("select distinct(product) from allproducts")

for m in mycursor:
    count=0
    total=0
    csvfile = open('test.csv')
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        for i in range(len(row)):
            if(m[0]==row[i]):
                count+=1
        total+=1
    if(count>=((support*total)/100)):
        mycursor1.execute("insert into products(product,count) value('{}',{})".format(m[0],count))
        mydb1.commit()
print("Processing For Single Item Completed \n")