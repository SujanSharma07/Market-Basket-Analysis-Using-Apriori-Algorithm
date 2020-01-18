import csv
import mysql.connector
from single import support,total


print("\nProcessing For pair")
csvfile= open('test.csv')
readCSV = csv.reader(csvfile, delimiter=',')

mydb = mysql.connector.connect(host='127.0.0.1', user='root',passwd='9680', database='market')
mycursor = mydb.cursor()

mydb1 = mysql.connector.connect(host='127.0.0.1', user='root',passwd='9680', database='market')

mydb2 = mysql.connector.connect(host='127.0.0.1', user='root',passwd='9680', database='market')
mycursor2 = mydb2.cursor()

mycursor.execute('truncate dublet')
mycursor.execute('truncate secondset2')
for i in readCSV:

    for p in range(len(i)-1):
        mm=p+1
        for m in range(mm,len(i)):


            if(i[p]!=i[m] and i[p]!='' and i[m]!=''):
                a=[]
                a.append(i[p])
                a.append(i[m])
                aa=sorted(a)
                j=aa[0]
                k=aa[1]


                mycursor.execute("insert into dublet value('{}','{}')".format(j, k))
                mydb.commit()



mycursor.execute('select distinct product_1,product_2 from dublet')

for l in mycursor:
    count=0
    mycursor1 = mydb1.cursor()
    mycursor1.execute('select * from dublet')
    for m in mycursor1:
        if ((l[0]==m[0] or l[1]==m[0] ) and (l[0]==m[1] or l[1]==m[1])):
            count+=1
    if (count >= ((support * total) / 100)):
        mycursor2.execute("insert into secondset2 value('{}','{}',{})".format(l[0],l[1],count))
        mydb2.commit()
print("Processing Completed For Pair\n")
