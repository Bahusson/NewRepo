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


#funkcja szukająca po dacie
def searchA(base,day1,month1,year1,day2,month2,year2):
    conn=sqlite3.connect("Lotto.db")
    cur=conn.cursor()
    global rowfrom
    global rowto
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
        cur.execute('SELECT MAX(rowid) FROM game3 WHERE "2"<=? AND "3"=? AND "4"=?',(day2,month2,year2))
        rowfrom=(cur.fetchone()[0])
        cur.execute('SELECT MIN(rowid) FROM game3 WHERE "2">=? AND "3"=? AND "4"=?',(day1,month1,year1))
        rowto=(cur.fetchone()[0])-rowfrom
        cur.execute('SELECT * FROM game3 LIMIT ? OFFSET ?', (rowto, rowfrom))
    elif base == 4:
        pass
    rows=cur.fetchall()
    conn.close()
    return rows

#Funkcja searchall dla checkboxa ściągająca dane z całej bazy danych. .
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

def dfdb(var):
    global df
    if var == 1 :
        df = pandas.read_sql_query(
            sql=('SELECT * FROM game1'),
            con=sqlite3.connect("Lotto.db"), coerce_float=False, parse_dates=None, chunksize=None)
    elif var == 2 :
        df = pandas.read_sql_query(
            sql=('SELECT * FROM game2'),
            con=sqlite3.connect("Lotto.db"), coerce_float=False, parse_dates=None, chunksize=None)
    elif var == 3 :
        df = pandas.read_sql_query(
            sql=('SELECT * FROM game3'),
            con=sqlite3.connect("Lotto.db"), coerce_float=False, parse_dates=None, chunksize=None)
    elif var == 4 :
        df = pandas.read_sql_query(
            sql=('SELECT * FROM game1 LIMIT ? OFFSET ?'),
            con=sqlite3.connect("Lotto.db"), coerce_float=False, params=[rowto, rowfrom], parse_dates=None, chunksize=None)
    elif var == 5 :
        df = pandas.read_sql_query(
            sql=('SELECT * FROM game2 LIMIT ? OFFSET ?'),
            con=sqlite3.connect("Lotto.db"), coerce_float=False, params=[rowto, rowfrom], parse_dates=None, chunksize=None)
    elif var == 6 :
        df = pandas.read_sql_query(
            sql=('SELECT * FROM game3 LIMIT ? OFFSET ?'),
            con=sqlite3.connect("Lotto.db"), coerce_float=False, params=[rowto, rowfrom], parse_dates=None, chunksize=None)
    else:
        pass

def enumerators(base,value,var1,var2):
    dfdb(base)
    df1=df.drop(df.columns[0:3],1)
    df2 = df1.apply(pandas.value_counts).fillna(0);
    df2.loc[:,'total'] = df2.sum(axis=1)
    df3=df2
    nplus = df3.sort_values(['total'], ascending=[False])[:1].index.values;
    nminus = df3.sort_values(['total'], ascending=[False])[-1:].index.values;
    nums = df3.sort_values(['total'], ascending=[False])[:int(value)].index.values;
    if var1 == 1 and var2 == 1 :
        yield "Max: " + str(nplus) + "  Min: " + str(nminus)
        yield "Od najczęstszej: " + str(nums)
    elif var1 == 1 and var2 == 0 :
        yield "Max: " + str(nplus) + "  Min: " + str(nminus)
    elif var1 == 0 and var2 == 1 :
        yield "Od najczęstszej: " + str(nums)
    else:
        pass

def makedf(base,var1,var2):
    dfdb(base)
    global df1
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
