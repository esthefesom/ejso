import pandas as varpandas
import matplotlib.pyplot as varplot

sxt = varpandas.read_csv("manchas.csv")
sxt = sxt.tail(10)
varplot.style.use('Solarize_Light2')

x = sxt.Ano
y = sxt.manchas

varplot.plot(x,y, marker = '_')
varplot.title('Taxa de manchas solares em Wolfer')
varplot.xlabel('ano')
varplot.ylabel('mancha')
varplot.grid(True, linewidth=0.3)
#plt.show()#
varplot.savefig("dez_ultimos.jpg")
