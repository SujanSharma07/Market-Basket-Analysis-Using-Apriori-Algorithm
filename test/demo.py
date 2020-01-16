from tkinter import *
from functools import partial
import matplotlib.pyplot as plt
import csv
import mysql.connector


def convertTuple(tup):
    str = ''.join(tup)
    return str


###############################################################################################################
def conf_graph2():
    activities = []
    slices = []
    left = []

    # heights of bars
    height = []

    # labels for bars
    tick_label = []
    mydb = mysql.connector.connect(host='127.0.0.1', user='root', passwd='9680', database='market')
    mycursor = mydb.cursor()
    mycursor.execute('select * from confidence')
    for key in mycursor:
        confidence_value = key[0]
        break
    mycursor.execute("SELECT count FROM products WHERE  product LIKE '%{}%'".format(entry.get()))
    for i in mycursor:
        a = i[0]

        break


    mycursor.execute("select product_2,count from secondset2 where product_1='{}' union select product_1,count from secondset2 where product_2='{}' order by count desc limit 7".format(entry.get(),entry.get()))
    j=1
    for i in mycursor:



        b=round((i[1]/a)*100)
        if(b>=confidence_value):
            if(j<=8):
                slices.append(b)
                tick_label.append(entry.get()+'-->'+convertTuple(i[0]))
                left.append(j)
                height.append(int(b))
                j += 1

                activities.append(convertTuple(i[0]))



    plt.bar(left, height, tick_label=tick_label, width=0.8, color=['red', 'green','grey'])

    # naming the x-axis
    plt.xlabel('ITEMS')
    # naming the y-axis
    plt.ylabel('CONFIDENCE IN %')
    # plot title
    plt.title('CONFIDENCE OF PRODUCT  '+entry.get())

    # function to show the plot
    plt.show()

def conf_graph3():
    left = []
    activities=[]

    # heights of bars
    height = []
    slices=[]
    # labels for bars
    tick_label = []
    mydb= mysql.connector.connect(host='127.0.0.1', user='root', passwd='9680', database='market')
    mycursor = mydb.cursor()
    mycursor.execute('select * from confidence')
    for key in mycursor:
        confidence_value = key[0]
        break
    mycursor.execute("SELECT count FROM products WHERE  product LIKE '%{}%'".format(entry.get()))
    for i in mycursor:
        a = i[0]

        break
    mycursor.execute("SELECT product_a,product_b,counts FROM setcount3 WHERE product_c='{}' UNION SELECT product_a,product_c,counts FROM setcount3 WHERE product_b='{}' UNION SELECT product_b,product_c,counts FROM setcount3 WHERE product_a='{}' ORDER BY counts desc limit 7".format(entry.get(),entry.get(),entry.get()))


    j = 1
    for i in mycursor:

        b = round((i[2] / a) * 100)
        if (b >= confidence_value):
            if (j <= 8):
                slices.append(b)
                tick_label.append(entry.get() + '-->' + i[0] + '&' + i[1])
                left.append(j)
                height.append(int(b))
                j += 1

                activities.append(convertTuple(i[0]))

    plt.bar(left, height, tick_label=tick_label, width=0.8, color=['red', 'green'])

    # naming the x-axis
    plt.ylabel('Confidence in %')
    # naming the y-axis
    plt.xlabel('Items')
    # plot title
    plt.title('CONFIDENCE OF PRODUCT  '+entry.get())

    # function to show the plot
    plt.show()
