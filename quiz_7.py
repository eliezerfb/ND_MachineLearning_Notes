###Quiz: Exemplo De Rede Em Camadas
###Em geral, juntamos unidades para formar redes em camadas. Isso será representado assim:

###[[nó, nó, nó],    # camada de entrada
###[nó, nó],        # camada oculta
###[nó]]            # camada de saída
###Se tomarmos [1, 1, -5] e [3, -4, 2] como pesos da camada oculta e [2, -1] como pesos da camada de saída, qual será o valor de saída desta rede para o input [1, 2, -3]?

import numpy as np

hidden_weights = np.array([[1,1,-5],[3,-4,2]])
output_weights = np.array([2,-1])
inputs = np.array([1,2,3])

hidden_thetas = []

for i in range(0,len(hidden_weights)):
    hidden_thetas.append(np.dot(inputs,hidden_weights[i].T))

print(hidden_thetas)

output = np.dot(hidden_thetas,output_weights)
print(output)
