# </> KNN - K NEAREST NEIGHBORS (K VIZINHOS MAIS PRÓXIMOS)
O K-Nearest Neighbors (KNN) é um algoritmo utilizado para análise de padrões em dados, tanto lineares quanto não lineares (em alguns casos). Ao desenvolver um sistema de previsão, é importante que o modelo apresente bom desempenho em dados novos, o que indica uma capacidade de generalização eficaz. Essa capacidade é crucial para a qualidade preditiva do modelo e o aprendizado de máquina se divide principalmente em dois tipos de abordagem:

## Aprendizado Baseado em Instância vs. Aprendizado Baseado em Modelo

### Aprendizado Baseado em Instância
Esse tipo de aprendizado pode ser entendido como um aprendizado de “memorização” ou aprendizado baseado em exemplos. Nele, a previsão é baseada em uma medida de similaridade entre os dados de entrada e o conjunto de dados já observado, ao invés de um modelo geral que descreva as relações subjacentes. 

Por exemplo:
- **Detecção de Fraude em Compras:** Um sistema pode identificar ações suspeitas comparando o número de tentativas de compra em um curto período com o comportamento usual do usuário, ou ainda comparando essas tentativas com padrões conhecidos de fraude.
- **Sistema de Detecção de Spam:** Um sistema de detecção de spam pode identificar e-mails suspeitos ao comparar a frequência de palavras específicas ou a estrutura das frases com padrões conhecidos de mensagens de spam.

Essa abordagem de aprendizado por instância é adequada para problemas em que é mais fácil prever com base na proximidade entre instâncias conhecidas (como KNN), em vez de uma relação matemática formal entre variáveis.

### Aprendizado Baseado em Modelo
No aprendizado baseado em modelo, o foco é entender e modelar a relação entre as entradas e as saídas esperadas. Essa abordagem utiliza algoritmos para construir um modelo generalizável que descreve o padrão ou a estrutura dos dados. A intenção é que o modelo faça previsões confiáveis para dados novos.