def conf_graph4():
    left = []
    activities=[]

    # heights of bars
    height = []
    slices=[]
    # labels for bars
    tick_label = []
    mydb= mysql.connector.connect(host='127.0.0.1', user='root', passwd='9680', database='market')
    mycursor = mydb.cursor()
    mycursor.execute('select * from confidence')
    for key in mycursor:
        confidence_value = key[0]
        break
    mycursor.execute("SELECT count FROM products WHERE  product LIKE '%{}%'".format(entry.get()))
    for i in mycursor:
        a = i[0]

        break
    mycursor.execute("SELECT product_a,product_b,product_c,counts FROM setcount4 WHERE product_d='{}' UNION SELECT product_a,product_b,product_d,counts FROM setcount4 WHERE product_c='{}' UNION SELECT product_a,product_c,product_d,counts FROM setcount4 WHERE product_b='{}' union SELECT product_b,product_c,product_d,counts FROM setcount4 WHERE product_a='{}' ORDER BY counts desc limit 7".format(entry.get(),entry.get(),entry.get(),entry.get()))


    j = 1
    for i in mycursor:

        b = round((i[3] / a) * 100)
        if (b >= confidence_value):
            if (j <= 8):
                slices.append(b)
                tick_label.append(entry.get()+'-->'+i[0]+','+i[1]+'&'+i[2])
                left.append(j)
                height.append(int(b))
                j += 1

    # plotting a bar chart
    plt.bar(left, height, tick_label=tick_label, width=0.8, color=['red', 'green'])

    # naming the x-axis
    plt.ylabel('Confidence in %')
    # naming the y-axis
    plt.xlabel('Items')
    # plot title
    plt.title('CONFIDENCE OF PRODUCT  '+entry.get())

    # function to show the plot
    plt.show()









###############################################################################################################

def grids():
    scrollbar = Scrollbar(newroot)
    scrollbar.pack(side=LEFT, fill=Y)

    csvfile= open('test.csv')
    readCSV = csv.reader(csvfile, delimiter=',')

    mylist1 = Listbox(newroot, yscrollcommand=scrollbar.set)
    a=0

    for i in readCSV:
        b=[]
        for j in range(len(i)):
            b.append(i[j])
            b.append('   ')

        if a==0:
            for k in range(2):
                mylist1.insert(END,'')

        mylist1.insert(END,' '+convertTuple(b))
        a=1
    mylist1.pack(fill=BOTH,expand=2,side=LEFT)
    scrollbar.config(command=mylist1.yview)

def freq_graph1():
    left = []

    # heights of bars
    height = []

    # labels for bars
    tick_label = []
    mydb = mysql.connector.connect(host='127.0.0.1', user='root', passwd='9680', database='market')
    mycursor = mydb.cursor()
    mycursor.execute("select * from products  limit 7")
    j = 1
    for i in mycursor:
        tick_label.append(convertTuple(i[0]))
        left.append(j)
        height.append(int(i[1]))
        j += 1

    # plotting a bar chart
    plt.bar(left, height, tick_label=tick_label, width=0.8, color=['red', 'green'])

    # naming the x-axis
    plt.ylabel('Frequency')
    # naming the y-axis
    plt.xlabel('Items')
    # plot title
    plt.title('Items VS Frequency')

    # function to show the plot
    plt.show()



def freq_graph2():
    left = []

    # heights of bars
    height = []

    # labels for bars
    tick_label = []
    mydb222 = mysql.connector.connect(host='127.0.0.1', user='root', passwd='9680', database='market')
    mycursor222 = mydb222.cursor()
    mycursor222.execute("select product_2,count from secondset2 where product_1='{}' union select product_1,count from secondset2 where product_2='{}' order by count desc limit 7".format(entry.get(),entry.get()))

    j = 1
    csvfile = open('test.csv')
    readCSV = csv.reader(csvfile, delimiter=',')

    total = 0
    for i in readCSV:
        total+=1
    for i in mycursor222:
        if(j<=7):
            tick_label.append(entry.get()+'&'+i[0])
            left.append(j)
            height.append((i[1]/total)*100)
            j += 1
        else:
            break
    # plotting a bar chart
    plt.bar(left, height, tick_label=tick_label, width=0.8, color=['red', 'green'])

    # naming the x-axis
    plt.ylabel('Support')
    # naming the y-axis
    plt.xlabel('Items')
    # plot title
    plt.title('Items VS Support of   ' +entry.get())

    # function to show the plot
    plt.show()
