import matplotlib.pyplot as plt

grades=[83,95,91,87,70,0,85,82,100,67,73,77,0]
decile = lambda grade: grade // 10*10
histogram = Counter(decile(grade) for grade in grades)

plt.bar([x -4 for x in histogram.keys()], #move cada barra para a esquerda em 4
        histogram.values(),               #da para cada barra sua altura correta
        8)                               #da pra cada barra a largura de 8

plt.axis([-5,105,0,5]) #eixo x de -5 até 105, eixo y de 0 até 5

plt.xticks([10* i for i in range(11)])
plt.xlabel("Decil")
plt.ylabel("# de alunos")
plt.title("Distribuição das notas de testes 1")
plt.show()
