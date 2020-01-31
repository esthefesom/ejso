import pandas as pd
import matplotlib.pyplot as plt

sxt = pd.read_csv("manchas.csv")
sxt = sxt.tail(10)
plt.style.use('Solarize_Light2')

x = sxt.Ano
y = sxt.manchas


plt.plot(x,y, marker = '_')
plt.title('Taxa de manchas solares em Wolfer')
plt.xlabel('ano')
plt.ylabel('mancha')
plt.grid(True, linewidth=0.3)
#plt.show()#
plt.savefig("10ultimos.jpg")
