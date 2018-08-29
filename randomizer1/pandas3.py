#Ten kod ma w założeniu podawać X najczęściej padających liczb.
#Zrób try/except na wypadek jakby ktoś wpisał za mało lub za dużo. W takim wypadku niech mu wyskoczy error message.
import pandas

inp=input("Ile chcesz liczb?:" )

df=pandas.read_csv('http://www.mbnet.com.pl/dl.txt',header =None, index_col=0, sep='[., ]', engine ='python')
df1=df.drop(df.columns[0:4],1)
df2 = df1.apply(pandas.value_counts).fillna(0);
df2.loc[:,'total'] = df2.sum(axis=1)
df3=df2
#print(df3.sort_values(['total']))
nums = df3.sort_values(['total'], ascending=[False])[:int(inp)].index.values;
print(nums)
