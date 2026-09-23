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

distancia_terra = 1.496e11

posicao_inicial = np.array([
    distancia_terra,
    0.0
])

velocidade_inicial = np.array([
    0.0,
    29_780.0
])

# ==========================================
# CONFIGURAÇÃO DOS EXPERIMENTOS
# ==========================================

passos = [
    1 * 60 * 60,       # 1 hora
    6 * 60 * 60,       # 6 horas
    12 * 60 * 60,      # 12 horas
    24 * 60 * 60       # 24 horas
]

nomes_passos = [
    "1 hora",
    "6 horas",
    "12 horas",
    "24 horas"
]

# Tempo total: 1 ano
tempo_total = 365 * 24 * 60 * 60

# ==========================================
# ARMAZENAR RESULTADOS
# ==========================================

resultados = []

# ==========================================
# EXECUTAR OS EXPERIMENTOS
# ==========================================

for dt, nome in zip(passos, nomes_passos):

    # Número de passos da simulação
    numero_passos = int(tempo_total / dt)

    # Reinicia as condições iniciais
    posicao = posicao_inicial.copy()
    velocidade = velocidade_inicial.copy()

    # Lista para armazenar distâncias
    distancias = []

    # ======================================
    # SIMULAÇÃO PELO MÉTODO DE EULER EXPLÍCITO
    # ======================================

    for i in range(numero_passos):

        # Distância da Terra ao Sol
        r = np.linalg.norm(posicao)

        # Guarda a distância
        distancias.append(r)

        # Calcula a aceleração gravitacional
        aceleracao = -G * M_sol * posicao / r**3

        # ==================================
        # MÉTODO DE EULER EXPLÍCITO
        # ==================================

        nova_posicao = posicao + velocidade * dt
        nova_velocidade = velocidade + aceleracao * dt

        posicao = nova_posicao
        velocidade = nova_velocidade

    # ======================================
    # CALCULAR RESULTADOS
    # ======================================

    distancia_minima = np.min(distancias)
    distancia_maxima = np.max(distancias)

    variacao = distancia_maxima - distancia_minima

    # Guarda os resultados
    resultados.append({
        "passo": nome,
        "minima": distancia_minima,
        "maxima": distancia_maxima,
        "variacao": variacao
    })


# ==========================================
# MOSTRAR RESULTADOS
# ==========================================

print()
print("=" * 70)
print("RESULTADOS DOS EXPERIMENTOS - MÉTODO DE EULER EXPLÍCITO")
print("=" * 70)

for resultado in resultados:

    print()
    print(f"Passo de tempo: {resultado['passo']}")

    print(
        f"Distância mínima: "
        f"{resultado['minima']:.3e} m"
    )

    print(
        f"Distância máxima: "
        f"{resultado['maxima']:.3e} m"
    )

    print(
        f"Variação: "
        f"{resultado['variacao']:.3e} m"
    )

print()
print("=" * 70)


# ==========================================
# GRÁFICO DA VARIAÇÃO
# ==========================================

nomes = [r["passo"] for r in resultados]

variacoes = [
    r["variacao"]
    for r in resultados
]

plt.figure(figsize=(9, 6))

plt.bar(nomes, variacoes)

plt.xlabel("Passo de tempo")
plt.ylabel("Variação da distância (m)")

plt.title(
    "Influência do Passo de Tempo "
    "no Método de Euler Explícito"
)

plt.grid(axis="y")

plt.show()
