import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# DADOS DOS EXPERIMENTOS
# ==========================================

passos = ["1 hora", "6 horas", "12 horas", "24 horas"]

# Variações obtidas no Euler-Cromer
variacoes_cromer = [
    2.083e8,
    6.669e8,
    1.297e9,
    2.576e9
]

# Variações obtidas no Euler Explícito
variacoes_explicito = [
    1.344e9,
    7.936e9,
    1.565e10,
    3.076e10
]

# ==========================================
# CONFIGURAÇÃO DO GRÁFICO
# ==========================================

x = np.arange(len(passos))   # posições no eixo x
largura = 0.35               # largura de cada barra

plt.figure(figsize=(10, 6))

# Barras do Euler-Cromer
plt.bar(
    x - largura/2,
    variacoes_cromer,
    largura,
    label="Euler-Cromer"
)

# Barras do Euler Explícito
plt.bar(
    x + largura/2,
    variacoes_explicito,
    largura,
    label="Euler Explícito",
    color="#cc0000"
)

# ==========================================
# PERSONALIZAÇÃO
# ==========================================

plt.xlabel("Passo de tempo")
plt.ylabel("Variação da distância (m)")
plt.title("Comparação entre Euler-Cromer e Euler Explícito")
plt.xticks(x, passos)
plt.legend()
plt.grid(axis="y")

# ==========================================
# EXIBIR GRÁFICO
# ==========================================
plt.savefig(
    "comparacao_euler.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
