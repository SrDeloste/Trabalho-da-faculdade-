# Importa os módulos math, numpy e matplotlib.pyplot
import math
import numpy as np
import matplotlib.pyplot as plt

# Define a constante pi com o valor de pi do módulo math
pi = math.pi

# Solicita ao usuário que insira os valores das variáveis
print('Valores pedidos')
L1 = int(input('Valor de L1: '))  # Solicita o valor de L1
L2 = int(input('Valor de L2: '))  # Solicita o valor de L2
xa = int(input('Valor de A no eixo x: '))  # Solicita o valor de xa
ya = int(input('Valor de A no eixo y: '))  # Solicita o valor de ya

# Calcula a distância d usando o teorema de Pitágoras
d = math.sqrt((xa**2) + (ya**2))

# Define uma função chamada 'conta' que realiza cálculos com base nas variáveis fornecidas
def conta(L1, L2, xa, ya, d):
    # Calcula os ângulos teta, alfa1, alfa2, beta e alfa usando fórmulas matemáticas
    teta = (180/pi) * (math.acos(-((L1**2) - (L2**2) - (d**2)) / (2 * L2 * d)))
    alfa1 = (180/pi) * (math.acos(-((L2**2) - (L1**2) - (d**2)) / (2 * L1 * d)))
    alfa2 = (180/pi) * (math.atan(ya / xa))
    beta = 180 - alfa1 - teta
    alfa = alfa1 + alfa2
    
    # Retorna os resultados como uma tupla (teta, alfa1, alfa2, beta, alfa)
    return teta, alfa1, alfa2, beta, alfa

# Chama a função 'conta' com os valores de entrada e atribui os resultados a variáveis em maiúsculas
T, A1, A2, B, A = conta(L1, L2, xa, ya, d)

# Cria arrays de valores de ângulo alfa e beta usando numpy
ALFA = np.linspace(xa, A)
BETA = np.linspace(xa, B)

# Verifica se os valores de A e B estão dentro das faixas permitidas
if ((A >= 0 and A <= 90) and (B >= 1 and B <= 359)):
    # Cria um gráfico de duas subplots
    plt.subplot(1, 2, 1)
    plt.xlabel('xa')
    plt.ylabel('alfa')
    plt.plot(ALFA)  # Plota o gráfico de alfa

    plt.subplot(1, 2, 2)
    plt.xlabel('xa')
    plt.ylabel('beta')
    plt.plot(BETA)  # Plota o gráfico de beta
    
    plt.show()  # Exibe o gráfico
