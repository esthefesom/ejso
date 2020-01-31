import pandas as varpandas
import matplotlib.pyplot as varplot

sxt = varpandas.read_csv("manchas.csv")
varplot.style.use('fast')

x = sxt.Ano
y = sxt.manchas

varplot.boxplot(x, patch_artist = True)
varplot.title('Taxa de manchas solares em Wolfer')

#plt.show()#
varplot.savefig("boxplot.jpg")
