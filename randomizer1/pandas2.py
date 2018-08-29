#Ten kod wyciąga najczęstszą i najrzadszą liczbę bez względu na źródło danych w mbnet.
import pandas

df=pandas.read_csv('http://www.mbnet.com.pl/dl.txt',header =None, index_col=0, sep='[., ]', engine ='python')
df1=df.drop(df.columns[0:4],1)
df2 = df1.apply(pandas.value_counts).fillna(0);
df2.loc[:,'total'] = df2.sum(axis=1)
df3=df2
nplus = df3.sort_values(['total'], ascending=[False])[:1].index.values;
nminus = df3.sort_values(['total'], ascending=[False])[-1:].index.values;
print(nplus)
print(nminus)
#poniżej output do zadania 1: najwyższa i najniższa liczba.
#print("najczęstsza liczba: "); int(nplus)
#print("narzadsza liczba: "); int(nminus)
#Ten kawałek jest do zadania 2: Bokeh plot.
#[34],[48]
