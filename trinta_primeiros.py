import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("manchas.csv")
dados = dados.head(30)
plt.style.use('Solarize_Light2')

x = dados.Ano
y = dados.manchas

plt.plot(x,y, marker = '_', color = 'c')
plt.title('Taxa de manchas solares em Wolfer')
plt.xlabel('ano')
plt.ylabel('mancha')

#plt.show()#
plt.savefig("trinta_primeiros.jpg")
