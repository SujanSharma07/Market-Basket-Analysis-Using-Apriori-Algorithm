
import matplotlib.pyplot as plt
def convertTuple(tup):
    str = ''.join(tup)
    return str

# import os
from tkinter import ttk

import mysql.connector




def convertTuple(tup):
    str = ''.join(tup)
    return str

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
    plt.xlabel('Frequency')
    # naming the y-axis
    plt.ylabel('Items')
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
    mycursor222.execute("select * from secondset2  limit 7")
    j = 1
    for i in mycursor222:
        tick_label.append(convertTuple(i[0])+'&'+convertTuple(i[1]))
        left.append(j)
        height.append(int(i[2]))
        j += 1

    # plotting a bar chart
    plt.bar(left, height, tick_label=tick_label, width=0.8, color=['red', 'green'])

    # naming the x-axis
    plt.xlabel('Frequency')
    # naming the y-axis
    plt.ylabel('Items')
    # plot title
    plt.title('Items VS Frequency')

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
    mycursor333.execute("select * from setcount3  limit 7")
    j = 1
    for i in mycursor333:
        tick_label.append(convertTuple(i[0])+'&'+convertTuple(i[1])+convertTuple(i[2]))
        left.append(j)
        height.append(int(i[3]))
        j += 1

    # plotting a bar chart
    plt.bar(left, height, tick_label=tick_label, width=0.8, color=['red', 'green'])

    # naming the x-axis
    plt.xlabel('Frequency')
    # naming the y-axis
    plt.ylabel('Items')
    # plot title
    plt.title('Items VS Frequency')

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
    mycursor444.execute("select * from setcount4  limit 7")
    j = 1
    for i in mycursor444:
        tick_label.append(convertTuple(i[0])+'&'+convertTuple(i[1])+convertTuple(i[2])+convertTuple(i[3]))
        left.append(j)
        height.append(int(i[4]))
        j += 1

    # plotting a bar chart
    plt.bar(left, height, tick_label=tick_label, width=0.8, color=['red', 'green'])

    # naming the x-axis
    plt.xlabel('Frequency')
    # naming the y-axis
    plt.ylabel('Items')
    # plot title
    plt.title('Items VS Frequency')

    # function to show the plot
    plt.show()
