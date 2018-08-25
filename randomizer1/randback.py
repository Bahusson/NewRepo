import sqlite3
import pandas

def connect(var):
    conn=sqlite3.connect("Lotto.db")
    cur=conn.cursor()
    if var == 1 :
        df = pandas.read_csv('http://www.mbnet.com.pl/ml.txt',header =None, sep='[., ]', engine ='python')
        df.rename(columns={'2': 'day', '3': 'month', '4' : 'year'}, inplace=True)
        df1= df.drop(df.columns[0:2],1)
        df1.to_sql('game1', conn, if_exists='replace', index=False)
    elif var == 2 :
        df = pandas.read_csv('http://www.mbnet.com.pl/dl.txt',header =None, sep='[., ]', engine ='python')
        df1= df.drop(df.columns[0:2],1)
        df1.to_sql('game2', conn, if_exists='replace', index=False)
    elif var == 3 :
        df = pandas.read_csv('http://www.mbnet.com.pl/el.txt',header =None, sep='[., ]', engine ='python')
        df1= df.drop(df.columns[0:2],1)
        df1.to_sql('game3', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()

#funkcja szukająca po dacie - ni chuja nie wiem jak to na razie zrobić...
def searchA(day,month,year):
    conn=sqlite3.connect("Lotto.db")
    cur=conn.cursor()
    cur.execute("SELECT FROM game WHERE day=?, month=?, year=?",(day,month,year))
    rows=cur.fetchall()
    conn.close()
    return rows

#Funkcja searchall dla checkboxa ściągająca dane z całej bazy danych. Zanim zaczniesz cokolwiek podpinać warto ją zrobić i na niej wszystko testować. Kalendarz zrobisz później...
def searchallbox(var):
    #miżna wstawić zmienną nazwy bazy danych zamiast pisać to 4 razy...
    conn=sqlite3.connect("Lotto.db")
    cur=conn.cursor()
    if var == 1 :
        cur.execute("SELECT * FROM game1 ")
    elif var == 2 :
        cur.execute("SELECT * FROM game2 ")
    elif var == 3 :
        cur.execute("SELECT * FROM game3 ")
    rows=cur.fetchall()
    conn.close()
    return rows

connect(1)
connect(2)
connect(3)

#def calmenu():
