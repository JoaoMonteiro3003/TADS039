import matplotlib.pyplot as plt

# Dados de exemplo
dados = [7, 8, 5, 6, 7, 8, 6, 5, 7, 6, 8, 9, 7, 6, 5]

# Criando o histograma
plt.hist(dados, bins=5, color='skyblue', edgecolor='black')

# Adicionando títulos e rótulos
plt.title("Histograma de Frequência")
plt.xlabel("Valores")
plt.ylabel("Frequência")

# Exibindo o gráfico
plt.show()