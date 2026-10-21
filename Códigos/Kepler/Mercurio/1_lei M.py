import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# CONSTANTES ASTRONÔMICAS
# ==========================================

# Parâmetro gravitacional do Sol
MU_SOL = 1.32712440041279419e20

# Unidade astronômica em metros
UA = 149_597_870_700.0

# ==========================================
# ELEMENTOS ORBITAIS DE MERCÚRIO
# ==========================================

# Semieixo maior
a_real = 0.38709927 * UA

# Excentricidade orbital
e_real = 0.20563593

# ==========================================
# CONDIÇÕES INICIAIS NO PERIÉLIO
# ==========================================

# Distância no periélio
r_perielio = a_real * (1 - e_real)

# Distância no afélio
r_afelio = a_real * (1 + e_real)

# Velocidade no periélio pela equação vis-viva
v_perielio = np.sqrt(
    MU_SOL * (
        2 / r_perielio
        - 1 / a_real
    )
)

# Mercúrio começa no periélio
posicao = np.array([
    r_perielio,
    0.0
])

# Velocidade inicial tangencial
velocidade = np.array([
    0.0,
    v_perielio
])

# ==========================================
# CONFIGURAÇÃO DA SIMULAÇÃO
# ==========================================

# Passo de tempo: 1 hora
dt = 60 * 60

# 100 dias de simulação
tempo_total = (
    100
    * 24
    * 60
    * 60
)

numero_passos = int(
    tempo_total / dt
)

# ==========================================
# ARMAZENAMENTO
# ==========================================

trajetoria = []
distancias = []

# ==========================================
# SIMULAÇÃO - EULER-CROMER
# ==========================================

for i in range(numero_passos):

    # Armazena posição atual
    trajetoria.append(
        posicao.copy()
    )

    # Distância Mercúrio-Sol
    r = np.linalg.norm(
        posicao
    )

    distancias.append(
        r
    )

    # ======================================
    # ACELERAÇÃO GRAVITACIONAL
    # ======================================

    aceleracao = (
        -MU_SOL
        * posicao
        / r**3
    )

    # ======================================
    # MÉTODO DE EULER-CROMER
    # ======================================

    # Primeiro atualiza a velocidade
    velocidade = (
        velocidade
        + aceleracao * dt
    )

    # Depois atualiza a posição
    posicao = (
        posicao
        + velocidade * dt
    )

# ==========================================
# CONVERTER PARA ARRAYS
# ==========================================

trajetoria = np.array(
    trajetoria
)

distancias = np.array(
    distancias
)

# ==========================================
# RESULTADOS DA SIMULAÇÃO
# ==========================================

# Menor distância encontrada
distancia_minima = np.min(
    distancias
)

# Maior distância encontrada
distancia_maxima = np.max(
    distancias
)

# Semieixo maior estimado pela simulação
a_simulado = (
    distancia_maxima
    + distancia_minima
) / 2

# Excentricidade estimada
e_simulado = (
    distancia_maxima
    - distancia_minima
) / (
    distancia_maxima
    + distancia_minima
)

# ==========================================
# ERRO DA EXCENTRICIDADE
# ==========================================

erro_e = (
    abs(
        e_simulado
        - e_real
    )
    / e_real
    * 100
)

# ==========================================
# RESULTADOS
# ==========================================

print()

print("=" * 65)

print(
    "1ª LEI DE KEPLER - MERCÚRIO"
)

print("=" * 65)

print()

print(
    "VALORES DE REFERÊNCIA:"
)

print()

print(
    f"Semieixo maior: "
    f"{a_real:.3e} m"
)

print(
    f"Excentricidade real: "
    f"{e_real:.8f}"
)

print(
    f"Periélio teórico: "
    f"{r_perielio:.3e} m"
)

print(
    f"Afélio teórico: "
    f"{r_afelio:.3e} m"
)

print(
    f"Velocidade no periélio: "
    f"{v_perielio:.2f} m/s"
)

print()

print(
    "RESULTADOS DA SIMULAÇÃO:"
)

print()

print(
    f"Distância mínima: "
    f"{distancia_minima:.3e} m"
)

print(
    f"Distância máxima: "
    f"{distancia_maxima:.3e} m"
)

print(
    f"Semieixo maior simulado: "
    f"{a_simulado:.3e} m"
)

print(
    f"Excentricidade simulada: "
    f"{e_simulado:.8f}"
)

print(
    f"Erro da excentricidade: "
    f"{erro_e:.6f}%"
)

print()

print("=" * 65)

# ==========================================
# GRÁFICO
# ==========================================

plt.figure(
    figsize=(9, 8)
)

# Órbita simulada
plt.plot(
    trajetoria[:, 0],
    trajetoria[:, 1],
    label="Órbita de Mercúrio"
)

# ==========================================
# SOL
# ==========================================

plt.scatter(
    0,
    0,
    s=160,
    label="Sol",
    zorder=5
)

# ==========================================
# PERIÉLIO
# ==========================================

plt.scatter(
    r_perielio,
    0,
    s=80,
    label="Periélio",
    zorder=5
)

plt.text(
    r_perielio,
    3e9,
    "Periélio",
    ha="center"
)

# ==========================================
# AFÉLIO
# ==========================================

plt.scatter(
    -r_afelio,
    0,
    s=80,
    label="Afélio",
    zorder=5
)

plt.text(
    -r_afelio,
    3e9,
    "Afélio",
    ha="center"
)

# ==========================================
# CONFIGURAÇÕES DO GRÁFICO
# ==========================================

plt.xlabel(
    "Posição x (m)"
)

plt.ylabel(
    "Posição y (m)"
)

plt.title(
    "1ª Lei de Kepler - Órbita de Mercúrio"
)

# Mantém a proporção correta dos eixos
plt.axis(
    "equal"
)

plt.grid()

plt.legend()

plt.tight_layout()

# ==========================================
# SALVAR IMAGEM
# ==========================================

plt.savefig(
    "primeira_lei_mercurio_real.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
