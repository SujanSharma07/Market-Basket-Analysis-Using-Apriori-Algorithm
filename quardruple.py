import csv
import mysql.connector
from single import *
from doublet import *
from triplet import *

csvfile= open('test.csv')
readCSV = csv.reader(csvfile, delimiter=',')
print("\nProcessing For Quadreuple")

mydb = mysql.connector.connect(host='127.0.0.1', user='root',passwd='9680', database='market')
mycursor = mydb.cursor()

mydb1 = mysql.connector.connect(host='127.0.0.1', user='root',passwd='9680', database='market')

mydb2 = mysql.connector.connect(host='127.0.0.1', user='root',passwd='9680', database='market')
mycursor2 = mydb2.cursor()

mycursor.execute('truncate quardruple')
mycursor.execute('truncate setcount4')
for i in readCSV:
    for p in range(len(i)-3):
        mm=p+1
        for m in range(mm,len(i)-2):
            nn=m+1
            for n in range(nn,len(i)-1):
                oo=n+1
                for o in range(oo,len(i)):
                    try:
                        if(i[p]!=i[m]!=i[n]!=i[o] and i[n]!=''and i[p]!='' and i[m]!='' and i[o]!=''):
                            a=[]
                            a.append(i[p])
                            a.append(i[m])
                            a.append(i[n])
                            a.append(i[o])
                            aa=sorted(a)
                            j=aa[0]
                            k=aa[1]
                            l=aa[2]
                            z=aa[3]
                            mycursor.execute("insert into quardruple value('{}','{}','{}','{}')".format(j, k, l,z))
                            mydb.commit()
                    except:
                        break
mycursor.execute('select distinct product_1,product_2,product_3,product_4 from quardruple')

for l in mycursor:
    count=0
    mycursor1 = mydb1.cursor()
    mycursor1.execute('select * from quardruple')
    for m in mycursor1:
        if ((l[0]==m[0] or l[1]==m[0] or l[2]==m[0] or l[3]==m[0]) and (l[0]==m[1] or l[1]==m[1] or l[2]==m[1] or l[3]==m[1])):
            if((l[0]==m[2] or l[1]==m[2] or l[2]==m[2] or l[3]==m[2])and(l[0]==m[3] or l[1]==m[3] or l[2]==m[3] or l[3]==m[3])):
                count+=1
    if(count>=((support*total)/100)):
        mycursor2.execute("insert into setcount4 value('{}','{}','{}','{}',{})".format(l[0],l[1],l[2],l[3],count))
        mydb2.commit()
print("Processing is Completed \n")
print("Now You Can Proceed To U.I.  \n")
