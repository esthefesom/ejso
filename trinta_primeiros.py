import pandas as varpandas
import matplotlib.pyplot as varplot

sxt = varpandas.read_csv("manchas.csv")
sxt = sxt.head(30)
varplot.style.use('Solarize_Light2')

x = sxt.Ano
y = sxt.manchas

varplot.plot(x,y, marker = '_', color = 'c')
varplot.title('Taxa de manchas solares em Wolfer')
varplot.xlabel('ano')
varplot.ylabel('mancha')

#plt.show()#
varplot.savefig("trinta_primeiros.jpg")
