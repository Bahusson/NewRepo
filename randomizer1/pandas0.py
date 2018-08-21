import pandas
#formatuje poprawnie dane z mbnet - kod bazowy.
dfa=pandas.read_csv('http://www.mbnet.com.pl/ml.txt',header =None, index_col=0, sep='[., ]', engine ='python')
print(dfa)
