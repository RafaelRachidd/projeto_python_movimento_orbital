# 🌌 Projeto: Entre Kepler e Newton
## Análise Computacional do Movimento dos Planetas

> **Diário técnico e científico — Etapa 2**
>
> Registro do experimento sobre a influência do **passo de tempo (`dt`)** na simulação orbital utilizando o **método de Euler**.

---

# 📚 1. O que já foi feito

Até este momento, o projeto já possui uma primeira simulação computacional do sistema **Sol–Terra**.

O programa foi desenvolvido em **Python** e utiliza:

- **NumPy** → cálculos numéricos e vetoriais;
- **Matplotlib** → geração dos gráficos;
- **Método de Euler** → integração numérica da equação do movimento;
- modelo gravitacional simplificado → a Terra sofre a atração gravitacional do Sol.

A primeira simulação mostrou que o programa consegue produzir uma trajetória orbital aproximadamente circular.

Depois disso, foi realizado um experimento mais importante: **alterar o tamanho do passo de tempo (`dt`) e observar como isso modifica os resultados da simulação**.

Esse experimento é uma das primeiras partes realmente quantitativas da investigação.

---

# 🔬 2. Por que estamos estudando o passo de tempo?

Uma simulação computacional não calcula o movimento de forma contínua como acontece na realidade.

O computador trabalha com uma sequência de instantes:

```text
t₀ → t₁ → t₂ → t₃ → t₄ → ...
```

Em cada instante, o programa calcula a posição e a velocidade do corpo.

O intervalo entre dois desses instantes é chamado de **passo de tempo**.

Representamos esse intervalo por:

\[
\Delta t
\]

ou, no código Python:

```python
dt
```

Por exemplo:

```python
dt = 60 * 60
```

significa:

```text
dt = 3600 segundos
dt = 1 hora
```

Portanto, quando usamos `dt = 1 hora`, o programa calcula uma nova aproximação da posição da Terra a cada uma hora de simulação.

---

# ⏱️ 3. O que significa aumentar o passo de tempo?

Imagine que queremos simular 1 dia.

### Passo de 1 hora

O computador faz aproximadamente:

```text
24 cálculos
```

### Passo de 6 horas

Faz:

```text
4 cálculos
```

### Passo de 12 horas

Faz:

```text
2 cálculos
```

### Passo de 24 horas

Faz:

```text
1 cálculo
```

Quanto maior o `dt`, menos pontos intermediários são calculados.

Podemos visualizar assim:

```text
REALIDADE
──────────────────────────────────────────────►
tempo contínuo

SIMULAÇÃO COM dt PEQUENO
●──●──●──●──●──●──●──●──●──●

SIMULAÇÃO COM dt GRANDE
●────────●────────●────────●
```

O segundo caso possui muito menos informações entre os pontos.

---

# 🧮 4. Por que isso influencia a precisão?

O método de Euler não encontra exatamente a solução da equação física.

Ele faz uma **aproximação**.

A ideia básica é:

\[
\vec{v}_{n+1} =
\vec{v}_n + \vec{a}_n\Delta t
\]

e depois:

\[
\vec{r}_{n+1} =
\vec{r}_n + \vec{v}_{n+1}\Delta t
\]

onde:

- \(\vec{r}\) = posição;
- \(\vec{v}\) = velocidade;
- \(\vec{a}\) = aceleração;
- \(\Delta t\) = passo de tempo;
- \(n\) = instante atual;
- \(n+1\) = próximo instante.

A aceleração gravitacional utilizada no projeto é:

\[
\vec{a} =
-GM\frac{\vec{r}}{|\vec{r}|^3}
\]

Assim, o programa calcula repetidamente:

```text
posição atual
       ↓
distância até o Sol
       ↓
aceleração gravitacional
       ↓
nova velocidade
       ↓
nova posição
       ↓
repete
```

O problema é que a aceleração muda continuamente durante a órbita.

Quando usamos um passo grande, estamos fazendo uma aproximação mais grosseira desse movimento contínuo.

---

# ⚖️ 5. Existe uma relação entre precisão e custo computacional

O `dt` cria um compromisso importante.

## Passo pequeno

Exemplo:

```text
dt = 1 hora
```

Vantagens:

- mais pontos calculados;
- maior detalhamento da trajetória;
- menor intervalo entre aproximações;
- tendência a produzir uma aproximação mais precisa.

Desvantagem:

- maior quantidade de cálculos.

---

## Passo grande

Exemplo:

```text
dt = 24 horas
```

Vantagens:

- menos cálculos;
- execução potencialmente mais rápida;
- menor quantidade de dados.

Desvantagens:

- menos pontos intermediários;
- aproximação mais grosseira;
- maior possibilidade de erro numérico e instabilidade.

---

# 🧪 6. Nosso experimento

Mantivemos o restante da simulação igual e alteramos somente o **passo de tempo**.

Foram testados:

| Experimento | Passo de tempo |
|---|---:|
| 1 | 1 hora |
| 2 | 6 horas |
| 3 | 12 horas |
| 4 | 24 horas |

A ideia foi descobrir:

> **Como o aumento do passo de tempo influencia a variação da distância entre a Terra e o Sol durante a simulação?**

Essa é uma variável que podemos controlar diretamente no programa.

---

# 📊 7. Resultados obtidos

Os resultados registrados no programa foram:

| Passo de tempo | Distância mínima | Distância máxima | Variação |
|---|---:|---:|---:|
| **1 hora** | 1,494 × 10¹¹ m | 1,496 × 10¹¹ m | **2,083 × 10⁸ m** |
| **6 horas** | 1,492 × 10¹¹ m | 1,499 × 10¹¹ m | **6,669 × 10⁸ m** |
| **12 horas** | 1,489 × 10¹¹ m | 1,502 × 10¹¹ m | **1,297 × 10⁹ m** |
| **24 horas** | 1,482 × 10¹¹ m | 1,508 × 10¹¹ m | **2,576 × 10⁹ m** |

---

# 📐 8. O que significa a distância mínima?

Durante a simulação, a posição da Terra muda.

Em cada instante, o programa calcula:

\[
r = |\vec{r}|
\]

Esse valor representa a distância entre a Terra e o Sol.

O programa guarda todas essas distâncias.

Depois podemos encontrar:

\[
r_{\min} = \min(r_1,r_2,r_3,\ldots,r_n)
\]

Ou seja:

> **a menor distância registrada entre a Terra e o Sol durante a simulação.**

---

# 📏 9. O que significa a distância máxima?

Da mesma maneira:

\[
r_{\max} = \max(r_1,r_2,r_3,\ldots,r_n)
\]

Representa:

> **a maior distância registrada entre a Terra e o Sol durante a simulação.**

---

# 📊 10. O que significa a "variação" do nosso gráfico?

No experimento, calculamos:

\[
\Delta r = r_{\max} - r_{\min}
\]

Portanto, a variação não significa diretamente "erro".

Ela representa a **amplitude da mudança na distância Terra–Sol observada na simulação**.

Essa distinção é importante para o trabalho científico.

### Exemplo: 24 horas

Temos aproximadamente:

\[
r_{\min}=1,482\times10^{11}\text{ m}
\]

e:

\[
r_{\max}=1,508\times10^{11}\text{ m}
\]

Logo:

\[
\Delta r =
1,508\times10^{11}
-
1,482\times10^{11}
\]

resultando aproximadamente em:

\[
\Delta r=2,6\times10^9\text{ m}
\]

O programa apresentou:

\[
\boxed{2,576\times10^9\text{ m}}
\]

---

# 📈 11. Interpretação detalhada do gráfico

O gráfico possui:

### Eixo X

Representa o **passo de tempo utilizado na simulação**:

```text
1 hora
6 horas
12 horas
24 horas
```

### Eixo Y

Representa a **variação da distância**, em metros:

\[
\Delta r = r_{\max}-r_{\min}
\]

A escala científica exibida no gráfico é:

```text
1e9
```

Isso significa que os valores do eixo Y estão sendo apresentados em bilhões de metros.

Por exemplo:

```text
0,5 no gráfico ≈ 0,5 × 10⁹ m
```

ou:

```text
500.000.000 m
```

---

# 🔎 12. O comportamento observado

Existe uma tendência muito clara:

```text
1 hora   →  █
6 horas  →  ███
12 horas →  ██████
24 horas →  ████████████
```

A variação aumenta conforme aumentamos o passo de tempo.

### 1 hora

\[
\Delta r = 2,083\times10^8\text{ m}
\]

É a menor variação observada entre os quatro testes.

---

### 6 horas

\[
\Delta r = 6,669\times10^8\text{ m}
\]

A variação já é aproximadamente **3,2 vezes maior** que no teste de 1 hora.

---

### 12 horas

\[
\Delta r = 1,297\times10^9\text{ m}
\]

A variação já ultrapassa **1 bilhão de metros**.

---

### 24 horas

\[
\Delta r = 2,576\times10^9\text{ m}
\]

É o maior valor observado.

