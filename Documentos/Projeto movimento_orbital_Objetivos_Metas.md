# 🌌 ENTRE KEPLER E NEWTON: ANÁLISE COMPUTACIONAL DO MOVIMENTO DOS PLANETAS

> **Projeto para a 19ª MiT --- Mostra de Ideias Transformadoras e
> Iniciação Científico-Tecnológica**\
> **Área principal:** Computação, com aplicação em Física e Matemática\
> **Linguagem principal:** Python\
> **Status:** Projeto em desenvolvimento --- etapa inicial

------------------------------------------------------------------------

# 📑 Sumário

1.  [Visão geral do projeto](#-visão-geral-do-projeto)
2.  [Ideia central](#-ideia-central)
3.  [Problema de pesquisa](#-problema-de-pesquisa)
4.  [Hipótese](#-hipótese)
5.  [Objetivos](#-objetivos)
6.  [O que o projeto NÃO pretende
    fazer](#-o-que-o-projeto-não-pretende-fazer)
7.  [Fundamentação teórica](#-fundamentação-teórica)
    -   [7.1 Leis de Kepler](#71-leis-de-kepler)
    -   [7.2 Gravitação Universal de
        Newton](#72-gravitação-universal-de-newton)
    -   [7.3 Da força à aceleração](#73-da-força-à-aceleração)
    -   [7.4 Equações diferenciais do
        movimento](#74-equações-diferenciais-do-movimento)
    -   [7.5 Condições iniciais](#75-condições-iniciais)
8.  [Métodos numéricos](#-métodos-numéricos)
    -   [8.1 Por que precisamos de métodos
        numéricos?](#81-por-que-precisamos-de-métodos-numéricos)
    -   [8.2 Método de Euler](#82-método-de-euler)
    -   [8.3 Método de Verlet](#83-método-de-verlet)
    -   [8.4 Possível expansão: RK4](#84-possível-expansão-rk4)
9.  [Grandezas que serão analisadas](#-grandezas-que-serão-analisadas)
10. [Experimentos](#-experimentos)
11. [Metodologia completa](#-metodologia-completa)
12. [Arquitetura do software](#-arquitetura-do-software)
13. [Tecnologias e bibliotecas](#-tecnologias-e-bibliotecas)
14. [Estrutura de pastas](#-estrutura-de-pastas)
15. [Plano de desenvolvimento do
    código](#-plano-de-desenvolvimento-do-código)
16. [Dados dos planetas](#-dados-dos-planetas)
17. [Unidades e escalas](#-unidades-e-escalas)
18. [Validação dos resultados](#-validação-dos-resultados)
19. [Análise dos resultados](#-análise-dos-resultados)
20. [Gráficos e tabelas](#-gráficos-e-tabelas)
21. [Demonstração na MiT](#-demonstração-na-mit)
22. [Cronograma](#-cronograma)
23. [Entregáveis](#-entregáveis)
24. [Possíveis dificuldades e
    soluções](#-possíveis-dificuldades-e-soluções)
25. [Critérios para considerar o projeto
    concluído](#-critérios-para-considerar-o-projeto-concluído)
26. [Referências](#-referências)
27. [Checklist geral](#-checklist-geral)

------------------------------------------------------------------------

# 🔭 Visão geral do projeto

O projeto investiga como diferentes formas de representar e calcular o
movimento de corpos sob atração gravitacional influenciam o resultado de
uma simulação computacional.

A ideia parte de um problema conhecido da Física:

> **Dadas a massa de um corpo central, as condições iniciais de outro
> corpo e a lei da gravitação, como podemos calcular sua trajetória ao
> longo do tempo usando um computador?**

O projeto utilizará as **Leis de Kepler** como referência para
compreender o movimento planetário e a **Lei da Gravitação Universal de
Newton** como base física para a modelagem.

A Computação será utilizada como ferramenta de investigação. O objetivo
não é simplesmente criar uma animação do Sistema Solar, mas construir um
pequeno **laboratório computacional** capaz de:

-   calcular trajetórias;
-   comparar métodos numéricos;
-   medir erros;
-   analisar estabilidade;
-   observar conservação de energia;
-   medir tempo de execução;
-   testar diferentes condições iniciais;
-   comparar modelos com diferentes níveis de complexidade.

A estrutura científica do projeto será:

``` text
PROBLEMA FÍSICO
      ↓
MODELO MATEMÁTICO
      ↓
EQUAÇÕES DO MOVIMENTO
      ↓
MÉTODO NUMÉRICO
      ↓
IMPLEMENTAÇÃO EM PYTHON
      ↓
EXPERIMENTOS
      ↓
DADOS
      ↓
GRÁFICOS E TABELAS
      ↓
ANÁLISE
      ↓
CONCLUSÕES
```

------------------------------------------------------------------------

# 💡 Ideia central

O ponto mais importante do projeto é entender que **o software não é o
objeto científico principal**.

O programa será utilizado como instrumento para responder à pergunta de
pesquisa.

### Exemplo

Em vez de:

> "Vou fazer um programa que mostra a Terra girando ao redor do Sol."

A proposta científica é:

> "Vou investigar como diferentes métodos numéricos influenciam a
> precisão e a estabilidade da representação computacional de uma
> órbita."

Isso torna o trabalho mais adequado a uma mostra científica.

------------------------------------------------------------------------

# ❓ Problema de pesquisa

## Pergunta principal

> **Como a complexidade do modelo físico e o método numérico utilizado
> influenciam a precisão, a estabilidade e o custo computacional da
> simulação do movimento planetário?**

### Perguntas secundárias

1.  O método de Euler mantém uma órbita estável durante simulações
    longas?
2.  O método de Verlet apresenta comportamento diferente?
3.  Como o tamanho do passo de tempo (`dt`) influencia o erro?
4.  Como o erro se acumula ao longo da simulação?
5.  Como a conservação da energia pode ser utilizada para avaliar a
    qualidade de um método?
6.  Qual método apresenta melhor equilíbrio entre precisão e tempo de
    execução?
7.  O que acontece quando pequenas alterações são feitas nas condições
    iniciais?
8.  Como a inclusão de outros corpos modifica a trajetória simulada?
9.  Um modelo mais complexo necessariamente produz um resultado melhor
    em todas as situações?
10. Qual combinação de modelo e método é mais adequada para cada
    experimento?

------------------------------------------------------------------------

# 🧪 Hipótese

A hipótese inicial do projeto será:

> **Métodos numéricos diferentes apresentarão níveis diferentes de
> precisão e estabilidade, e métodos mais adequados à natureza do
> problema orbital deverão apresentar menor erro acumulado e melhor
> conservação das grandezas físicas, embora possam apresentar maior
> custo computacional.**

Essa hipótese **não deve ser tratada como resultado** antes dos
experimentos.

O correto é testar a hipótese e deixar os dados mostrarem o
comportamento observado.

------------------------------------------------------------------------

# 🎯 Objetivos

## Objetivo geral

Desenvolver uma ferramenta computacional em Python para estudar e
comparar a representação numérica do movimento planetário a partir de
modelos gravitacionais e diferentes métodos de integração.

## Objetivos específicos

-   estudar as Leis de Kepler;
-   estudar a Gravitação Universal de Newton;
-   transformar o modelo físico em equações computacionais;
-   implementar inicialmente o modelo Sol--Terra;
-   implementar o método de Euler;
-   implementar o método de Verlet;
-   futuramente implementar RK4, se necessário;
-   testar diferentes tamanhos de passo de tempo;
-   comparar trajetórias;
-   calcular erros;
-   analisar estabilidade orbital;
-   analisar conservação de energia;
-   medir tempo de execução;
-   testar diferentes condições iniciais;
-   ampliar gradualmente o modelo para mais corpos;
-   produzir gráficos e tabelas;
-   interpretar os resultados;
-   documentar todo o processo.

------------------------------------------------------------------------

# 🚫 O que o projeto NÃO pretende fazer

É importante deixar isso claro para evitar um problema comum em
trabalhos científicos.

O projeto **não pretende**:

-   descobrir novamente as Leis de Kepler;
-   provar que Newton estava correto;
-   criar um novo modelo físico;
-   substituir estudos astronômicos reais;
-   reproduzir com precisão absoluta o Sistema Solar;
-   criar um jogo;
-   fazer apenas uma animação;
-   apresentar uma calculadora de órbitas sem análise;
-   afirmar resultados antes da realização dos experimentos.

O projeto pretende **estudar computacionalmente a influência dos modelos
e métodos de cálculo sobre os resultados obtidos**.

------------------------------------------------------------------------

# 📚 Fundamentação teórica

# 7.1 Leis de Kepler

As Leis de Kepler descrevem características importantes do movimento dos
planetas.

## Primeira Lei --- Lei das Órbitas

Os planetas descrevem órbitas aproximadamente elípticas ao redor do Sol,
com o Sol localizado em um dos focos da elipse.

Uma elipse pode ser caracterizada pelo:

-   semi-eixo maior `a`;
-   semi-eixo menor `b`;
-   excentricidade `e`.

A excentricidade é dada por:


$$
e = \sqrt{1-\frac{b^2}{a^2}}
$$


Quanto mais próxima de zero, mais circular é a órbita.

------------------------------------------------------------------------

## Segunda Lei --- Lei das Áreas

A linha que liga o planeta ao Sol percorre áreas iguais em intervalos de
tempo iguais.

Isso significa que a velocidade orbital não é constante em uma órbita
elíptica.

O planeta:

-   move-se mais rapidamente quando está mais próximo do Sol;
-   move-se mais lentamente quando está mais distante.

A velocidade areolar pode ser expressa por:


$$
\frac{dA}{dt} = \text{constante}
$$


Essa propriedade é importante para verificar se a simulação está
reproduzindo um comportamento fisicamente coerente.

------------------------------------------------------------------------

## Terceira Lei --- Lei dos Períodos

Existe uma relação entre o período orbital e o tamanho da órbita.

Para um sistema dominado por uma massa central:


$$
T^2 \propto a^3
$$


Na forma associada à gravitação newtoniana:


$$
T^2 = \frac{4\pi^2}{GM}a^3
$$


onde:

-   `T` = período orbital;
-   `a` = semi-eixo maior;
-   `G` = constante gravitacional;
-   `M` = massa do corpo central.

Essa relação poderá ser utilizada como **referência de validação** da
simulação.

------------------------------------------------------------------------

# 7.2 Gravitação Universal de Newton

A Lei da Gravitação Universal descreve a atração gravitacional entre
dois corpos.


$$
F = G\frac{m_1m_2}{r^2}
$$


onde:

-   `F` = força gravitacional;
-   `G` = constante gravitacional;
-   `m₁` = massa do primeiro corpo;
-   `m₂` = massa do segundo corpo;
-   `r` = distância entre os centros dos corpos.

No caso de um planeta orbitando uma estrela, podemos considerar:

``` text
Sol → corpo central
Terra → corpo em movimento
```

------------------------------------------------------------------------

# 7.3 Da força à aceleração

Pela segunda Lei de Newton:


$$
\vec F = m\vec a
$$


Combinando essa relação com a gravitação, obtemos a aceleração do corpo:


$$
\vec a = -GM\frac{\vec r}{|\vec r|^3}
$$


Essa é uma das equações centrais do projeto.

Ela informa a direção e a intensidade da aceleração gravitacional.

------------------------------------------------------------------------

# 7.4 Equações diferenciais do movimento

O movimento pode ser representado por:


$$
\frac{d\vec r}{dt} = \vec v
$$


e


$$
\frac{d\vec v}{dt} = -GM\frac{\vec r}{|\vec r|^3}
$$


Assim, o computador precisa calcular repetidamente:

1.  posição;
2.  distância até o corpo central;
3.  aceleração;
4.  velocidade;
5.  nova posição.

Esse processo é realizado passo a passo.

------------------------------------------------------------------------

# 7.5 Condições iniciais

Para iniciar uma simulação precisamos informar:

-   posição inicial;
-   velocidade inicial;
-   massa do corpo;
-   massa do corpo central;
-   passo de tempo;
-   duração da simulação.

Exemplo simplificado para a Terra:

``` text
posição inicial:
x = 1 UA
y = 0

velocidade inicial:
vx = 0
vy ≈ 29,78 km/s
```

Esses valores serão refinados conforme os dados utilizados no
experimento.

------------------------------------------------------------------------

# 🔢 Métodos numéricos

# 8.1 Por que precisamos de métodos numéricos?

As equações do movimento podem ser resolvidas analiticamente em
determinadas condições, mas o projeto precisa investigar o comportamento
de uma solução calculada numericamente.

O computador não acompanha o movimento de forma contínua.

Ele trabalha com pequenos intervalos:

``` text
t0 → t1 → t2 → t3 → t4 → ...
```

O tamanho desse intervalo é o:


$$
\Delta t
$$


ou `dt` no programa.

Quanto menor o `dt`, maior tende a ser o número de cálculos necessários.

Isso cria uma relação importante:

``` text
passo pequeno
     ↓
mais cálculos
     ↓
maior custo computacional
```

enquanto:

``` text
passo grande
     ↓
menos cálculos
     ↓
maior possibilidade de erro numérico
```

Essa relação será uma das coisas investigadas.

------------------------------------------------------------------------

# 8.2 Método de Euler

O método de Euler é uma das formas mais simples de realizar integração
numérica.

A atualização da velocidade pode ser escrita como:


$$
\vec v\_{n+1} = \vec v_n +
\vec a_n\Delta t
$$


e a posição:


$$
\vec r\_{n+1} = \vec r_n +
\vec v_n\Delta t
$$


No código, a ideia é:

``` python
velocidade += aceleracao * dt
posicao += velocidade * dt
```

### Vantagens

-   simples;
-   fácil de implementar;
-   excelente para aprender integração numérica;
-   baixo custo por passo.

### Desvantagens

-   pode acumular erro;
-   pode apresentar problemas de estabilidade;
-   pode distorcer órbitas em simulações longas.

Por isso, Euler é muito interessante para comparação.

------------------------------------------------------------------------

# 8.3 Método de Verlet

O método de Verlet é bastante utilizado em problemas de dinâmica.

Uma forma básica da atualização da posição é:


$$
\vec r\_{n+1} = 2\vec r_n-\vec r\_{n-1}
+\vec a_n\Delta t^2
$$


Uma implementação mais completa também precisa tratar adequadamente a
velocidade e as condições iniciais.

O interesse do método no projeto está na comparação com Euler,
principalmente em:

-   estabilidade;
-   trajetória;
-   erro;
-   conservação de energia;
-   custo computacional.

------------------------------------------------------------------------

# 8.4 Possível expansão: RK4

O método de Runge-Kutta de quarta ordem (RK4) poderá ser implementado
como uma expansão do projeto.

Ele é mais complexo que Euler e exige mais avaliações da função a cada
passo.

A ideia será:

``` text
Euler
  ↓
Verlet
  ↓
RK4 (opcional)
```

**Importante:** RK4 não precisa estar na primeira versão. Primeiro
devemos garantir que Euler e Verlet estejam funcionando corretamente.

------------------------------------------------------------------------

# 📊 Grandezas que serão analisadas

O projeto não deve comparar apenas se a órbita "parece bonita".

Precisamos transformar o comportamento em dados mensuráveis.

## 1. Erro orbital

Quando houver um valor de referência:


$$
Erro(%) = \frac{|valor_{simulado}-valor_{referência}|}
{valor\_{referência}} \times100
$$


Exemplo:


$$
Erro_T(%) = \frac{|T_{simulado}-T_{referência}|}
{T\_{referência}} \times100
$$


------------------------------------------------------------------------

## 2. Período orbital

Tempo necessário para o planeta completar uma volta.

Pode ser comparado com o período de referência obtido pela relação de
Kepler ou por dados adotados no projeto.

------------------------------------------------------------------------

## 3. Distância ao corpo central

A distância será:


$$
r = \sqrt{x^2+y^2}
$$


Ela permite analisar se a órbita permanece estável.

------------------------------------------------------------------------

## 4. Energia mecânica

Para o problema simplificado de dois corpos, podemos analisar:


$$
E = \frac{1}{2}mv^2 - \frac{GMm}{r}
$$


A variação relativa da energia pode ser utilizada como indicador de
estabilidade numérica.

Uma medida possível:


$$
Erro_E(%) = \frac{|E(t)-E_0|} {|E_0|} \times100
$$


------------------------------------------------------------------------

## 5. Tempo de execução

O programa deverá registrar o tempo necessário para executar cada
experimento.

Assim será possível comparar:

``` text
Precisão
   ×
Custo computacional
```

------------------------------------------------------------------------

## 6. Número de passos

Se:


$$
N = \frac{t_{final}-t_{inicial}}{\Delta t}
$$


então diminuir `dt` aumenta o número de passos.

Essa grandeza ajuda a explicar o aumento do custo computacional.

------------------------------------------------------------------------

# 🧪 Experimentos

O projeto será desenvolvido de forma incremental.

------------------------------------------------------------------------

## Experimento 01 --- Sol + Terra com Euler

### Objetivo

Criar a primeira simulação funcional.

### Modelo

``` text
Sol + Terra
```

### Método

Euler.

### Saídas

-   trajetória;
-   posição;
-   velocidade;
-   distância ao Sol;
-   tempo de execução.

### Primeiro gráfico

``` text
x × y
```

O resultado esperado é uma trajetória orbital.

**Observação:** o formato exato deve ser obtido experimentalmente. Não
devemos afirmar antecipadamente que a órbita terá determinada
deformação.

------------------------------------------------------------------------

# Experimento 02 --- Influência do passo de tempo

Testar diferentes valores de `dt`.

Exemplo:

``` text
dt = 1 hora
dt = 6 horas
dt = 12 horas
dt = 24 horas
```

Os valores definitivos serão escolhidos após os primeiros testes.

### Analisar

-   erro;
-   estabilidade;
-   tempo de execução;
-   trajetória;
-   energia.

### Pergunta

> Como o tamanho do passo de tempo influencia a qualidade da simulação?

------------------------------------------------------------------------

# Experimento 03 --- Euler × Verlet

Executar exatamente o mesmo cenário usando:

``` text
Euler
Verlet
```

Manter iguais:

-   condições iniciais;
-   duração;
-   `dt`;
-   massas;
-   constantes.

Alterar somente o método.

### Comparar

  Métrica              Euler   Verlet
  ------------------ ------- --------
  Erro de período        ---      ---
  Erro de energia        ---      ---
  Tempo                  ---      ---
  Estabilidade           ---      ---
  Número de passos       ---      ---

Os valores serão preenchidos somente depois dos experimentos.

------------------------------------------------------------------------

# Experimento 04 --- Simulação de longo prazo

Aumentar o período simulado.

Exemplo:

``` text
1 ano
5 anos
10 anos
50 anos
```

Os valores finais dependerão do custo computacional.

### Objetivo

Observar se pequenos erros acumulados tornam-se significativos ao longo
do tempo.

------------------------------------------------------------------------

# Experimento 05 --- Comparação com a relação de Kepler

Calcular um período de referência e comparar com o período obtido pela
simulação.


$$
T^2 = \frac{4\pi^2}{GM}a^3
$$


Depois:


$$
Erro(%) = \frac{|T_{simulado}-T_{referência}|}
{T\_{referência}}\times100
$$


### Objetivo

Usar uma relação teórica conhecida como referência para avaliar a
simulação.

------------------------------------------------------------------------

# Experimento 06 --- Outros planetas

Depois que o modelo Sol--Terra estiver funcionando:

``` text
Mercúrio
Vênus
Terra
Marte
Júpiter
Saturno
Urano
Netuno
```

Não é obrigatório implementar todos imediatamente.

A ordem recomendada é:

``` text
Terra
↓
Marte
↓
Júpiter
↓
demais planetas
```

------------------------------------------------------------------------

# Experimento 07 --- Alteração das condições iniciais

Modificar ligeiramente a posição ou velocidade inicial.

Exemplo:

``` text
condição original
+0,1%
+1%
+5%
+10%
```

### Objetivo

Investigar como alterações nas condições iniciais influenciam a
trajetória obtida.

------------------------------------------------------------------------

# Experimento 08 --- Mais de um corpo

Após validar o modelo simples, adicionar outro corpo.

Exemplo:

``` text
Sol
 ↓
Terra
 ↓
Júpiter
```

A intenção não é reproduzir todo o Sistema Solar de imediato.

O objetivo é observar como a inclusão de interações adicionais modifica
o comportamento do sistema.

------------------------------------------------------------------------

# 🧭 Metodologia completa

A metodologia seguirá estas etapas:

``` text
ETAPA 1
Revisão bibliográfica
        ↓
ETAPA 2
Definição do modelo físico
        ↓
ETAPA 3
Definição das equações
        ↓
ETAPA 4
Implementação de Euler
        ↓
ETAPA 5
Validação inicial
        ↓
ETAPA 6
Implementação de Verlet
        ↓
ETAPA 7
Testes controlados
        ↓
ETAPA 8
Coleta de dados
        ↓
ETAPA 9
Análise estatística/computacional
        ↓
ETAPA 10
Gráficos e tabelas
        ↓
ETAPA 11
Interpretação
        ↓
ETAPA 12
Conclusões
```

------------------------------------------------------------------------

# 💻 Arquitetura do software

O software será dividido em partes para separar:

-   modelo físico;
-   métodos numéricos;
-   dados;
-   experimentos;
-   análise;
-   visualização.

## Fluxo

``` text
Dados
  ↓
Modelo físico
  ↓
Aceleração
  ↓
Integrador
  ↓
Simulação
  ↓
Resultados
  ↓
Análise
  ↓
Gráficos
```

------------------------------------------------------------------------

# 🛠 Tecnologias e bibliotecas

## Python

Linguagem principal.

Será utilizada para:

-   cálculos;
-   simulação;
-   organização dos experimentos;
-   análise dos dados;
-   geração dos gráficos.

------------------------------------------------------------------------

## NumPy

Biblioteca principal para:

-   vetores;
-   matrizes;
-   operações matemáticas;
-   cálculo de normas;
-   manipulação eficiente de dados.

Exemplo:

``` python
import numpy as np

posicao = np.array([1.496e11, 0.0])

r = np.linalg.norm(posicao)
```

------------------------------------------------------------------------

## Pandas

Será utilizado para organizar resultados experimentais.

Exemplo de tabela:

  método       dt   erro   tempo
  -------- ------ ------ -------
  Euler      3600    ...     ...
  Verlet     3600    ...     ...

------------------------------------------------------------------------

## Matplotlib

Será utilizado para:

-   trajetórias;
-   gráficos de erro;
-   energia;
-   tempo de execução;
-   comparação entre métodos.

------------------------------------------------------------------------

## SciPy --- opcional

Pode ser utilizada posteriormente para:

-   métodos numéricos;
-   validações;
-   comparação com soluções de referência.

A implementação dos métodos principais deve ser feita pelo próprio
projeto quando isso for útil para demonstrar o funcionamento dos
algoritmos.

------------------------------------------------------------------------

# 📁 Estrutura de pastas

Estrutura recomendada:

``` text
kepler-newton/
│
├── main.py
│
├── models/
│   ├── kepler.py
│   └── newton.py
│
├── integrators/
│   ├── euler.py
│   ├── verlet.py
│   └── rk4.py
│
├── data/
│   └── planets.csv
│
├── experiments/
│   ├── experiment_01.py
│   ├── experiment_02.py
│   ├── experiment_03.py
│   └── experiment_04.py
│
├── analysis/
│   ├── errors.py
│   ├── energy.py
│   └── statistics.py
│
├── visualization/
│   └── plots.py
│
├── results/
│   ├── graphs/
│   └── tables/
│
└── README.md
```

### Estratégia

Não é necessário começar com essa estrutura inteira.

Começar simples:

``` text
projeto/
└── main.py
```

Depois separar os componentes conforme o código crescer.

------------------------------------------------------------------------

# 🧑‍💻 Plano de desenvolvimento do código

## Fase 1 --- Primeiro programa

Criar:

-   constante `G`;
-   massa do Sol;
-   posição inicial;
-   velocidade inicial;
-   `dt`;
-   laço de simulação;
-   cálculo da aceleração;
-   atualização da posição;
-   armazenamento dos resultados.

------------------------------------------------------------------------

## Fase 2 --- Vetores

Representar:

``` python
posicao = np.array([x, y])
velocidade = np.array([vx, vy])
```

Calcular:

``` python
r = np.linalg.norm(posicao)
```

E:

``` python
aceleracao = -G * M * posicao / r**3
```

------------------------------------------------------------------------

## Fase 3 --- Armazenamento

Em vez de apenas imprimir:

``` python
print(posicao)
```

guardar:

``` python
trajetoria.append(posicao.copy())
```

Depois transformar os dados em arrays:

``` python
trajetoria = np.array(trajetoria)
```

------------------------------------------------------------------------

## Fase 4 --- Primeiro gráfico

Plotar:

``` python
plt.plot(
    trajetoria[:, 0],
    trajetoria[:, 1]
)
```

Adicionar:

-   título;
-   eixo X;
-   eixo Y;
-   unidade;
-   legenda quando necessário.

------------------------------------------------------------------------

# 📐 Dados dos planetas

Os dados utilizados deverão ser documentados.

Para cada planeta, idealmente teremos:

  Dado                                 Exemplo
  ---------------------------------- ---------
  Massa                                     kg
  Distância média                            m
  Semi-eixo maior                            m
  Período orbital                            s
  Velocidade orbital de referência         m/s
  Excentricidade                           ---

### Fonte dos dados

Os valores deverão vir de fontes confiáveis, preferencialmente:

-   instituições científicas;
-   bases astronômicas;
-   literatura acadêmica;
-   NASA/JPL;
-   outras fontes institucionais verificáveis.

**Nunca colocar valores aproximados sem registrar a fonte.**

------------------------------------------------------------------------

# 📏 Unidades e escalas

Um problema importante é a diferença enorme entre as escalas.

Por exemplo:

``` text
distância → bilhões de metros
massa → bilhões de bilhões de kg
tempo → segundos
velocidade → milhares de m/s
```

Inicialmente podemos utilizar o Sistema Internacional:

``` text
massa       → kg
distância   → m
tempo       → s
velocidade  → m/s
aceleração  → m/s²
```

------------------------------------------------------------------------

# 🌍 Possibilidade de usar Unidades Astronômicas

Para facilitar visualização, podemos posteriormente utilizar:


$$
1,UA \approx 1,496\times10^{11},m
$$


Assim:

``` text
Terra ≈ 1 UA
```

Isso pode tornar os gráficos mais fáceis de interpretar.

**Importante:** a unidade utilizada no cálculo precisa ser consistente.

------------------------------------------------------------------------

# ✅ Validação dos resultados

Antes de fazer experimentos complexos, o programa precisa ser validado.

## Nível 1 --- Validação matemática

Verificar manualmente:

-   distância;
-   aceleração;
-   velocidade inicial;
-   número de passos.

------------------------------------------------------------------------

## Nível 2 --- Validação física

Verificar:

-   sentido da aceleração;
-   comportamento orbital;
-   distância ao corpo central;
-   comportamento da velocidade.

------------------------------------------------------------------------

## Nível 3 --- Validação por referência

Comparar:

-   período;
-   semi-eixo;
-   energia;
-   trajetória;

com valores teóricos ou referências escolhidas.

------------------------------------------------------------------------

## Nível 4 --- Validação entre métodos

Executar o mesmo problema usando:

``` text
Euler
Verlet
```

e verificar diferenças.

------------------------------------------------------------------------

# 📈 Análise dos resultados

A análise deverá responder perguntas científicas.

Não basta dizer:

> "O gráfico ficou assim."

É necessário interpretar:

> "O aumento do passo de tempo provocou aumento do erro?"

ou:

> "Qual método apresentou menor variação relativa de energia?"

ou:

> "A redução de `dt` melhorou a precisão proporcionalmente ao aumento do
> custo computacional?"

------------------------------------------------------------------------

# 📊 Gráficos e tabelas

## Gráfico 1 --- Trajetória

``` text
X × Y
```

Mostra a órbita simulada.

------------------------------------------------------------------------

## Gráfico 2 --- Erro ao longo do tempo

``` text
tempo × erro
```

Permite observar o acúmulo de erro.

------------------------------------------------------------------------

## Gráfico 3 --- Energia

``` text
tempo × energia
```

Permite observar a estabilidade da energia.

------------------------------------------------------------------------

## Gráfico 4 --- Tempo de execução

``` text
método × tempo
```

Compara o custo computacional.

------------------------------------------------------------------------

## Gráfico 5 --- Precisão × custo

Um dos gráficos mais importantes.

Pode mostrar:

``` text
erro
  ↑
  │
  │      método A
  │
  │  método B
  │
  └────────────────→ tempo
```

A forma final dependerá dos resultados.

------------------------------------------------------------------------

# 🏆 Demonstração na MiT

A apresentação pode ser estruturada como uma pequena investigação.

## Demonstração 1 --- Órbita básica

Mostrar:

``` text
Sol + Terra
```

------------------------------------------------------------------------

## Demonstração 2 --- Euler × Verlet

Selecionar:

``` text
Euler
```

executar.

Depois:

``` text
Verlet
```

executar.

Mostrar a diferença.

------------------------------------------------------------------------

## Demonstração 3 --- Passo de tempo

Alterar:

``` text
dt
```

e mostrar como isso afeta o resultado.

------------------------------------------------------------------------

## Demonstração 4 --- Condição inicial

Alterar ligeiramente:

``` text
velocidade inicial
```

e observar a mudança da trajetória.

------------------------------------------------------------------------

## Interface

Uma interface simples poderá conter:

``` text
========================================
 ENTRE KEPLER E NEWTON
========================================

Planeta:
[ Terra              ▼ ]

Método:
[ Euler              ▼ ]

Tempo de simulação:
[ 365 dias             ]

Passo:
[ 1 hora               ]

[ SIMULAR ]

----------------------------------------

Resultado:
Período: ...
Erro: ...
Tempo: ...

        [ gráfico da órbita ]
```

### Mas a interface é secundária

Primeiro:

> **ciência → código → resultados**

Depois:

> **interface**

------------------------------------------------------------------------

# 🗓 Cronograma

Considerando a apresentação da MiT em **28/10/2026**:

## 15--21 setembro

### Fundamentação

-   estudar Kepler;
-   estudar Newton;
-   revisar vetores;
-   revisar movimento circular/orbital;
-   estudar integração numérica;
-   definir experimentos.

**Resultado da semana:** modelo científico definido.

------------------------------------------------------------------------

## 22--28 setembro

### Primeira simulação

-   preparar ambiente Python;
-   instalar bibliotecas;
-   implementar Euler;
-   simular Sol + Terra;
-   gerar primeiro gráfico.

**Resultado da semana:** primeira órbita funcionando.

------------------------------------------------------------------------

## 29 setembro--5 outubro

### Métodos numéricos

-   revisar Euler;
-   implementar Verlet;
-   testar `dt`;
-   começar coleta de métricas;
-   corrigir erros;
-   organizar código.

**Meta:** congelar o núcleo principal do software até aproximadamente
05/10.

------------------------------------------------------------------------

## 6--12 outubro

### Experimentos

Executar:

-   comparação Euler × Verlet;
-   diferentes `dt`;
-   períodos diferentes;
-   energia;
-   erros;
-   tempo de execução;
-   condições iniciais.

**Resultado:** banco de resultados.

------------------------------------------------------------------------

## 13--19 outubro

### Análise e escrita

-   interpretar resultados;
-   selecionar gráficos;
-   montar tabelas;
-   escrever metodologia;
-   escrever resultados;
-   escrever discussão;
-   elaborar conclusão.

------------------------------------------------------------------------

## 20--27 outubro

### Apresentação

-   banner;
-   slides;
-   demonstração;
-   revisão;
-   ensaio;
-   preparação de perguntas.

------------------------------------------------------------------------

## 28 outubro

# 🎓 19ª MiT

Apresentação do projeto.

------------------------------------------------------------------------

# 📦 Entregáveis

Ao final do projeto devemos ter:

## 1. Código

Projeto Python organizado.

## 2. Dados

Arquivos com resultados experimentais.

## 3. Gráficos

Trajetórias e comparações.

## 4. Tabelas

Comparação entre métodos.

## 5. Texto científico

Resumo/artigo conforme exigência do evento.

## 6. Banner

Apresentação visual.

## 7. Slides

Apresentação oral.

## 8. Demonstração

Programa funcionando.

## 9. Repositório

Opcionalmente, GitHub com:

``` text
README
código
dados
gráficos
documentação
```

------------------------------------------------------------------------

# ⚠️ Possíveis dificuldades e soluções

## Problema 1 --- Órbita explode

### Possíveis causas

-   `dt` muito grande;
-   erro no cálculo da aceleração;
-   unidade inconsistente;
-   condição inicial inadequada.

### Solução

Testar:

``` text
dt menor
```

e verificar as equações.

------------------------------------------------------------------------

## Problema 2 --- Gráfico parece estranho

Verificar:

-   unidades;
-   escala dos eixos;
-   posição inicial;
-   velocidade inicial;
-   massa utilizada.

------------------------------------------------------------------------

## Problema 3 --- Euler apresenta muito erro

Isso não significa necessariamente que o projeto deu errado.

Na verdade, **o comportamento do método pode ser justamente um resultado
importante da pesquisa**.

O importante é medir e comparar.

------------------------------------------------------------------------

## Problema 4 --- Simulação muito lenta

Possíveis soluções:

-   aumentar `dt` quando cientificamente justificável;
-   usar NumPy;
-   evitar `print()` dentro de milhões de iterações;
-   armazenar somente os dados necessários;
-   otimizar o código.

------------------------------------------------------------------------

## Problema 5 --- Modelo com muitos corpos fica complicado

Não começar pelo Sistema Solar completo.

Seguir:

``` text
Sol + Terra
       ↓
Sol + Terra + Júpiter
       ↓
mais corpos
```

------------------------------------------------------------------------

## Problema 6 --- Falta de tempo

Prioridade:

### Essencial

-   Sol + Terra;
-   Euler;
-   Verlet;
-   comparação;
-   erro;
-   energia;
-   tempo;
-   gráficos.

### Importante

-   outros planetas;
-   alteração das condições iniciais.

### Extra

-   RK4;
-   muitos corpos;
-   interface sofisticada.

Se faltar tempo, **não sacrificar o núcleo científico para criar uma
interface bonita**.

------------------------------------------------------------------------

# 🎯 Critérios para considerar o projeto concluído

O projeto estará em uma versão sólida quando for possível:

-   [ ] explicar as Leis de Kepler;
-   [ ] explicar a Gravitação de Newton;
-   [ ] explicar as equações utilizadas;
-   [ ] explicar integração numérica;
-   [ ] executar Sol + Terra;
-   [ ] executar Euler;
-   [ ] executar Verlet;
-   [ ] alterar `dt`;
-   [ ] calcular período;
-   [ ] calcular erro;
-   [ ] calcular energia;
-   [ ] medir tempo;
-   [ ] gerar gráficos;
-   [ ] comparar métodos;
-   [ ] documentar os experimentos;
-   [ ] interpretar os resultados;
-   [ ] preparar o banner;
-   [ ] preparar os slides;
-   [ ] conseguir executar uma demonstração ao vivo.

------------------------------------------------------------------------

# 🧠 Como explicar o projeto para alguém

Uma explicação curta:

> **"Eu estou desenvolvendo uma simulação computacional do movimento
> planetário usando as leis de Kepler e a gravitação de Newton como
> base. A parte principal da pesquisa é comparar diferentes métodos
> numéricos e analisar como eles influenciam a precisão, a estabilidade
> e o custo dos cálculos."**

### Se perguntarem: "Mas você está provando Kepler?"

Resposta:

> **"Não. As leis já são conhecidas. Eu uso essas relações como base
> teórica e como referência para validar os resultados da simulação."**

### Se perguntarem: "Qual é a parte de Computação?"

Resposta:

> **"A Computação é utilizada para resolver numericamente as equações do
> movimento e realizar experimentos controlados, comparando métodos,
> erros, estabilidade e tempo de execução."**

### Se perguntarem: "Por que comparar Euler e Verlet?"

Resposta:

> **"Porque eles realizam a integração numérica de maneiras diferentes.
> A comparação permite investigar como a escolha do método influencia o
> comportamento da simulação."**

### Se perguntarem: "Qual método é melhor?"

Não responder antes dos experimentos.

Resposta adequada:

> **"Essa é justamente uma das questões que pretendo investigar. Vou
> comparar os métodos usando métricas como erro, estabilidade,
> conservação da energia e custo computacional."**

------------------------------------------------------------------------

# 📚 Referências

As referências iniciais utilizadas para fundamentar o projeto são:

**NASA.** *Orbits and Kepler's Laws*. NASA Science, 2024. Disponível em:
https://science.nasa.gov/solar-system/orbits-and-keplers-laws/. Acesso
em: 15 set. 2026.

**NASA.** *Gravity & Mechanics: Chapter 3*. NASA Science. Disponível em:
https://science.nasa.gov/learn/basics-of-space-flight/chapter3-3/.
Acesso em: 15 set. 2026.

**GUERRERO, Marcelo.** *Mecânica do Sistema Solar (II): Leis de Kepler*.
Belo Horizonte: Universidade Federal de Minas Gerais, 
$$
s.d.
$$
.
Disponível em:
https://lilith.fisica.ufmg.br/\~guerrero/notas-fis004/01-sistema_solar_02.pdf.
Acesso em: 15 set. 2026.

------------------------------------------------------------------------

# 🔬 Estrutura científica resumida

O projeto inteiro pode ser entendido através deste esquema:

``` text
                  PERGUNTA
                     │
                     ▼
        Como o método numérico
        influencia a simulação?
                     │
                     ▼
             MODELO FÍSICO
                     │
             Newton + Kepler
                     │
                     ▼
          EQUAÇÕES DO MOVIMENTO
                     │
                     ▼
          INTEGRAÇÃO NUMÉRICA
              │            │
              ▼            ▼
            Euler        Verlet
              │            │
              └──────┬─────┘
                     ▼
                 SIMULAÇÃO
                     │
                     ▼
              COLETA DE DADOS
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
        Erro       Energia     Tempo
          │          │          │
          └──────────┼──────────┘
                     ▼
               COMPARAÇÃO
                     │
                     ▼
                ANÁLISE
                     │
                     ▼
                CONCLUSÃO
```

------------------------------------------------------------------------

# 🚀 Ordem prática para começar AGORA

Não vamos tentar fazer tudo de uma vez.

## Passo 1 --- Ambiente

Instalar/verificar:

``` bash
python --version
```

Depois:

``` bash
pip install numpy matplotlib pandas
```

------------------------------------------------------------------------

## Passo 2 --- Primeiro programa

Criar:

``` text
main.py
```

E fazer apenas:

``` text
Sol + Terra
+
Newton
+
Euler
+
gráfico
```

------------------------------------------------------------------------

## Passo 3 --- Verificar fisicamente

Antes de continuar, responder:

-   a Terra está sendo atraída para o Sol?
-   a trajetória faz sentido?
-   a escala está correta?
-   o `dt` está adequado?

------------------------------------------------------------------------

## Passo 4 --- Transformar em experimento

Depois que o programa funcionar:

``` text
Euler
×
Verlet
```

com exatamente as mesmas condições.

------------------------------------------------------------------------

## Passo 5 --- Medir

Adicionar:

``` text
período
erro
energia
tempo
```

------------------------------------------------------------------------

## Passo 6 --- Produzir evidências

Gerar:

``` text
gráficos
tabelas
dados
```

------------------------------------------------------------------------

## Passo 7 --- Expandir

Somente depois:

``` text
outros planetas
condições iniciais
mais corpos
RK4
interface
```

------------------------------------------------------------------------

# ⭐ Regra principal do projeto

> **Não tentar construir o Sistema Solar inteiro antes de provar que
> Sol + Terra funciona corretamente.**

A ordem correta será:

``` text
Física
  ↓
Matemática
  ↓
Código simples
  ↓
Validação
  ↓
Experimento
  ↓
Medição
  ↓
Comparação
  ↓
Expansão
```

Isso evita que o projeto vire apenas uma aplicação visual e mantém o
foco na **investigação científico-computacional**.

------------------------------------------------------------------------

# 🏁 Resultado esperado do projeto

Ao final, o projeto deverá permitir responder, com base nos experimentos
realizados:

> **Como diferentes métodos numéricos e diferentes níveis de
> simplificação do modelo influenciam a precisão, a estabilidade e o
> custo computacional da simulação do movimento planetário?**

A resposta não será determinada antecipadamente.

Ela será construída a partir de:


$$
\boxed{
\text{Modelo}
\rightarrow
\text{Algoritmo}
\rightarrow
\text{Experimento}
\rightarrow
\text{Dados}
\rightarrow
\text{Análise}
\rightarrow
\text{Conclusão}
}
$$


**Esse é o núcleo científico do projeto.**
