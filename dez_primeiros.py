import pandas as pd
import matplotlib.pyplot as plt

sxt = pd.read_csv("manchas.csv")
sxt = sxt.head(10)
plt.style.use('dark_background')

x = sxt.Ano
y = sxt.manchas


plt.plot(x,y, marker = '_')
plt.title('Taxa de manchas solares em Wolfer')
plt.xlabel('ano')
plt.ylabel('mancha')
plt.grid(True, linewidth=0.3)
#plt.show()#
plt.savefig("dez_primeiros.jpg")
