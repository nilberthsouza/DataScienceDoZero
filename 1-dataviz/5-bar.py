import matplotlib.pyplot as plt

mentions = [500,505]
years = [2013,2014]

plt.bar([2012.6,2013.6],mentions,0.8)
plt.xticks(years)
plt.ylabel("# de vezes que ouvimos alguém dizer data science")

#se você não fizer isso, matplotlib nomeará o eixo x de 0.1

#e então adciona a +2.013e3 para fora do canto
plt.ticklabel_format(useOffset=False)

#engarnar o eixo y mostra apenas a parte acima de 500
plt.axis([2012.5,2014.5,499,506])
plt.title("Olhe o Grande Aumento")
plt.show()
