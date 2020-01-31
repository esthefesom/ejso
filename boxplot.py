import pandas as pd
import matplotlib.pyplot as plt

sxt = pd.read_csv("manchas.csv")
plt.style.use('fast')

x = sxt.Ano
y = sxt.manchas

plt.boxplot(x, patch_artist = True)
plt.title('Taxa de manchas solares em Wolfer')

#plt.show()#
plt.savefig("boxplot.jpg")
