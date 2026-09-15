# 🌌 Entre Kepler e Newton: Análise Computacional do Movimento dos Planetas

> **Diário de desenvolvimento — Etapa 1**
>
> Registro didático do que foi desenvolvido até agora no projeto.

---

## 1. Sobre o projeto

O projeto estuda o movimento planetário utilizando **Física, Matemática e Computação**.

A ideia não é provar novamente as Leis de Kepler ou a Gravitação Universal de Newton. Essas teorias já são conhecidas. Elas serão utilizadas como base para construir modelos computacionais e investigar como diferentes escolhas na simulação influenciam os resultados.

A estrutura geral é:

```text
Problema científico
       ↓
Modelo físico e matemático
       ↓
Implementação em Python
       ↓
Simulação numérica
       ↓
Coleta dos dados
       ↓
Comparação dos resultados
       ↓
Análise científica
```

---

## 2. Pergunta inicial

A pergunta geral do projeto é:

> **Como a complexidade do modelo físico e o método numérico utilizado influenciam a precisão e o custo computacional da simulação do movimento orbital?**

Neste primeiro momento, investigamos uma questão mais específica:

> **Como o tamanho do passo de tempo influencia os resultados de uma simulação orbital utilizando o método de Euler?**

---

## 3. Primeiro sistema estudado: Sol e Terra

Começamos com:

- ☀️ Sol
- 🌎 Terra

A Terra é tratada como um corpo submetido à atração gravitacional do Sol.

Nesta primeira versão, o Sol é considerado aproximadamente fixo e estudamos o movimento da Terra ao seu redor.

### Por que começar assim?

Um sistema com muitos corpos possui muito mais variáveis e aumenta a complexidade. Começar com Sol + Terra permite:

1. entender as equações;
2. testar o programa;
3. verificar se a órbita faz sentido;
4. estudar os erros numéricos;
5. aumentar a complexidade posteriormente.

---

## 4. Modelo matemático

A base física é a **Lei da Gravitação Universal de Newton**:

$$
F = G\frac{Mm}{r^2}
$$

onde:

| Símbolo | Significado |
|---|---|
| $F$ | força gravitacional |
| $G$ | constante gravitacional |
| $M$ | massa do Sol |
| $m$ | massa da Terra |
| $r$ | distância entre os corpos |

Como:

$$
F = ma
$$

podemos obter a aceleração:

$$
a = \frac{F}{m}
$$

e, na forma vetorial utilizada na simulação:

$$
\vec{a} = -G\frac{M}{r^3}\vec{r}
$$

O sinal negativo indica que a aceleração aponta em direção ao Sol.

---

## 5. Representação por vetores

A posição da Terra é representada por:

$$
\vec{r}=(x,y)
$$

No Python:

```python
posicao = np.array([
    distancia_terra,
    0.0
])
```

A velocidade também é um vetor:

```python
velocidade = np.array([
    0.0,
    29_780.0
])
```

Assim, o programa consegue representar o movimento em duas dimensões.

---

## 6. Bibliotecas utilizadas

### NumPy

Utilizada para operações numéricas e vetoriais:

```python
import numpy as np
```

### Matplotlib

Utilizada para gerar os gráficos:

```python
import matplotlib.pyplot as plt
```

---

## 7. Constantes

Foram utilizadas:

```python
G = 6.67430e-11
M_sol = 1.989e30
```

Ou:

$$
G = 6{,}67430\times10^{-11}
$$

e aproximadamente:

$$
M_{Sol}=1{,}989\times10^{30}\ kg
$$

A distância inicial utilizada para a Terra foi:

```python
distancia_terra = 1.496e11
```

ou:

$$
r_0=1{,}496\times10^{11}\ m
$$

aproximadamente uma Unidade Astronômica.

---

## 8. Cálculo da distância

A distância da Terra ao Sol é calculada pela norma do vetor posição:

```python
r = np.linalg.norm(posicao)
```

Matematicamente:

$$
r=\sqrt{x^2+y^2}
$$

A distância é recalculada a cada passo da simulação.

---

## 9. Aceleração gravitacional no código

O programa calcula:

```python
aceleracao = -G * M_sol * posicao / r**3
```

Correspondendo a:

