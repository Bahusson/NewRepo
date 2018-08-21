import sqlite3


        #Zrób ten myk, żeby przy komendzie insert sprawdzał, czy wartości już tam są, żeby ich nie ładował ponownie z internetu.
def radio(ch=1):
    if ch == 1 :
        fradio = "MultiMulti.db"
        gamecre= "CREATE TABLE IF NOT EXISTS game (id INTEGER PRIMARY KEY, day integer, month integer, year integer, n1 integer, n2 integer, n3 integer, n4 integer, n5 integer, n6 integer, n7 integer, n8 integer, n9 integer, n10 integer, n11 integer, n12 integer, n13 integer, n14 integer, n15 integer, n16 integer, n17 integer, n17 integer, n18 integer, n19 integer, n20 integer, np integer)"
        gameins="INSERT INTO game VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(day,month,year,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,np)
    elif ch == 2 :
        fradio = "Lotto.db"
        gamecre= "CREATE TABLE IF NOT EXISTS game (id INTEGER PRIMARY KEY, day integer, month integer, year integer, n1 integer, n2 integer, n3 integer, n4 integer, n5 integer, n6 integer)"
        gameins="INSERT INTO game VALUES (NULL,?,?,?,?,?,?,?,?,?)",(day,month,year,n1,n2,n3,n4,n5,n6)
    elif ch == 3 :
        fradio = "EuroJackpot.db"
        gamecre= "CREATE TABLE IF NOT EXISTS game (id INTEGER PRIMARY KEY, day integer, month integer, year integer, n1 integer, n2 integer, n3 integer, n4 integer, n5 integer, np1 integer, np2 integer)"
        gameins="INSERT INTO game VALUES (NULL,?,?,?,?,?,?,?,?,?,?)",(day,month,year,n1,n2,n3,n4,n5,np1,np2)
    elif ch == 4 :
        fradio = "EkstraPensja.db"
        gamecre= "CREATE TABLE IF NOT EXISTS game (id INTEGER PRIMARY KEY, day integer, month integer, year integer, n1 integer, n2 integer, n3 integer, n4 integer, n5 integer, np integer)"
        gameins="INSERT INTO game VALUES (NULL,?,?,?,?,?,?,?,?,?)",(day,month,year,n1,n2,n3,n4,n5,n6)

def connectA():
    conn=sqlite3.connect("Multi.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS game (id INTEGER, day integer, month integer, year integer, n1 integer, n2 integer, n3 integer, n4 integer, n5 integer, n6 integer, n7 integer, n8 integer, n9 integer, n10 integer, n11 integer, n12 integer, n13 integer, n14 integer, n15 integer, n16 integer, n17 integer, n17 integer, n18 integer, n19 integer, n20 integer, np integer)"
    conn.commit()
    conn.close()

def connectB():
    conn=sqlite3.connect("Lotto.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS game (id integer, day integer, month integer, year integer, n1 integer, n2 integer, n3 integer, n4 integer, n5 integer, n6 integer)")
    conn.commit()
    conn.close()

def connectC():
    conn=sqlite3.connect("Mini.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS game (id integer, day integer, month integer, year integer, n1 integer, n2 integer, n3 integer, n4 integer, n5 integer, n6 integer)")
    conn.commit()
    conn.close()

def connect():
    conn=sqlite3.connect(radio().fradio)
    cur=conn.cursor()
    cur.execute(gamecre)
    conn.commit()
    conn.close()

def insert():
    conn=sqlite3.connect(fradio)
    cur=conn.cursor()
    cur.execute(gameins)
    conn.commit()
    conn.close()

#Pamiętaj, że masz dwa searche, jeden DO, a jeden OD i one muszą współgrać, więc ten jeszcze nie robi roboty... :(
def search():
    conn=sqlite3.connect(fradio)
    cur=conn.cursor()
    cur.execute("SELECT FROM game WHERE day=?, month=?, year=?",(day,month,year))
    rows=cur.fetchall()
    conn.close()
    return rows

#Funkcja searchall dla checkboxa ściągająca dane z całej bazy danych. Zanim zaczniesz cokolwiek podpinać warto ją zrobić i na niej wszystko testować. Kalendarz zrobisz później...
def searchallbox():
    conn=sqlite3.connect(fradio)
    cur=conn.cursor()
    cur.execute("SELECT * FROM game ")
    rows=cur.fetchall()
    conn.close()
    return rows

connect()
