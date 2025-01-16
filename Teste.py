import matplotlib.pyplot as plt

# Dados simples para o gráfico
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Criar o gráfico
plt.plot(x, y, label='Crescimento')

# Adicionar título e rótulos
plt.title('Gráfico de Crescimento')
plt.xlabel('X')
plt.ylabel('Y')

# Exibir legenda
plt.legend()

# Mostrar o gráfico
plt.show()