$$
\vec{a}=-G\frac{M}{r^3}\vec{r}
$$

A aceleração aponta continuamente para o Sol e altera a velocidade da Terra.

---

## 10. Método de Euler

O primeiro método numérico implementado foi o **método de Euler**.

Ele aproxima a solução utilizando o estado atual para estimar o próximo estado.

Para a velocidade:

$$
\vec{v}_{n+1}
=
\vec{v}_n+\vec{a}_n\Delta t
$$

Para a posição:

$$
\vec{r}_{n+1}
=
\vec{r}_n+\vec{v}_{n+1}\Delta t
$$

No código:

```python
velocidade = velocidade + aceleracao * dt
posicao = posicao + velocidade * dt
```

---

## 11. O que é `dt`?

`dt` representa o **passo de tempo** da simulação.

Por exemplo:

```python
dt = 60 * 60
```

significa:

```text
60 × 60 = 3600 segundos = 1 hora
```

Portanto, com `dt = 1 hora`, a simulação calcula um novo estado a cada hora de tempo simulado.

---

## 12. Primeiro experimento

Foi investigada a influência do tamanho de `dt`.

Foram testados:

| Passo | Segundos |
|---|---:|
| 1 hora | 3.600 |
| 6 horas | 21.600 |
| 12 horas | 43.200 |
| 24 horas | 86.400 |

Todas as simulações foram realizadas durante aproximadamente **1 ano**.

---

## 13. Resultados obtidos

Os testes produziram:

| Passo de tempo | Distância mínima | Distância máxima |
|---|---:|---:|
| **1 hora** | $1{,}494\times10^{11}$ m | $1{,}496\times10^{11}$ m |
| **6 horas** | $1{,}492\times10^{11}$ m | $1{,}498\times10^{11}$ m |
| **12 horas** | $1{,}489\times10^{11}$ m | $1{,}502\times10^{11}$ m |
| **24 horas** | $1{,}482\times10^{11}$ m | $1{,}508\times10^{11}$ m |

### Primeira observação

Os resultados indicam que, conforme aumentamos o passo de tempo, aumenta a variação da distância observada na simulação.

Isso é uma **observação experimental**, não uma conclusão definitiva sobre a qualidade do método.

---

## 14. Variação da distância

Uma primeira métrica utilizada é:

$$
\Delta r=r_{máx}-r_{mín}
$$

Por exemplo, para 1 hora:

$$
\Delta r=
1{,}496\times10^{11}
-
1{,}494\times10^{11}
$$

aproximadamente:

$$
\Delta r\approx2\times10^8\ m
$$

Essa medida permite comparar os diferentes experimentos.

---

## 15. O que os gráficos mostraram?

A trajetória produzida pelo programa ficou aproximadamente circular, representando a órbita da Terra ao redor do Sol.

Entretanto, alterar o passo de tempo modifica a forma como o computador acompanha essa trajetória.

A ideia é:

```text
dt pequeno
   ↓
mais cálculos
   ↓
maior resolução temporal

dt grande
   ↓
menos cálculos
   ↓
maior influência da aproximação numérica
```

Ainda precisamos de métricas adicionais para avaliar essa influência com maior precisão.

---

## 16. Um problema encontrado durante o desenvolvimento

Ao tentar automatizar os quatro experimentos, apareceu:

```text
NameError: name 'dt' is not defined
```

O motivo foi a substituição de:

```python
dt = 60 * 60
```

por uma lista:

```python
passos = [
    1 * 60 * 60,
    6 * 60 * 60,
    12 * 60 * 60,
    24 * 60 * 60
]
```

mas uma parte antiga do programa ainda utilizava:

```python
numero_passos = int(tempo_total / dt)
```

Como `dt` não era mais uma variável única, ocorreu o erro.

---

## 17. Como vamos corrigir

A ideia é fazer o programa percorrer automaticamente os valores:

```python
for dt, nome in zip(passos, nomes_passos):

    numero_passos = int(tempo_total / dt)

    # reiniciar posição e velocidade

    # executar a simulação

    # calcular distância mínima

    # calcular distância máxima

    # calcular variação

    # guardar resultado
```

Assim, os quatro experimentos serão executados automaticamente.

---

