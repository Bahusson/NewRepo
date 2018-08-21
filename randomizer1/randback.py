import sqlite3
import pandas
import random


def connect(var):
    conn=sqlite3.connect("Lotto.db")
    cur=conn.cursor()
    if var == 1 :
        df = pandas.read_csv('http://www.mbnet.com.pl/ml.txt',header =None, sep='[., ]', engine ='python')
        df.to_sql('game1', conn, if_exists='replace', index=False)
    elif var == 2 :
        df = pandas.read_csv('http://www.mbnet.com.pl/dl.txt',header =None, sep='[., ]', engine ='python')
        df.to_sql('game2', conn, if_exists='replace', index=False)
    elif var == 3 :
        df = pandas.read_csv('http://www.mbnet.com.pl/el.txt',header =None, sep='[., ]', engine ='python')
        df.to_sql('game3', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()

def searchA(day,month,year):
    conn=sqlite3.connect("Lotto.db")
    cur=conn.cursor()
    cur.execute("SELECT FROM game WHERE day=?, month=?, year=?",(day,month,year))
    rows=cur.fetchall()
    conn.close()
    return rows

#Funkcja searchall dla checkboxa ściągająca dane z całej bazy danych. Zanim zaczniesz cokolwiek podpinać warto ją zrobić i na niej wszystko testować. Kalendarz zrobisz później...
def searchallbox():
    #miżna wstawić zmienną nazwy bazy danych zamiast pisać to 4 razy...
    conn=sqlite3.connect("Lotto.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM game ")
    rows=cur.fetchall()
    conn.close()
    return rows

connect(1)
connect(2)
connect(3)
