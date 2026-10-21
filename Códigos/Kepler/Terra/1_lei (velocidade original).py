import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# CONSTANTES ASTRONÔMICAS
# ==========================================

# Parâmetro gravitacional do Sol (JPL)
MU_SOL = 1.32712440041279419e20

# Unidade astronômica em metros
UA = 149_597_870_700.0

# ==========================================
# ELEMENTOS ORBITAIS DA TERRA - J2000
# ==========================================

# Semieixo maior
a_real = 1.00000011 * UA

# Excentricidade orbital
e_real = 0.01671022

# ==========================================
# CONDIÇÕES INICIAIS NO PERIÉLIO
# ==========================================

# Distância no periélio
r_perielio = a_real * (1 - e_real)

# Distância no afélio - valor teórico
r_afelio = a_real * (1 + e_real)

# Velocidade no periélio pela equação vis-viva
v_perielio = np.sqrt(
    MU_SOL * (
        2 / r_perielio
        - 1 / a_real
    )
)

# Terra começa no periélio
posicao = np.array([
    r_perielio,
    0.0
])

# Velocidade tangencial
velocidade = np.array([
    0.0,
    v_perielio
])

# ==========================================
# CONFIGURAÇÃO DA SIMULAÇÃO
# ==========================================

dt = 60 * 60           # 1 hora
tempo_total = 366 * 24 * 60 * 60

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

    trajetoria.append(
        posicao.copy()
    )

    r = np.linalg.norm(posicao)

    distancias.append(r)

    # Gravitação do Sol
    aceleracao = (
        -MU_SOL
        * posicao
        / r**3
    )

    # Euler-Cromer
    velocidade = (
        velocidade
        + aceleracao * dt
    )

    posicao = (
        posicao
        + velocidade * dt
    )

# ==========================================
# ARRAYS
# ==========================================

trajetoria = np.array(trajetoria)
distancias = np.array(distancias)

# ==========================================
# RESULTADOS DA SIMULAÇÃO
# ==========================================

distancia_minima = np.min(
    distancias
)

distancia_maxima = np.max(
    distancias
)

a_simulado = (
    distancia_maxima
    + distancia_minima
) / 2

e_simulado = (
    distancia_maxima
    - distancia_minima
) / (
    distancia_maxima
    + distancia_minima
)

# ==========================================
# RESULTADOS
# ==========================================

print()
print("=" * 65)
print("1ª LEI DE KEPLER - TERRA COM VALORES REAIS")
print("=" * 65)

print()
print("VALORES DE REFERÊNCIA:")

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
print("RESULTADOS DA SIMULAÇÃO:")

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

print()
print("=" * 65)

# ==========================================
# GRÁFICO
# ==========================================

plt.figure(figsize=(8, 8))

plt.plot(
    trajetoria[:, 0],
    trajetoria[:, 1],
    label="Órbita simulada"
)

plt.scatter(
    0,
    0,
    s=150,
    label="Sol"
)

plt.xlabel("Posição x (m)")
plt.ylabel("Posição y (m)")

plt.title(
    "1ª Lei de Kepler - Órbita Realista da Terra"
)

plt.axis("equal")
plt.grid()
plt.legend()

plt.savefig(
    "primeira_lei_terra_real.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
