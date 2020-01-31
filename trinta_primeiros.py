import pandas as pd
import matplotlib.pyplot as plt

sxt = pd.read_csv("manchas.csv")
sxt = sxt.head(30)
plt.style.use('Solarize_Light2')

x = sxt.Ano
y = sxt.manchas

plt.plot(x,y, marker = '_', color = 'c')
plt.title('Taxa de manchas solares em Wolfer')
plt.xlabel('ano')
plt.ylabel('mancha')

#plt.show()#
plt.savefig("30primeiros.jpg")
