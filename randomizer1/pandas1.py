#Ten kod rysuje graf bez względu na źródło danych w mbnet. Trzeba pod ten blok podpiąć też średnie wyników.
import pandas
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource

df = pandas.read_csv('http://www.mbnet.com.pl/ml.txt',header =None, index_col=0, sep='[., ]', engine ='python')
df1=df.drop(df.columns[0:2],1)
df4=df1.T
df5=df4.mean().round(0).value_counts()


source = ColumnDataSource(
    data=dict(
        Means=df5.index,
        Freqs=df5.values
        ))

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
