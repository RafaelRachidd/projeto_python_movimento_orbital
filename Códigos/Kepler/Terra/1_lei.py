import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# CONSTANTES
# ==========================================

G = 6.67430e-11
M_sol = 1.989e30

# ==========================================
# CONDIÇÕES INICIAIS
# ==========================================

distancia_inicial = 1.496e11

posicao = np.array([
    distancia_inicial,
    0.0
])

# Velocidade menor que a usada anteriormente
# para gerar uma órbita elíptica mais visível
velocidade = np.array([
    0.0,
    29_780.0
])

# ==========================================
# CONFIGURAÇÃO DA SIMULAÇÃO
# ==========================================

dt = 1 * 60 * 60       # 1 hora
tempo_total = 365 * 24 * 60 * 60

numero_passos = int(tempo_total / dt)

# ==========================================
# ARMAZENAR TRAJETÓRIA
# ==========================================

trajetoria = []
distancias = []

# ==========================================
# SIMULAÇÃO - EULER-CROMER
# ==========================================

for i in range(numero_passos):

    # Guarda a posição atual
    trajetoria.append(posicao.copy())

    # Distância atual Terra-Sol
    r = np.linalg.norm(posicao)

    distancias.append(r)

    # Aceleração gravitacional
    aceleracao = (
        -G * M_sol * posicao / r**3
    )

    # Euler-Cromer
    velocidade = velocidade + aceleracao * dt
    posicao = posicao + velocidade * dt


# ==========================================
# TRANSFORMAR LISTAS EM ARRAYS
# ==========================================

trajetoria = np.array(trajetoria)
distancias = np.array(distancias)

# ==========================================
# CÁLCULOS DA ÓRBITA
# ==========================================

distancia_minima = np.min(distancias)
distancia_maxima = np.max(distancias)

# Semieixo maior aproximado
a = (
    distancia_maxima + distancia_minima
) / 2

# Excentricidade aproximada
e = (
    distancia_maxima - distancia_minima
) / (
    distancia_maxima + distancia_minima
)

# ==========================================
# MOSTRAR RESULTADOS
# ==========================================

print()
print("=" * 60)
print("1ª LEI DE KEPLER - ÓRBITA ELÍPTICA")
print("=" * 60)

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
    f"Semieixo maior aproximado: "
    f"{a:.3e} m"
)

print(
    f"Excentricidade aproximada: "
    f"{e:.4f}"
)

print()
print("=" * 60)

# ==========================================
# GRÁFICO DA ÓRBITA
# ==========================================

plt.figure(figsize=(8, 8))

plt.plot(
    trajetoria[:, 0],
    trajetoria[:, 1],
    label="Órbita simulada"
)

# Sol na origem
plt.scatter(
    0,
    0,
    s=150,
    label="Sol"
)

plt.xlabel("Posição x (m)")
plt.ylabel("Posição y (m)")

plt.title(
    "1ª Lei de Kepler - Órbita Elíptica"
)

plt.axis("equal")
plt.grid()
plt.legend()

plt.savefig(
    "primeira_lei_kepler.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