def freq_graph3():
    left = []

    # heights of bars
    height = []

    # labels for bars
    tick_label = []
    mydb333 = mysql.connector.connect(host='127.0.0.1', user='root', passwd='9680', database='market')
    mycursor333 = mydb333.cursor()
    mycursor333.execute("SELECT product_a,product_b,counts FROM setcount3 WHERE product_c='{}' UNION SELECT product_a,product_c,counts FROM setcount3 WHERE product_b='{}' UNION SELECT product_b,product_c,counts FROM setcount3 WHERE product_a='{}' ORDER BY counts desc limit 7".format(entry.get(),entry.get(),entry.get()))


    j = 1
    csvfile = open('test.csv')
    readCSV = csv.reader(csvfile, delimiter=',')

    total = 0
    for i in readCSV:
        total += 1
    for i in mycursor333:
        tick_label.append(entry.get()+','+i[0]+'&'+i[1])
        left.append(j)
        height.append((i[2]/total)*100)
        j += 1

    # plotting a bar chart
    plt.bar(left, height, tick_label=tick_label, width=0.8, color=['red', 'green'])

    # naming the x-axis
    plt.ylabel('Support')
    # naming the y-axis
    plt.xlabel('Items')
    # plot title
    plt.title('Items VS Support OF PRODUCT  '+entry.get())

    # function to show the plot
    plt.show()
def freq_graph4():
    left = []

    # heights of bars
    height = []

    # labels for bars
    tick_label = []
    mydb444 = mysql.connector.connect(host='127.0.0.1', user='root', passwd='9680', database='market')
    mycursor444 = mydb444.cursor()
    mycursor444.execute("SELECT product_a,product_b,product_c,counts FROM setcount4 WHERE product_d='{}' UNION SELECT product_a,product_b,product_d,counts FROM setcount4 WHERE product_c='{}' UNION SELECT product_a,product_c,product_d,counts FROM setcount4 WHERE product_b='{}' union SELECT product_b,product_c,product_d,counts FROM setcount4 WHERE product_a='{}' ORDER BY counts desc limit 7".format(entry.get(),entry.get(),entry.get(),entry.get()))


    j = 1
    csvfile = open('test.csv')
    readCSV = csv.reader(csvfile, delimiter=',')

    total = 0
    for i in readCSV:
        total += 1
    for i in mycursor444:
        tick_label.append(entry.get()+','+i[0]+','+i[1]+'&'+i[2])
        left.append(j)
        height.append((i[3]/total)*100)
        j += 1

    # plotting a bar chart
    plt.bar(left, height, tick_label=tick_label, width=0.8, color=['red', 'green'])

    # naming the x-axis
    plt.ylabel('SUPPORT')
    # naming the y-axis
    plt.xlabel('Items')
    # plot title
    plt.title('Items VS SUPPORT OF PRODUCT  '+entry.get())

    # function to show the plot
    plt.show()



#####################




