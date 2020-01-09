import matplotlib.pyplot as plt 

movies =  ["Annie Hall","Ben-Hur","Casablanca","Gandhi","West Side Story"]
num_oscars = [5,11,3,8,10]

#barras possuem o tamanho padrão de 0.8, então adcionaremos 0.1 `as cordenadas a esquerda para que cada barra seja centralizada
xs = [i +0.1 for i, _ in enumerate(movies)]

#as barras do grafico com as coordenadas x a esquerda [xs], alturas[num_oscars]
plt.bar(xs, num_oscars)

plt.ylabel("# de Premiações")
plt.title("Meus filmes Favoritos")

#nomeia o eixo x com nomes de filmes na barra central
plt.xticks([i + 0.5 for i,_ in enumerate(movies)],movies)

plt.show()
