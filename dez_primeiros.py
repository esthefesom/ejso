import pandas as varpandas
import matplotlib.pyplot as varplot

sxt = varpandas.read_csv("manchas.csv")
sxt = sxt.head(10)
varplot.style.use('dark_background')

x = sxt.Ano
y = sxt.manchas


varplot.plot(x,y, marker = '_')
varplot.title('Taxa de manchas solares em Wolfer')
varplot.xlabel('ano')
varplot.ylabel('mancha')
varplot.grid(True, linewidth=0.3)
#plt.show()#
varplot.savefig("dez_primeiros.jpg")
