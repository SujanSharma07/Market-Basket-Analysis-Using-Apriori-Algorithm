import csv
import mysql.connector
from single import support,total

print("\nProcessing For Triplet")
csvfile= open('test.csv')
readCSV = csv.reader(csvfile, delimiter=',')

mydb = mysql.connector.connect(host='127.0.0.1', user='root',passwd='9680', database='market')
mycursor = mydb.cursor()

mydb1 = mysql.connector.connect(host='127.0.0.1', user='root',passwd='9680', database='market')

mydb2 = mysql.connector.connect(host='127.0.0.1', user='root',passwd='9680', database='market')
mycursor2 = mydb2.cursor()

mycursor.execute('truncate triplet')
mycursor.execute('truncate setcount3')
for i in readCSV:
    for p in range(len(i)-2):
        mm=p+1
        for m in range(mm,len(i)-1):
            nn=m+1
            for n in range(nn,len(i)):
                try:
                    if(i[p]!=i[m]!=i[n] and i[n]!=''and i[p]!='' and i[m]!=''):
                        a=[]
                        a.append(i[p])
                        a.append(i[m])
                        a.append(i[n])
                        aa=sorted(a)
                        j=aa[0]
                        k=aa[1]
                        l=aa[2]

                        mycursor.execute("insert into triplet value('{}','{}','{}')".format(j, k, l))
                        mydb.commit()
                except:
                    break

mycursor.execute('select distinct product_1,product_2,product_3 from triplet')

for l in mycursor:
    count=0
    mycursor1 = mydb1.cursor()
    mycursor1.execute('select * from triplet')
    for m in mycursor1:
        if ((l[0]==m[0] or l[1]==m[0] or l[2]==m[0]) and (l[0]==m[1] or l[1]==m[1] or l[2]==m[1]) and (l[0]==m[2] or l[1]==m[2] or l[2]==m[2])):
            count+=1
    if (count >= ((support * total) / 100)):
        mycursor2.execute("insert into setcount3 value('{}','{}','{}',{})".format(l[0],l[1],l[2],count))
        mydb2.commit()
print("Processing Completed For Triplet\n")