def confidence(count):

    mydb = mysql.connector.connect(host='127.0.0.1', user='root', passwd='9680', database='market')
    mycursor = mydb.cursor()
    mydb444 = mysql.connector.connect(host='127.0.0.1', user='root', passwd='9680', database='market')
    mycursor444 = mydb444.cursor()
    mycursor444.execute('select * from confidence')
    for key in mycursor444:
        confidence_value = key[0]
        break

    newroot3 = Tk()
    j=1

    scrollbar1 = Scrollbar(newroot3)
    scrollbar1.pack(side=RIGHT, fill=Y)


    csvfile1 = open('test.csv')
    readCSV1 = csv.reader(csvfile1, delimiter=',')

    mylist1 = Listbox(newroot3, yscrollcommand=scrollbar1.set)
    a = 0
    for i in readCSV1:
        b = []
        for j in range(len(i)):
            b.append(i[j])
            b.append('   ')

        if a == 0:
            for k in range(2):
                mylist1.insert(END, '')
        mylist1.insert(END, ' ' + convertTuple(b))
        a = 1
    mylist1.pack(fill=BOTH,expand=2 ,side=RIGHT)
    scrollbar1.config(command=mylist1.yview)



    newroot3.title('CONFIDENCE OF '+entry.get())
    newroot3.geometry('640x480')
    mycursor.execute("SELECT count FROM products WHERE  product LIKE '%{}%'".format(entry.get()))
    for i in mycursor:
        a=i[0]

        break
    if(count==1):

        mycursor1=mydb.cursor()
        mycursor1.execute("select product_2,count from secondset2 where product_1='{}' union select product_1,count from secondset2 where product_2='{}' order by count desc".format(entry.get(),entry.get()))
    if(count==2):
        mycursor1 = mydb.cursor()
        mycursor1.execute("SELECT product_a,product_b,counts FROM setcount3 WHERE product_c='{}' UNION SELECT product_a,product_c,counts FROM setcount3 WHERE product_b='{}' UNION SELECT product_b,product_c,counts FROM setcount3 WHERE product_a='{}' ORDER BY counts desc".format(entry.get(),entry.get(),entry.get()))

    if(count==3):


        mycursor1=mydb.cursor()
        mycursor1.execute("SELECT product_a,product_b,product_c,counts FROM setcount4 WHERE product_d='{}' UNION SELECT product_a,product_b,product_d,counts FROM setcount4 WHERE product_c='{}' UNION SELECT product_a,product_c,product_d,counts FROM setcount4 WHERE product_b='{}' union SELECT product_b,product_c,product_d,counts FROM setcount4 WHERE product_a='{}' ORDER BY counts desc".format(entry.get(),entry.get(),entry.get(),entry.get()))

    scrollbar = Scrollbar(newroot3)
    scrollbar.pack(side=LEFT, fill=Y)
    mylist = Listbox(newroot3, yscrollcommand=scrollbar.set)
    #confidence_graph(count)
    ll=0

    for i in mycursor1:

        if(count==1):
            bottom30 = Button(newroot3, text='Confidence Graph', bg='blue', fg='black', command=conf_graph2).place(x=250,y=250)

            b=round((i[1]/a)*100)
            if(b>=confidence_value):

                mylist.insert(END, entry.get()+'  -->  '+convertTuple(i[0])+'  =  '+str(b)+'%')
        if(count == 2):
            b=round((i[2]/a)*100)
            bottom30 = Button(newroot3, text='Confidence Graph', bg='blue', fg='black', command=conf_graph3).place(x=250,y=250)
            if (b >= confidence_value):


                mylist.insert(END,entry.get()+'  -->  '+convertTuple(i[0]) + '&\t'+convertTuple(i[1])+'  =  '+str(b)+'%')
        if (count == 3):
            b=round((i[3]/a)*100)
            bottom30 = Button(newroot3, text='Confidence Graph', bg='blue', fg='black', command=conf_graph4).place(x=250,y=250)
            if (b >= confidence_value):

                mylist.insert(END,entry.get()+'  -->  '+convertTuple(i[0])+',\t'+convertTuple(i[1])+' &\t'+convertTuple(i[2])+'  =  '+str(b)+'%')

    mylist.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=mylist.yview)


    level3 = Label(newroot3, text='TRANSACTION', fg='blue', font='times 8').place(x=210, y=15)






def convertTuple(tup):
    str = ''.join(tup)
    return str

def grid():

    newroot2 = Tk()
    newroot2.title('ALL PRODUCT')
    newroot2.geometry('640x480')
    csvfile = open('test.csv')
    readCSV = csv.reader(csvfile, delimiter=',')

    scrollbar = Scrollbar(newroot2)
    scrollbar.pack(side=RIGHT, fill=Y)

    mylist = Listbox(newroot2, yscrollcommand=scrollbar.set)
    for i in readCSV:

        mylist.insert(END,convertTuple(i))
    mylist.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=mylist.yview)

def declare(h):
    #newroot.destroy()
    newroot1 = Tk()
    mydb = mysql.connector.connect(host='127.0.0.1', user='root', passwd='9680', database='market')
    mycursor = mydb.cursor()
    newroot1.title('SHOW PRODUCT')
    newroot1.geometry('640x480')
    b1= partial(confidence, 1)
    b2 = partial(confidence, 2)
    b3 = partial(confidence,3)
    scrollbar = Scrollbar(newroot)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar.pack(side=BOTTOM, fill=X)
    csvfile = open('test.csv')
    readCSV = csv.reader(csvfile, delimiter=',')

    mylist1 = Listbox(newroot1, yscrollcommand=scrollbar.set)
    a = 0
    for i in readCSV:
        b = []
        for j in range(len(i)):
            b.append(i[j])
            b.append('   ')

        if a == 0:
            for k in range(2):
                mylist1.insert(END, '')
        mylist1.insert(END, ' ' + convertTuple(b))
        a = 1
    mylist1.pack(fill=BOTH,expand=2, side=RIGHT)
    scrollbar.config(command=mylist1.yview)
    Label(newroot1, text='TRANSACTION', fg='blue', font='times 8').place(x=20, y=10)
    if h==1:

        Button(newroot1, text='Pair', bg='white', fg='black', command=onetoone).place(x=450, y=150)
        Button(newroot1, text='Triplet', bg='white', fg='black', command=printt1).place(x=450, y=200)
        Button(newroot1, text='Quadruplet', bg='white', fg='black', command=printt2).place(x=450, y=250)
    if h==2:

        Button(newroot1, text='Pair', bg='white', fg='black', command=b1).place(x=450, y=150)
        Button(newroot1, text='Triplet', bg='white', fg='black', command=b2).place(x=450, y=200)
        Button(newroot1, text='Quadruplet', bg='white', fg='black', command=b3).place(x=450, y=250)



