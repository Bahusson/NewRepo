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

#funkcja szukająca po dacie
def searchA(base,day1,month1,year1,day2,month2,year2):
    conn=sqlite3.connect("Lotto.db")
    cur=conn.cursor()
    if base == 1:
        cur.execute('SELECT MIN(rowid) FROM game1 WHERE "2"=? AND "3"=? AND "4"=?',(day2,month2,year2))
        rowfrom=(cur.fetchone()[0])
        cur.execute('SELECT MAX(rowid) FROM game1 WHERE "2"=? AND "3"=? AND "4"=?',(day1,month1,year1))
        rowto=(cur.fetchone()[0])-rowfrom
        cur.execute('SELECT * FROM game1 LIMIT ? OFFSET ?', (rowto, rowfrom))
    elif base == 2:
        cur.execute('SELECT MAX(rowid) FROM game2 WHERE "2"<=? AND "3"=? AND "4"=?',(day2,month2,year2))
        rowfrom=(cur.fetchone()[0])
        cur.execute('SELECT MIN(rowid) FROM game2 WHERE "2">=? AND "3"=? AND "4"=?',(day1,month1,year1))
        rowto=(cur.fetchone()[0])-rowfrom
        cur.execute('SELECT * FROM game2 LIMIT ? OFFSET ?', (rowto, rowfrom))
    elif base == 3:
        cur.execute('SELECT MAX(rowid) FROM game2 WHERE "2"<=? AND "3"=? AND "4"=?',(day2,month2,year2))
        rowfrom=(cur.fetchone()[0])
        cur.execute('SELECT MIN(rowid) FROM game2 WHERE "2">=? AND "3"=? AND "4"=?',(day1,month1,year1))
        rowto=(cur.fetchone()[0])-rowfrom
        cur.execute('SELECT * FROM game2 LIMIT ? OFFSET ?', (rowto, rowfrom))
    elif base == 4:
        pass
    rows=cur.fetchall()
    conn.close()
    return rows

#Funkcja searchall dla checkboxa ściągająca dane z całej bazy danych. Zanim zaczniesz cokolwiek podpinać warto ją zrobić i na niej wszystko testować. Kalendarz zrobisz później...
def searchallbox(var):
    conn=sqlite3.connect("Lotto.db")
    cur=conn.cursor()
    if var == 1 :
        cur.execute('SELECT * FROM game1')
    elif var == 2 :
        cur.execute('SELECT * FROM game2')
    elif var == 3 :
        cur.execute('SELECT * FROM game3')
    elif var == 4 :
        pass
    rows=cur.fetchall()
    conn.close()
    return rows

#Ta funkcja jest do obliczeń na samych liczbach, tj. jest niewidoczna dla użytkownika dopóki nie zamówi grafu. NIEPODŁĄCZONA!!!
def searchvalbox(var):
    conn=sqlite3.connect("Lotto.db")
    cur=conn.cursor()
    if var == 1 :
        cur.execute('SELECT "5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24" FROM game1')
    elif var == 2 :
        cur.execute('SELECT "5","6","7","8","9","10" FROM game2')
    elif var == 3 :
        cur.execute('SELECT "5","6","7","8","9" FROM game3')
    elif var == 4 :
        pass
    rows=cur.fetchall()
    conn.close()
    return rows



connect(1)
connect(2)
connect(3)

#def calmenu():
