# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt #biblioteca gráfica
import numpy as np #biblioteca matemática para traabalhar com arrays e matrizes

"""##DECLARAÇÃO DAS PRINCIPAIS VARIÁVEIS

Fala, galera, esse é o primeiro poster da página e espero que seja o primeiro de muitos sobre Inteligência Artificial, Eletrônica e muitos outros temas...

O objetivo em si é desenvolver redes Neurais e em alguns casos implementar isso em conjunto com circuitos eletrônicos (Esp, Arduino, Ci's...)

Geralmente aqui irei postar os resultados, mas em alguns casos algums partes do código (a documentação toda irei deixar no GitHub)

Let's Go!!!

Título: Regressão Linear

Acho que uma bom tema para iniciar é Regressão Linear, quando comecei no mundo da programação uma das coisas que mais achava interessante eram a manipulação e geeração de gráficos e logo após um tempo as famosas RNA's, e se tem uma coisa que não se pode faltar quando agente fala disso são os gráficos... Mas vamos lá, Nesse poster trago a implementação de um algorítmo fr regressão, um programado apartir de uma fórmula (minimos) e outro apartir da bivliotrca skelearn (skelear.linear_model.LinearRegression();

Para leigos:

A regressão linear é uma ferreamentaque busca modelar a relação entre um conjunto de dados, em outras palavreas ela busca apróximar "funcionamento" de um conjunto de dados com objetivo de prever novos valores. Na matemática voçê  já viu falar na qquação do 1° grau y = ax+b,
"""

n = 0 # quantidade de elementos/amostras/pares x e y
a = 0 # beta coeficiente linear
b = 0 # alfa coeficiente angular
e = 0 # erro y(real) - y(encontrado) (não utilizamos aqui)
x = 0 # variável dependente
y = 0 # resultado (variável independente)

"""##VALROES DE  TESTE"""

#VALORES DE EXEMPLO GERADOS PELO CHAT GPT PARA CÁLCULO
#CASO FOSSEM DADOS DE CSV, AQUI NÓS IRIAMOS FAZER A INSERÇÃO DOS MESMOS

x = [0.0, 0.120, 0.241, 0.361, 0.482, 0.602, 0.723, 0.843, 0.964, 1.084, 1.205, 1.325, 1.446, 1.566, 1.687,
1.807, 1.928, 2.048, 2.169, 2.289, 2.410, 2.530, 2.651, 2.771, 2.892, 3.012, 3.133, 3.253, 3.374,
3.494, 3.615, 3.735, 3.856, 3.976, 4.097, 4.217, 4.338, 4.458, 4.579, 4.699, 4.820, 4.940, 5.061,
5.181, 5.302, 5.422, 5.543, 5.663, 5.784, 5.904, 6.025, 6.145, 6.266, 6.386, 6.507, 6.627, 6.748,
6.868, 6.989, 7.109, 7.230, 7.350, 7.471, 7.591, 7.712, 7.832, 7.953, 8.073, 8.194, 8.314, 8.435,
8.555, 8.676, 8.796, 8.917, 9.037, 9.158, 9.278, 9.399, 9.519, 9.640, 9.760, 9.881, 10.0]


y = [3.50, 3.10, 4.13, 5.25, 3.73, 3.97, 6.02, 5.45, 4.46, 5.71, 4.95, 5.18, 6.13, 4.22, 4.65,
6.05, 5.84, 7.41, 6.43, 6.17, 9.28, 7.83, 8.37, 7.12, 8.24, 9.14, 8.11, 9.88, 9.15, 9.70,
9.63, 12.32, 10.70, 9.89, 12.02, 10.21, 11.88, 9.96, 10.83, 12.59, 13.38, 13.05, 13.00, 13.06,
12.12, 13.12, 13.62, 15.38, 14.91, 13.04, 15.37, 14.90, 14.85, 16.38, 17.04, 17.18, 15.65,
16.43, 17.31, 18.19, 16.98, 17.51, 16.83, 16.98, 19.23, 20.02, 18.83, 20.15, 19.75, 18.98,
20.23, 21.65, 20.31, 22.16, 18.21, 21.89, 21.40, 21.26, 21.89, 20.05, 22.06, 22.88, 24.24, 22.48]