Comparando com o experimento de 1 hora, a variação é aproximadamente **12,4 vezes maior**.

---

# 📌 13. Comparação com a distância de referência

A distância utilizada inicialmente para a Terra foi aproximadamente:

\[
r_0 = 1,496\times10^{11}\text{ m}
\]

Isso corresponde a aproximadamente:

\[
149,6\text{ milhões de km}
\]

Podemos comparar a amplitude observada com essa distância inicial.

| Passo | Variação | Variação relativa aproximada |
|---|---:|---:|
| 1 hora | 2,083 × 10⁸ m | **0,139%** |
| 6 horas | 6,669 × 10⁸ m | **0,446%** |
| 12 horas | 1,297 × 10⁹ m | **0,867%** |
| 24 horas | 2,576 × 10⁹ m | **1,722%** |

Essa comparação ajuda a mostrar quantitativamente que o comportamento da simulação muda conforme alteramos o `dt`.

---

# ⚠️ 14. Isso significa que a simulação de 24 horas está errada?

**Ainda não podemos afirmar isso somente olhando esse gráfico.**

Esse é um ponto muito importante.

A variação observada não é automaticamente o "erro da simulação".

Estamos medindo:

\[
\Delta r=r_{\max}-r_{\min}
\]

Para falar em **erro**, precisamos comparar um resultado da simulação com um valor de referência.

Por exemplo, posteriormente podemos comparar:

- período orbital simulado × período esperado;
- energia simulada × energia inicial;
- posição simulada × posição de referência;
- trajetória obtida por um método × trajetória obtida por outro método.

Assim teremos métricas de erro mais rigorosas.

---

# 🧠 15. Então o que esse experimento já demonstra?

Ele demonstra uma **dependência do resultado em relação ao passo de integração**.

Em outras palavras:

> Quando modificamos o intervalo entre os cálculos, a trajetória produzida pelo método numérico também se modifica.

Isso é exatamente o tipo de comportamento que queremos investigar no projeto.

Ainda não estamos concluindo qual método é melhor.

Estamos construindo a base experimental necessária para fazer essa comparação posteriormente.

---

# 🔬 16. Variável independente e variável observada

Esse experimento já pode ser descrito de forma científica.

## Variável independente

É aquilo que nós alteramos propositalmente:

\[
\boxed{\Delta t}
\]

ou seja:

> **passo de tempo da simulação.**

Valores:

- 1 h;
- 6 h;
- 12 h;
- 24 h.

---

## Variável observada

É aquilo que medimos como resultado:

\[
\boxed{\Delta r}
\]

ou seja:

> **variação da distância entre a Terra e o Sol.**

---

## Variáveis mantidas

Para que a comparação seja válida, devemos manter constantes:

- massa do Sol;
- constante gravitacional;
- posição inicial da Terra;
- velocidade inicial da Terra;
- modelo gravitacional;
- método de Euler;
- duração da simulação.

Assim, tentamos fazer com que a principal diferença entre os experimentos seja o `dt`.

---

# 🧪 17. Por que isso é importante para a pesquisa?

Imagine que obtivéssemos os resultados abaixo:

```text
dt pequeno → pequena variação
dt médio   → variação maior
dt grande  → variação ainda maior
```

Isso sugere que o tamanho do passo possui influência sobre o comportamento numérico da simulação.

A partir daí surge uma investigação mais interessante:

> **Qual é o tamanho de passo adequado para obter uma simulação suficientemente precisa sem aumentar desnecessariamente o custo computacional?**

Essa pergunta conecta diretamente:

**Física + Matemática + Computação.**

---

# 💻 18. Relação com o custo computacional

Existe outra coisa que ainda precisamos medir.

Se simulamos um ano:

### 1 hora

\[
365\times24=8760
\]

passos.

### 6 horas

\[
365\times4=1460
\]

passos.

### 12 horas

\[
365\times2=730
\]

passos.

### 24 horas

\[
365
\]

passos.

Portanto:

| Passo | Passos em 1 ano |
|---|---:|
| 1 hora | 8.760 |
| 6 horas | 1.460 |
| 12 horas | 730 |
| 24 horas | 365 |

Isso mostra o outro lado do problema:

> **Passos menores aumentam a quantidade de cálculos necessários.**

Por isso não queremos simplesmente escolher o menor `dt` possível.

Queremos investigar o equilíbrio entre:

\[
\boxed{\text{Precisão} \times \text{Custo computacional}}
\]

---

# 🌎 19. O que ainda não devemos concluir

Neste momento, ainda não podemos afirmar:

❌ que Euler é o melhor método;

❌ que 1 hora é o melhor passo;

❌ que 24 horas é necessariamente inadequado;

❌ que a diferença observada é totalmente causada por erro numérico;

❌ que o modelo já representa perfeitamente uma órbita planetária real.

Essas conclusões exigem novos experimentos.

---

# 🎯 20. Próximo experimento recomendado

Agora que conseguimos controlar o `dt`, o próximo passo será medir uma grandeza ainda mais importante:

## Período orbital

Queremos descobrir:

> **Quanto tempo a Terra leva para completar uma volta na simulação?**

Depois poderemos comparar o valor obtido pelo programa com um valor de referência.

A fórmula do erro percentual será:

\[
Erro(\%)=
\frac{|T_{\text{simulado}}-T_{\text{referência}}|}
{T_{\text{referência}}}
\times100
\]

Isso permitirá transformar nossa análise em uma comparação quantitativa de precisão.

---

# 🧭 21. Caminho planejado do projeto

Até agora:

```text
[✓] Modelo Sol–Terra
        ↓
[✓] Gravitação Newtoniana
        ↓
[✓] Método de Euler
        ↓
[✓] Simulação da órbita
        ↓
[✓] Teste de diferentes passos de tempo
        ↓
[✓] Gráfico da variação da distância
        ↓
[PRÓXIMO] Medição do período orbital
        ↓
[PRÓXIMO] Cálculo do erro percentual
        ↓
[PRÓXIMO] Análise da energia
        ↓
[PRÓXIMO] Implementação do método de Verlet
        ↓
[PRÓXIMO] Comparação Euler × Verlet
        ↓
[PRÓXIMO] Outros planetas
        ↓
[PRÓXIMO] Análise final
```

---

# 🏆 22. Resultado científico desta etapa

O principal resultado desta etapa foi observar experimentalmente que o **passo de tempo utilizado na integração numérica influencia a variação da distância registrada na simulação orbital**.

Os dados obtidos apresentaram aumento progressivo da variação:

\[
2,083\times10^8
\rightarrow
6,669\times10^8
\rightarrow
1,297\times10^9
\rightarrow
2,576\times10^9\text{ m}
\]

conforme o passo passou de:

\[
1h\rightarrow6h\rightarrow12h\rightarrow24h
\]

Esse resultado não encerra a investigação. Pelo contrário, ele fornece uma primeira evidência experimental para justificar os próximos testes de precisão, estabilidade e custo computacional.

---

# 📝 23. Registro para o relatório científico

Uma forma adequada de descrever esta etapa futuramente no trabalho é:

> **“Foi realizado um experimento inicial utilizando o método de Euler para avaliar a influência do passo de tempo na simulação da órbita terrestre. Foram testados intervalos de 1, 6, 12 e 24 horas, mantendo-se as demais condições iniciais constantes. Observou-se aumento progressivo da variação da distância entre a Terra e o Sol conforme o passo de tempo foi ampliado, passando de aproximadamente \(2,083\times10^8\) m para \(2,576\times10^9\) m. Esses resultados indicam que o intervalo utilizado na integração numérica influencia o comportamento obtido na simulação, motivando análises posteriores de erro, estabilidade e custo computacional.”**

> **Observação:** essa redação é para uso posterior no relatório. Como o projeto ainda está em desenvolvimento, não devemos tratá-la como conclusão final.

---

# 🧠 24. Conceito principal aprendido nesta etapa

### `dt` não é apenas uma configuração do programa.

Ele é uma **variável numérica que pode influenciar diretamente a qualidade da aproximação computacional de um fenômeno físico**.

Isso transforma uma simples alteração no código:

```python
dt = 60 * 60
```

em uma variável experimental:

\[
\boxed{\Delta t}
\]

que pode ser controlada, comparada e analisada cientificamente.

---

## 🌌 Estado atual do projeto

**Projeto:** Entre Kepler e Newton: Análise Computacional do Movimento dos Planetas

**Status:** 🟢 Desenvolvimento

**Modelo atual:** Sol + Terra

**Força utilizada:** Gravitação Universal de Newton

**Método atual:** Euler

**Linguagem:** Python 3.14.7

**Bibliotecas:** NumPy + Matplotlib

**Experimento concluído:** influência do passo de tempo

**Próxima etapa:** medir o período orbital e calcular o erro percentual.

---

> **Regra para as próximas etapas:** primeiro executamos o experimento, depois analisamos os dados e só então tiramos conclusões. Não vamos inventar resultados antes de o programa produzi-los.