def onetoone():
    #newroot.destroy()
    mydb = mysql.connector.connect(host='127.0.0.1', user='root', passwd='9680', database='market')
    mycursor = mydb.cursor()



    newroot2 = Tk()
    newroot2.title('RELATED PRODUCT OF  '+entry.get())
    newroot2.geometry('640x480')
    mycursor.execute("select product_2,count from secondset2 where product_1='{}' union select product_1,count from secondset2 where product_2='{}' order by count desc".format(entry.get(),entry.get()))
    scrollbar = Scrollbar(newroot2)
    scrollbar.pack(side=LEFT, fill=Y)


    mylist = Listbox(newroot2, yscrollcommand=scrollbar.set)
    scrollbar1 = Scrollbar(newroot2)
    scrollbar1.pack(side=RIGHT, fill=Y)

    csvfile = open('test.csv')
    readCSV = csv.reader(csvfile, delimiter=',')

    mylist1 = Listbox(newroot2, yscrollcommand=scrollbar1.set)
    a = 0
    total=0
    for i in readCSV:
        b = []
        for j in range(len(i)):
            b.append(i[j])
            b.append('   ')

        if a == 0:
            for k in range(2):
                mylist1.insert(END, '')
        total+=1
        mylist1.insert(END, ' ' + convertTuple(b))
        a = 1
    mylist1.pack(fill=BOTH, side=RIGHT,expand=2)
    scrollbar1.config(command=mylist1.yview)

    for i in mycursor:



        mylist.insert(END,entry.get()+' & '+i[0]+'-->'+str((i[1]/total)*100)+'%')


    mylist.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=mylist.yview)
    level3 = Label(newroot2, text='TRANSACTION', fg='blue', font='times 8').place(x=210, y=15)
    bottom30 = Button(newroot2, text='Graph', bg='blue', fg='black', command=freq_graph2).place(x=250, y=250)




def printt1():
    #newroot.destroy()
    mydb = mysql.connector.connect(host='127.0.0.1', user='root', passwd='9680', database='market')
    mycursor = mydb.cursor()


    mycursor.execute("SELECT product_a,product_b,counts FROM setcount3 WHERE product_c='{}' UNION SELECT product_a,product_c,counts FROM setcount3 WHERE product_b='{}' UNION SELECT product_b,product_c,counts FROM setcount3 WHERE product_a='{}' ORDER BY counts desc".format(entry.get(),entry.get(),entry.get()))



    newroot2 = Tk()

    newroot2.title('RELATED PRODUCT OF  '+entry.get())
    newroot2.geometry('640x480')
    Button(newroot2, text='Grid', bg='white', fg='black', command=grid).place(x=450, y=250)
    scrollbar = Scrollbar(newroot2)
    scrollbar.pack(side=LEFT, fill=Y)
    scrollbar1 = Scrollbar(newroot2)
    scrollbar1.pack(side=RIGHT, fill=Y)

    csvfile = open('test.csv')
    readCSV = csv.reader(csvfile, delimiter=',')

    mylist1 = Listbox(newroot2, yscrollcommand=scrollbar1.set)
    a = 0

    total=0
    for i in readCSV:
        b = []
        for j in range(len(i)):
            b.append(i[j])
            b.append('   ')

        if a == 0:
            for k in range(2):
                mylist1.insert(END, '')
        mylist1.insert(END, ' ' + convertTuple(b))
        a = 1
        total+=1
    mylist1.pack(fill=BOTH,expand=2, side=RIGHT)
    scrollbar1.config(command=mylist1.yview)

    mylist = Listbox(newroot2, yscrollcommand=scrollbar.set)

    for i in mycursor:

        mylist.insert(END,entry.get()+', '+ i[0]+'  &  '+i[1]+'-->'+str((i[2]/total)*100)+'%')

    mylist.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=mylist.yview)
    level3 = Label(newroot2, text='TRANSACTION', fg='blue', font='times 8').place(x=210, y=15)
    bottom30 = Button(newroot2, text='Graph', bg='blue', fg='black', command=freq_graph3).place(x=250, y=250)
