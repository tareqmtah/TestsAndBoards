import re
from csv import reader
import datetime
import mysql.connector
import pymysql
def checkBoards2(mylist,Vboards):
    for y in range(len(mylist)):
        flag = True
        preph1= mylist[y][4]
        mypreph1=0
        mypreph2=0
        if preph1 == 'Yes':
            mypreph1=1
        else :
            mypreph1=0
        preph2 =  mylist[y][5]
        if preph2 == 'Yes':
            mypreph2=1
        else:
            mypreph2=0
        while flag == True:
            flag = False
            for x in Vboards:
                version=  str(x[3]) + '.' +  str(x[4])
                if re.match(x[2].replace("'",""),mylist[y][2].split()[0],re.IGNORECASE) and x[8]==0 and \
                        int(x[1]) >= int(mylist[y][1]) and  float(mylist[y][2].split()[1]) <= float(version) and mypreph1 == x[6] and mypreph2 == x[7]:
                    print ('match ' + str(x) + " " + mylist[y][0] + str(mylist[y][2].split()[0]) + " " + str(x[1]) + " <= " +  str(mylist[y][1]) + " " + str(version) + " " +  str(mylist[y][2].split()[1] ))
                    updatequery("update boards set InUse = 1 where Inuse=0 and  BoardName = " + "'" + str(x[0] ) + "'")
                    Vboards = querysql('select * from boards where InUse = 0 order by Memory DESC')
                    flag = True
                    break;

def getValidTests(mylist):
    testlist=[]
    print ( "Valid tests are :")
    for rows in range(len(mylist)):
            if re.search('.*regression[ ]{0,4}[0-9]{1}',mylist[rows][0],re.IGNORECASE) :
                testlist.append(mylist[rows])
                print(mylist[rows])
    return testlist
def getItemFromCSV ():
# read csv file as a list of lists
    with open('tests2.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        list_of_rows = list(csv_reader)
        validBoards=querysql('select * from boards where InUse = 0 order by Memory DESC')
        print('Available Boards Are: ')
        for row in validBoards :
            print(row)
        checkBoards2(getValidTests(list_of_rows),validBoards)
def querysql (mystring):
        retVal =[]
        cnx = mysql.connector.connect(host="10.225.180.220", user="root", password="Admin11!",database="dom")
        cursor = cnx.cursor()
        query = mystring
        cursor.execute(query)
        for x in cursor.fetchall():
            retVal.append(x)
        cursor.close()
        cnx.close()
        return retVal
def updatequery (mystring):
        retVal =[]
        cnx = mysql.connector.connect(host="10.225.180.220", user="root", password="Admin11!",database="dom")
        cursor = cnx.cursor(buffered=True)
        query = mystring
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()
                    
if __name__ == '__main__':
    getItemFromCSV()