Exemplo:
- **Regressão Linear:** No [primeiro tópico](https://github.com/well1ngt0nso/APRENDIZADO_DE_MAQUINA/tree/main/1-REGRESSAO_LINEAR#regress%C3%A3o-linear), usamos um modelo de regressão linear para capturar a relação entre a tensão (V) e a corrente (A) em um componente. Observamos as amostras e inferimos que uma equação linear representaria bem essa relação. Com base nisso, desenvolvemos uma fórmula que melhor descrevesse essa relação, permitindo ao modelo prever a corrente para novos valores de tensão com precisão. Mais especificamente encontramos os coeficientes para adequação na formula de um sistema linear, enquanto na outra abordagem um modelo da biblioteca *sklearn*.

Os modelos baseados em instância, como o KNN, podem ser muito eficazes em problemas onde os dados são variados e dependem muito do contexto imediato (ou da proximidade com outros pontos de dados). Por outro lado, modelos baseados em aprendizado, como a regressão linear, são mais adequados para cenários onde há uma relação previsível e contínua entre variáveis.

> Em resumo, enquanto o aprendizado baseado em instância (como KNN) se apoia em comparações diretas com dados observados, o aprendizado baseado em modelo (como regressão) busca uma equação ou estrutura subjacente que permita capturar a relação entre entradas e saídas.

## DESENVOLVENDO UM MODELO KNN, OU SEJA, BASEADO EM INSTÂNCIA

Iremos fazer isso de duas formas:

1. Utilizando a biblioteca `sklearn`
2. Modelando matematicamente em Python
   
### Utilizando a biblioteca

No primeiro caso, vamos basicamente mudar uma única linha do exemplo já desenvolvido (Regressão Linear).

```python
import matplotlib.pyplot as plt
import numpy as np
import sklearn.neighbors

model = sklearn.neighbors.KNeighborsRegressor(n_neighbors=7  # Criando modelo onde recebe como argumento o número de vizinhos mais próximos (n_neighbors); nesse caso, decidi por 7
x = x.reshape(-1,1)  # Ajustando x para o formato esperado pelo modelo (de (84,) para (84,1))
y = y.reshape(-1,1)  # Ajustando y para o formato esperado pelo modelo

model.fit(x, y)  # Treinando o modelo com o conjunto de dados já tratado

print(model.predict([[2], [4]]))  # Prevê a saída para os valores de entrada 2 e 4
```
Neste exemplo:

- **n_neighbors=4**: Este parâmetro determina o número de vizinhos mais próximos considerados para realizar uma previsão. No KNN, o valor de k (ou n_neighbors) influencia o nível de detalhamento ou suavidade do modelo. Um valor menor (por exemplo, k=1) permite que o modelo capture mais detalhes e peculiaridades dos dados, enquanto um valor maior de k suaviza a previsão, considerando mais vizinhos na média.

- **Formatando x e y**: O uso de reshape(-1,1) transforma os vetores x e y em matrizes de uma coluna, um formato exigido pelo KNeighborsRegressor da biblioteca sklearn. Sem essa estrutura, o modelo não consegue processar os dados corretamente. reshape(-1, 1) indica ao Python para manter o número de linhas conforme necessário (-1 faz o ajuste automático) e definir uma única coluna para a matriz, resultando em um array 2D do tipo (n, 1). Isso ocorre porque a função espera que cada linha seja uma instância e cada coluna uma característica (feature).

Esse método direto, utilizando *sklearn*, facilita o processo de criação, treinamento e previsão com o modelo KNN em apenas algumas linhas de código. A simplicidade deste processo permite a rápida adaptação e uso para explorar o comportamento de novos dados, especialmente em problemas onde uma relação perceptível entre variáveis não é clara, mas onde há um padrão de proximidade ou similaridade entre os dados.

#### Resultado: 

 <p align="center">
  <img src="PLOTS/comp.svg" width="50%" />
</p>


O valor de \( n \) foi definido exclusivamente de forma empírica. Observemos que não existe uma fórmula que determine a melhor estrutura a ser utilizada no modelo ou qual o melhor modelo em si. Embora exista um caminho mais eficaz para chegar a conclusões, ao falarmos sobre parâmetros, a situação se torna mais complexa. Na maioria dos casos, a melhor abordagem é testar diferentes valores ou basear-se em conhecimento empírico.

Neste exemplo, seria interessante testar uma variedade de valores de \( n \) e analisar qual proporciona os melhores resultados.

 <p align="center">
  <img src="PLOTS/n_neighbors.svg" width="50%" />
</p>



Essa imagem serve como um lembrete de algumas observações e decisões tomadas no processo de modelagem:

1. **Objetivo**: Nosso principal objetivo era encontrar o melhor valor para a resistência \( R \), que representa o coeficiente angular da reta.
2. **Relação Linear**: Observamos que o sistema segue uma relação linear entre as variáveis, o que facilitou a modelagem.
3. **Previsão de Valores**: A partir dessa relação, buscamos prever valores da variável \( A \).

Apesar de ser uma relação linear, os dados possuem certo ruído, o que os afasta de uma reta perfeita. Em teoria, quanto melhores as condições, mais os dados se aproximam da relação linear ideal. Ao modelar o sistema para capturar a realidade dos dados, experimentamos diferentes valores de \( n \) (o número de vizinhos no modelo KNN). Com \( n = 1 \), o modelo se ajusta fortemente aos dados, enquanto com \( n = 7 \) observamos uma suavização que se aproxima mais das condições teóricas.

É importante ressaltar que o valor ideal de \( n \) não segue uma regra rígida. Tanto valores menores quanto maiores para \( n \) podem afetar a qualidade do modelo de formas diferentes. Características como o tamanho do conjunto de dados, a qualidade e quantidade de variáveis, e o nível de ruído influenciam essa escolha.

Uma abordagem extrema seria definir \( n \) igual ao número total de amostras. Nesse caso, o modelo se ajusta tanto aos dados que gera uma linha quase reta, indicando uma suavização excessiva e uma perda da capacidade de identificar a complexidade e os padrões nos dados.

Em resumo, a escolha de \( n \) requer experimentação e análise para alcançar um modelo equilibrado que capture bem os padrões sem se perder no ruído.


### Utilizando um algorítmo baseado na ideia matemática 
