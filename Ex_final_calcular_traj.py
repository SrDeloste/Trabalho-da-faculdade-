import math

# Define a constante pi com o valor de pi do módulo math
pi = math.pi

# Solicita ao usuário que insira os valores das variáveis
print('Primeiro digite os valores')
L1 = int(input('Valor de L1:'))  # Solicita o valor de L1
L2 = int(input('Valor de L2:'))  # Solicita o valor de L2
alfa = int(input('Valor de alfa:'))  # Solicita o valor de alfa
beta = int(input('Valor de beta:'))  # Solicita o valor de beta

# Define uma função chamada 'conta' que realiza os cálculos
def conta(L1, L2, alfa, beta):
    # Calcula as coordenadas xb e yb usando fórmulas trigonométricas
    xb = (math.cos((alfa * pi) / 180)) * L1
    yb = (math.sin((alfa * pi) / 180)) * L1
    
    # Calcula beta1 e beta2 com base nos ângulos fornecidos
    beta1 = 90 - alfa
    beta2 = beta - beta1 - 90
    
    # Retorna os resultados como uma tupla (xb, yb, beta1, beta2)
    return xb, yb, beta1, beta2

# Chama a função 'conta' com os valores de entrada e atribui os resultados a variáveis em maiúsculas
XB, YB, BETA1, BETA2, = conta(L1, L2, alfa, beta)

# Condicional para verificar se os valores de alfa e beta estão dentro das faixas permitidas
if ((alfa >= 0 and alfa <= 90) and (beta >= 1 and beta <= 359)):
    print('O valor das variáveis é:')
    print('Valor de Xb: {0:.2f}'.format(XB))
    print('Valor de Yb: {0:.2f}'.format(YB))
    print('Valor de beta1: {0:.2f}'.format(BETA1))
    print('Valor de beta2: {0:.2f}'.format(BETA2))
else:
    print('Com os valores inseridos não será possível calcular as trajetórias, digite outros valores!')
