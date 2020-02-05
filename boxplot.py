import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("manchas.csv")
plt.style.use('fast')

x = dados.Ano
y = dados.manchas

plt.boxplot(x, patch_artist = True)
plt.title('Taxa de manchas solares em Wolfer')

#plt.show()#
plt.savefig("boxplot.jpg")