"""##PLOTAGEM DOS DADOS"""

#PRIMEIRO CONTATO COM OS MESMOS DE FORMA GRÁFICA
#FORMA DE ENCONTRAR POSSÍVEIS ERROS, OUTLIERS

x = np.array(x)
y = np.array(y)
plt.figure()
plt.plot(x, y, '.', color = 'black', ls ='none')
plt.xlabel('Tensão (V)')
plt.ylabel('Corrente (A)')
plt.title( 'Gráfico de dispersão Fig.1')
plt.savefig('disperção.svg', format='svg',  bbox_inches='tight')
plt.show()

"""##DESEMVOLVENDO A LÓGICA (MÉTODO DOS MÍNIMOS QUADRÁTICOS)"""

# y = ax + b
# b = ( n * soma(xi*yi) - soma(xi)*soma(yi)) / (n * soma(xi²) - soma(xi)²)
#x.shape #84 (quantidade de elementos)

n = x.shape[0]
xy = x * y
sum_xy = sum(xy)
sum_x = sum(x)
sum_y = sum(y)
x_qdt = x * x

b = ( n * sum_xy - sum_x*sum_y ) /  (( n *sum(x_qdt)) - ( sum_x * sum_x ))
print("COEFICIENT ANGULAR:",  b)

def func(x, a, b):
  return x*b + a

# a = media(y) - b*media(x)
a =  (sum_y/n) - (b*(sum_x/n))
print("COEFICIENT LINEAR:", a)

plt.figure()
plt.plot(x, func(x,a,b), color = 'black', label = 'RETA DE AJUSTE ')
plt.xlabel('CORRENTE (A)')
plt.ylabel('TENSÃO')
plt.title('Método dos Mínimos Quadráticos Fig.2')

plt.plot(x, y, '.', label = 'DADOS DE DISPERSÃO')
plt.text(5,10,'y = β1x + β0 + e')
plt.text(5,8.5,'β1 ≃ 2.019 e β0 ≃ 2.798')
plt.legend()
plt.savefig('metodos_mt_comp.svg', format='svg',  bbox_inches='tight')
plt.show()

print(func(2, a , b))

"""##TESTE UTILIZANDO A BIBLIOTECA DO SKLEARN"""

import matplotlib.pyplot as plt
import numpy as np
import sklearn.linear_model

model = sklearn.linear_model.LinearRegression() # Criando modelo Linear
x = x.reshape(-1,1) # x y são estão no formato (84,), .fit aceita matrizes
y = y.reshape(-1,1) # então crio uma de 1 coluna e a quantidade de linhas a função escolhe (-1)
model.fit(x,y) #treino o modelo no conjunto já tratado
x.shape

print(model.predict([[2], [4]])) #prevê a saída para dois valores

plt.figure()
plt.plot(x[:,], func(x[:,], a, b), color = "black", label = "mínimos quadráticos")
plt.plot(x[:,], model.predict(x[:,]), color = "blue", label = "model.predict")
plt.xlabel("Tensão (V)")
plt.ylabel("Corrente (A) x 10 ^ -15")
plt.title("Comparação entre a previsão dos modelos Fig.3")
plt.legend()
plt.savefig('metodos_predict_comp.svg', format='svg',  bbox_inches='tight')
plt.show()

"""##ERRO"""

plt.figure()
plt.plot(x[:,], (func(x[:,], a, b) - model.predict(x))*1000000000000000,  color = 'black', label = 'model_predict - mínimos_quadráticos')
plt.ylabel("Corrente (A) x 10^-15")
plt.xlabel("Tensão (V)")
plt.legend()
plt.title("Erro Fig.4")

plt.savefig("erro.svg", format = "svg", bbox_inches='tight' )
plt.show()
