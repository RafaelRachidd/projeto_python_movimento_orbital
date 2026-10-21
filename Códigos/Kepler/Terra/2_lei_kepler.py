import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# CONSTANTES ASTRONÔMICAS
# ==========================================

MU_SOL = 1.32712440041279419e20
UA = 149_597_870_700.0

# ==========================================
# ELEMENTOS ORBITAIS DA TERRA
# ==========================================

a_real = 1.00000011 * UA
e_real = 0.01671022

# ==========================================
# CONDIÇÕES INICIAIS - PERIÉLIO
# ==========================================

r_perielio = a_real * (1 - e_real)

v_perielio = np.sqrt(
    MU_SOL * (
        2 / r_perielio
        - 1 / a_real
    )
)

posicao = np.array([
    r_perielio,
    0.0
])

velocidade = np.array([
    0.0,
    v_perielio
])

# ==========================================
# CONFIGURAÇÃO DA SIMULAÇÃO
# ==========================================

dt = 60 * 60  # 1 hora

tempo_total = (
    366 * 24 * 60 * 60
)

numero_passos = int(
    tempo_total / dt
)

# ==========================================
# ARMAZENAMENTO
# ==========================================

trajetoria = []
velocidades = []
distancias = []

# ==========================================
# SIMULAÇÃO - EULER-CROMER
# ==========================================

for i in range(numero_passos):

    trajetoria.append(
        posicao.copy()
    )

    velocidades.append(
        velocidade.copy()
    )

    # Distância Terra-Sol
    r = np.linalg.norm(
        posicao
    )

    distancias.append(r)

    # Aceleração gravitacional
    aceleracao = (
        -MU_SOL
        * posicao
        / r**3
    )

    # Método de Euler-Cromer
    velocidade = (
        velocidade
        + aceleracao * dt
    )

    posicao = (
        posicao
        + velocidade * dt
    )

# ==========================================
# TRANSFORMAR LISTAS EM ARRAYS
# ==========================================

trajetoria = np.array(
    trajetoria
)

velocidades = np.array(
    velocidades
)

distancias = np.array(
    distancias
)

# ==========================================
# LOCALIZAR O AFÉLIO
# ==========================================

indice_afelio = np.argmax(
    distancias
)

# ==========================================
# INTERVALO ANALISADO
# ==========================================

dias_intervalo = 30

passos_intervalo = int(
    dias_intervalo
    * 24
    * 60
    * 60
    / dt
)

# ==========================================
# FUNÇÃO PARA CALCULAR A ÁREA VARRIDA
# ==========================================

def calcular_area(inicio, fim):

    area = 0.0

    for i in range(inicio, fim - 1):

        x1 = trajetoria[i][0]
        y1 = trajetoria[i][1]

        x2 = trajetoria[i + 1][0]
        y2 = trajetoria[i + 1][1]

        # Área do pequeno triângulo
        area_triangulo = (
            0.5
            * abs(
                x1 * y2
                - y1 * x2
            )
        )

        area += area_triangulo

    return area


# ==========================================
# INTERVALO APÓS O PERIÉLIO
# ==========================================

inicio_perielio = 0

fim_perielio = (
    inicio_perielio
    + passos_intervalo
)

area_perielio = calcular_area(
    inicio_perielio,
    fim_perielio
)

# ==========================================
# INTERVALO APÓS O AFÉLIO
# ==========================================

inicio_afelio = indice_afelio

fim_afelio = (
    inicio_afelio
    + passos_intervalo
)

area_afelio = calcular_area(
    inicio_afelio,
    fim_afelio
)

# ==========================================
# CALCULAR VELOCIDADES MÉDIAS
# ==========================================

modulos_velocidade = np.linalg.norm(
    velocidades,
    axis=1
)

velocidade_media_perielio = np.mean(
    modulos_velocidade[
        inicio_perielio:fim_perielio
    ]
)

velocidade_media_afelio = np.mean(
    modulos_velocidade[
        inicio_afelio:fim_afelio
    ]
)

# ==========================================
# DIFERENÇA PERCENTUAL ENTRE AS ÁREAS
# ==========================================

diferenca_percentual = (
    abs(
        area_perielio
        - area_afelio
    )
    / area_perielio
    * 100
)

# ==========================================
# MOSTRAR RESULTADOS
# ==========================================

print()
print("=" * 65)
print("2ª LEI DE KEPLER - ÁREAS IGUAIS EM TEMPOS IGUAIS")
print("=" * 65)

print()

print(
    f"Intervalo analisado: "
    f"{dias_intervalo} dias"
)

print()

print("APÓS O PERIÉLIO:")

print(
    f"Área varrida: "
    f"{area_perielio:.5e} m²"
)

print(
    f"Velocidade média: "
    f"{velocidade_media_perielio / 1000:.3f} km/s"
)

print()

print("APÓS O AFÉLIO:")

print(
    f"Área varrida: "
    f"{area_afelio:.5e} m²"
)

print(
    f"Velocidade média: "
    f"{velocidade_media_afelio / 1000:.3f} km/s"
)

print()

print(
    f"Diferença percentual entre as áreas: "
    f"{diferenca_percentual:.6f}%"
)

print()
print("=" * 65)

# ==========================================
# GRÁFICO
# ==========================================

plt.figure(
    figsize=(10, 8)
)

# Órbita completa
plt.plot(
    trajetoria[:, 0],
    trajetoria[:, 1],
    label="Órbita da Terra"
)

# Sol
plt.scatter(
    0,
    0,
    s=150,
    label="Sol"
)

# ==========================================
# ÁREA DOS 30 DIAS APÓS O PERIÉLIO
# ==========================================

x_perielio = np.concatenate((
    [0],
    trajetoria[
        inicio_perielio:fim_perielio,
        0
    ],
    [0]
))

y_perielio = np.concatenate((
    [0],
    trajetoria[
        inicio_perielio:fim_perielio,
        1
    ],
    [0]
))

plt.fill(
    x_perielio,
    y_perielio,
    alpha=0.4,
    label="30 dias após o periélio"
)

# ==========================================
# ÁREA DOS 30 DIAS APÓS O AFÉLIO
# ==========================================

x_afelio = np.concatenate((
    [0],
    trajetoria[
        inicio_afelio:fim_afelio,
        0
    ],
    [0]
))

y_afelio = np.concatenate((
    [0],
    trajetoria[
        inicio_afelio:fim_afelio,
        1
    ],
    [0]
))

plt.fill(
    x_afelio,
    y_afelio,
    alpha=0.4,
    label="30 dias após o afélio"
)

# ==========================================
# PERSONALIZAÇÃO
# ==========================================

plt.xlabel(
    "Posição x (m)"
)

plt.ylabel(
    "Posição y (m)"
)

plt.title(
    "2ª Lei de Kepler - Áreas Iguais em Tempos Iguais"
)

plt.axis("equal")

plt.grid()

# Legenda fora do gráfico
plt.legend(
    loc="center left",
    bbox_to_anchor=(1.02, 0.5)
)

# Ajusta o espaço automaticamente
plt.tight_layout()

# ==========================================
# SALVAR GRÁFICO
# ==========================================

plt.savefig(
    "segunda_lei_kepler.png",
    dpi=300,
    bbox_inches="tight"
)

# ==========================================
# EXIBIR GRÁFICO
# ==========================================

plt.show()