## 18. Por que reiniciar as condições iniciais?

Todos os experimentos precisam começar da mesma situação.

```text
Experimento 1
dt = 1 hora
posição inicial = mesma
velocidade inicial = mesma
tempo = 1 ano


Experimento 2
dt = 6 horas
posição inicial = mesma
velocidade inicial = mesma
tempo = 1 ano
```

Se um experimento começasse usando o resultado do anterior, a comparação seria prejudicada.

---

## 19. O projeto está deixando de ser apenas uma simulação

No início, poderíamos resumir o programa como:

> "Um programa que desenha a órbita da Terra."

Agora a proposta é mais científica:

> **Investigar como diferentes configurações numéricas alteram os resultados de uma simulação orbital.**

O programa é a **ferramenta de experimentação**.

A parte científica está na:

- definição das condições;
- execução dos experimentos;
- coleta dos dados;
- comparação;
- análise;
- interpretação.

---

# 20. Próximas etapas

### Agora

- [ ] Automatizar os quatro experimentos
- [ ] Criar tabela comparativa
- [ ] Criar gráfico da variação

### Depois

- [ ] Calcular o período orbital simulado
- [ ] Comparar com uma referência teórica
- [ ] Calcular erro percentual
- [ ] Analisar conservação da energia
- [ ] Implementar Verlet
- [ ] Comparar Euler × Verlet
- [ ] Testar outros planetas
- [ ] Alterar condições iniciais
- [ ] Estudar sistemas com mais de um corpo
- [ ] Organizar os resultados finais

---

## 21. Relação com as Leis de Kepler

As Leis de Kepler serão utilizadas como referência teórica.

A terceira lei estabelece uma relação entre o período orbital e o tamanho da órbita:

$$
T^2\propto a^3
$$

Para o modelo gravitacional simplificado:

$$
T^2=\frac{4\pi^2}{GM}a^3
$$

Uma etapa futura será comparar o período produzido pela simulação com o período esperado teoricamente.

O objetivo não é "provar Kepler", mas utilizar a teoria como **referência para avaliar o comportamento do modelo computacional**.

---

## 22. Hipótese inicial

Uma hipótese de trabalho é:

> **Métodos numéricos e configurações de simulação diferentes podem apresentar diferentes níveis de precisão, estabilidade e custo computacional na representação do movimento orbital.**

Os experimentos deverão fornecer evidências para avaliar essa hipótese.

---

## 23. Conceitos trabalhados até agora

### Física

- Gravitação Universal
- aceleração gravitacional
- velocidade orbital
- movimento planetário
- órbitas

### Matemática

- vetores
- norma vetorial
- equações diferenciais
- aproximação numérica
- análise de erro

### Computação

- Python
- NumPy
- Matplotlib
- listas
- estruturas de repetição
- simulação computacional
- armazenamento de resultados
- geração de gráficos

---

## 24. Cuidados científicos

Devemos diferenciar **resultado observado** de **conclusão**.

Evitar:

> "O método de Euler é ruim."

Preferir:

> **"Os resultados iniciais indicam que o tamanho do passo de tempo influencia a variação da distância obtida pela simulação utilizando o método de Euler."**

Depois de realizar mais experimentos, poderemos fazer conclusões quantitativas.

Também não devemos afirmar antecipadamente que Verlet será melhor. Isso será uma hipótese a ser testada.

---

# 🏁 25. Estado atual do projeto

### 🟢 Etapa: primeira simulação funcional

Já temos um protótipo funcional de uma simulação orbital **Sol–Terra utilizando o método de Euler**.

O fluxo atual é:

```text
Equações físicas
       ↓
Código Python
       ↓
Simulação
       ↓
Órbita da Terra
       ↓
Dados numéricos
       ↓
Primeira análise
```

O próximo passo é transformar os testes manuais em um **experimento automatizado e reproduzível**.

Depois, começaremos a trabalhar com **erro, período orbital e conservação de energia**, antes de implementar e comparar o método de Verlet.

---

## ⭐ Regra principal do projeto

> **Primeiro executar e medir; depois interpretar e concluir.**

Este documento deve ser atualizado conforme novos códigos, experimentos, gráficos e resultados forem desenvolvidos.
