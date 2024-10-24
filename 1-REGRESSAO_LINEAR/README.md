## REGRESSÃO LINEAR

Acho que uma bom tema para iniciar é Regressão Linear, quando comecei no mundo da programação uma das coisas que mais achava interessante eram a manipulação e geeração de gráficos e logo após um tempo as famosas RNA's, e se tem uma coisa que não se pode faltar quando agente fala disso são os gráficos... Mas vamos lá, Nesse poster trago a implementação de um algorítmo fr regressão, um programado apartir de uma fórmula (minimos) e outro apartir da bivliotrca skelearn (skelear.linear_model.LinearRegression();

Para leigos:

A regressão linear é uma ferreamentaque busca modelar a relação entre um conjunto de dados, em outras palavreas ela busca apróximar "funcionamento" de um conjunto de dados com objetivo de prever novos valores. Na matemática voçê já viu falar na equação do 1° grau **y = ax + b**,

### O problema: 

# Problema do Resistor de Grafite

Vamos supor que você se deparou com o seguinte problema: 

Você estava em seu laboratório e estava trabalhando em um resistor feito de grafite de lápis. Para saber sua resistência e incluir essa informação em um artigo, você aplicou um valor de tensão **V** sobre ele e mediu a corrente, utilizando a Lei de Ohm.

**R=V/I**

Após a primeira medição, você chegou a um valor de 100Ω (ohms). Duvidando do resultado, você testou outro valor e obteve 80Ω. Ao realizar várias medições, percebeu que os valores apresentavam leves variações.

Nesse ponto, você quer um valor mais confiável para descrever seu resistor. Uma alternativa é somar todas as observações e calcular a média.
Como você gosta de desafios partiu para a segunda opção:

1. Você fez várias mediçoes:
2. Plotou Todas em um gráfico de corrente por tensão

   
![GRÁFICO DE DISPERSÃO](PLOTS/dispersao.svg)

A partir deste momento, você já consegue observar o comportamento linear entre **V** e **I**, como é esperado. Basta calcular a reta que melhor aproxima esse conjunto de pontos, algo no formato **y = ax + b**. No nosso caso, isso se traduz em **V = RI**, onde **R = a** (coeficiente angular).

A primeira forma que vamos utilizar é por meio de métodos analíticos:

### MÉTODO 1: MÉTODO DOS MÍNIMOS QUADRÁTICOS

Um sistema linear simples no formato **y = ax + b** consiste em dois coeficientes:

- **Coeficiente Angular (a)**: Representa a inclinação da reta em relação a **x** ou a variação de **y** em função de **x**.
- **Coeficiente Linear (b)**: Indica onde a reta cruza o eixo **y** ou o valor de **y** quando **x = 0**.

Com esses dois coeficientes, podemos descrever qualquer reta. O **Método dos Mínimos Quadráticos** é uma técnica que, quando aplicada a um conjunto de pontos, encontra os melhores valores dos coeficientes **a** e **b**. Em outras palavras, esse método determina os valores que melhor descrevem o comportamento do conjunto de pontos por meio de uma reta.

Implementei isso em python e plotei os resultados: 

![regresão mínimos quadráticos](PLOTS/metodos_mt_comp.svg)

Aqui a comparação entre o modelo analítico (MMQT)  e  model.linear_model.LinearRegression(), fica praticaamente inperceptível a diferença:

![equação método dos mínimos quadráticos](PLOTS/metodos_predict_comp.svg)

Aqui podemos ver melhor o erro, veja que é x10^(-15)

![equação método dos mínimos quadráticos](PLOTS/erro.svg)


Todo o algorítmo se enontra aqui com todos os detalhes:

 