def printt2():
    #newroot.destroy()
    mydb = mysql.connector.connect(host='127.0.0.1', user='root', passwd='9680', database='market')
    mycursor = mydb.cursor()


    mycursor.execute("SELECT product_a,product_b,product_c,counts FROM setcount4 WHERE product_d='{}' UNION SELECT product_a,product_b,product_d,counts FROM setcount4 WHERE product_c='{}' UNION SELECT product_a,product_c,product_d,counts FROM setcount4 WHERE product_b='{}' union SELECT product_b,product_c,product_d,counts FROM setcount4 WHERE product_a='{}' ORDER BY counts desc".format(entry.get(),entry.get(),entry.get(),entry.get()))


    newroot2 = Tk()
    newroot2.title('RELATED PRODUCT OF  '+entry.get())
    newroot2.geometry('640x480')

    scrollbar = Scrollbar(newroot2)
    scrollbar.pack(side=LEFT, fill=Y)

    mylist = Listbox(newroot2, yscrollcommand=scrollbar.set)
    scrollbar1 = Scrollbar(newroot2)
    scrollbar1.pack(side=RIGHT, fill=Y)

    csvfile = open('test.csv')
    readCSV = csv.reader(csvfile, delimiter=',')

    mylist1 = Listbox(newroot2, yscrollcommand=scrollbar1.set)
    a = 0
    total=0
    for i in readCSV:
        b = []
        for j in range(len(i)):
            b.append(i[j])
            b.append('   ')

        if a == 0:
            for k in range(2):
                mylist1.insert(END, '')
        mylist1.insert(END, ' ' + convertTuple(b))
        total+=1
        a = 1
    mylist1.pack(fill=BOTH,expand=2, side=RIGHT)
    scrollbar1.config(command=mylist1.yview)

    for i in mycursor:

        mylist.insert(END,entry.get()+', '+i[0]+',  '+i[1]+'  &  '+i[2]+'-->'+str((i[3]/total)*100)+'%')
    mylist.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=mylist.yview)
    Label(newroot2, text='TRANSACTION', fg='blue', font='times 8').place(x=210, y=15)
    bottom3 = Button(newroot2, text='Graph', bg='blue', fg='black', command=freq_graph4).place(x=250, y=250)


newroot=Tk()

newroot.title('SHOW PRODUCT')
newroot.geometry('640x480')
level2 = Label(newroot, text='SEARCH FREQUENT ITEMSETS', fg='green', font='times 15').pack()
grids()


mydb = mysql.connector.connect(host='127.0.0.1', user='root', passwd='9680', database='market')
mycursor = mydb.cursor()

mycursor.execute("select product from products order by count desc")
scrollbar = Scrollbar(newroot)
scrollbar.pack(side=LEFT ,fill=Y)
mylist = Listbox(newroot, yscrollcommand=scrollbar.set)
a=0
for i in mycursor:
    if(a==0):
        for j in range(2):
            mylist.insert(END,'')

    a=1
    mylist.insert(END,' '+i[0])
mylist.pack(side=RIGHT, fill=BOTH)
scrollbar.config(command=mylist.yview)
level3 = Label(newroot, text='ITEMS', fg='blue', font='times 8').place(x=530,y=35)
entry = Entry()

entry.place(x=120, y=100)

level3 = Label(newroot, text='TRANSACTION', fg='blue', font='times 8').place(x=210,y=35)
a1 = partial(declare,1)
a2=partial(declare,2)
bottom1 = Button(newroot, text='search for support', bg='red', fg='black', command=a1).place(x=130, y=140)
bottom2 = Button(newroot, text='search for confidence', bg='red', fg='black', command=a2).place(x=130, y=200)
bottom3 = Button(newroot, text='Frequent Graph', bg='yellow', fg='black', command=freq_graph1).place(x=130, y=250)


newroot.mainloop()



