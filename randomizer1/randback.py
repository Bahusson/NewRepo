import sqlite3
import pandas
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource

def connect(var):
    conn=sqlite3.connect("Lotto.db")
    cur=conn.cursor()
    if var == 1 :
        df = pandas.read_csv('http://www.mbnet.com.pl/ml.txt',header =None, sep='[., ]', engine ='python')
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


global rowfrom
#funkcja szukająca po dacie
def searchA(base,day1,month1,year1,day2,month2,year2):
    conn=sqlite3.connect("Lotto.db")
    cur=conn.cursor()
    if base == 1:
        cur.execute('SELECT MIN(rowid) FROM game1 WHERE "2"=? AND "3"=? AND "4"=?',(day2,month2,year2))
        global rowfrom
        rowfrom=(cur.fetchone()[0])
        cur.execute('SELECT MAX(rowid) FROM game1 WHERE "2"=? AND "3"=? AND "4"=?',(day1,month1,year1))
        global rowto
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

#Ta funkcja jest do obliczeń na samych liczbach, tj. jest niewidoczna dla użytkownika dopóki nie zamówi grafu.
#NIEPODŁĄCZONA!!! (Chyba będzie niepotrzebna, bo będę liczył na rekonwertowanym df...)
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

def makegraph():
        p=figure(plot_width=500, plot_height=400, tools = 'pan, reset', logo=None)
        p.title.text = "Dystrybucja"
        p.title.text_color = "Orange"
        p.title.text_font = "times"
        p.title.text_font_style = "italic"
        p.yaxis.minor_tick_line_color = "Yellow"
        p.xaxis.axis_label = "Średnie"
        p.yaxis.axis_label = "Częstotliwości"
        p.circle(x='Means', y='Freqs', source=source, size = 10, color="red", alpha=0.6)
        hover=HoverTool(tooltips=[("Mean","@Means"),("Freq","@Freqs")])
        p.add_tools(hover)
        output_file('graph1.html')
        show(p)

#To funkcja rekonwertująca bazę danych do df aby można było zrobić graf i inne fajne rzeczy na liczbach...
#Ciekawe dlaczego jak wywołuje się średnie, to również dwa razy wywala graf. O.o
def makedf(var1,var2):
    df = pandas.read_sql_query(
        sql=('SELECT * FROM game1 LIMIT ? OFFSET ?'),
        con=sqlite3.connect("Lotto.db"), coerce_float=False, params=[rowto, rowfrom], parse_dates=None, chunksize=None)
    df1=df.drop(df.columns[0:3],1)
    df4=df1.T
    df5=df4.mean().round(0).value_counts()
    zipped = zip(df5.index, df5.values)
    a=list(zipped)
    global source
    source = ColumnDataSource(
        data=dict(
            Means=df5.index,
            Freqs=df5.values
            ))
    if var1 == 1 and var2 == 1:
            makegraph()
            return a
    elif var1 == 0 and var2 == 1:
            makegraph()
    elif var1 == 1 and var2 == 0:
            return a
    else:
            pass





connect(1)
connect(2)
connect(3)

#def calmenu():
