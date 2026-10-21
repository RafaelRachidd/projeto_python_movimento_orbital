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
# PERÍODO TEÓRICO - 3ª LEI DE KEPLER
# ==========================================

periodo_teorico = (
    2
    * np.pi
    * np.sqrt(
        a_real**3 / MU_SOL
    )
)

periodo_teorico_dias = (
    periodo_teorico
    / (24 * 60 * 60)
)

# ==========================================
# CONFIGURAÇÃO DA SIMULAÇÃO
# ==========================================

dt = 60 * 60  # 1 hora

# Usamos 400 dias para garantir
# que uma órbita completa seja detectada
tempo_total = (
    400 * 24 * 60 * 60
)

numero_passos = int(
    tempo_total / dt
)

# ==========================================
# ARMAZENAMENTO
# ==========================================

trajetoria = []

tempo = 0.0

periodo_simulado = None

# ==========================================
# SIMULAÇÃO - EULER-CROMER
# ==========================================

for i in range(numero_passos):

    trajetoria.append(
        posicao.copy()
    )

    # Distância Terra-Sol
    r = np.linalg.norm(
        posicao
    )

    # Aceleração gravitacional
    aceleracao = (
        -MU_SOL
        * posicao
        / r**3
    )

    # Euler-Cromer
    nova_velocidade = (
        velocidade
        + aceleracao * dt
    )

    nova_posicao = (
        posicao
        + nova_velocidade * dt
    )

    novo_tempo = (
        tempo + dt
    )

    # ======================================
    # DETECTAR UMA VOLTA COMPLETA
    # ======================================

    # A Terra começou no eixo x positivo.
    #
    # Depois de uma órbita completa,
    # ela cruza novamente o eixo x positivo,
    # passando de y negativo para y positivo.

    if (
        posicao[1] < 0
        and nova_posicao[1] >= 0
        and nova_posicao[0] > 0
    ):

        # Interpolação para estimar
        # o instante exato do cruzamento

        fracao = (
            -posicao[1]
            / (
                nova_posicao[1]
                - posicao[1]
            )
        )

        periodo_simulado = (
            tempo
            + fracao * dt
        )

        break

    # Atualiza os valores
    posicao = nova_posicao
    velocidade = nova_velocidade
    tempo = novo_tempo

# ==========================================
# TRANSFORMAR TRAJETÓRIA EM ARRAY
# ==========================================

trajetoria = np.array(
    trajetoria
)

# ==========================================
# CONVERTER PERÍODO SIMULADO PARA DIAS
# ==========================================

periodo_simulado_dias = (
    periodo_simulado
    / (24 * 60 * 60)
)

# ==========================================
# CALCULAR ERRO PERCENTUAL
# ==========================================

erro_percentual = (
    abs(
        periodo_simulado
        - periodo_teorico
    )
    / periodo_teorico
    * 100
)

# ==========================================
# MOSTRAR RESULTADOS
# ==========================================

print()
print("=" * 65)

print(
    "3ª LEI DE KEPLER - "
    "PERÍODO ORBITAL"
)

print("=" * 65)

print()

print(
    f"Semieixo maior: "
    f"{a_real:.3e} m"
)

print()

print(
    f"Período teórico: "
    f"{periodo_teorico_dias:.6f} dias"
)

print(
    f"Período simulado: "
    f"{periodo_simulado_dias:.6f} dias"
)

print()

print(
    f"Erro percentual: "
    f"{erro_percentual:.6f}%"
)

print()

print("=" * 65)

# ==========================================
# GRÁFICO COMPARATIVO
# ==========================================

nomes = [
    "Teórico",
    "Simulado"
]

periodos = [
    periodo_teorico_dias,
    periodo_simulado_dias
]

plt.figure(
    figsize=(7, 6)
)

barras = plt.bar(
    nomes,
    periodos
)

plt.ylabel(
    "Período orbital (dias)"
)

plt.title(
    "3ª Lei de Kepler - "
    "Período Teórico e Simulado"
)

plt.grid(
    axis="y"
)

# ==========================================
# VALORES SOBRE AS BARRAS
# ==========================================

for barra, valor in zip(
    barras,
    periodos
):

    plt.text(
        barra.get_x()
        + barra.get_width() / 2,

        barra.get_height(),

        f"{valor:.3f} dias",

        ha="center",
        va="bottom"
    )

plt.tight_layout()

# ==========================================
# SALVAR GRÁFICO
# ==========================================

plt.savefig(
    "terceira_lei_kepler.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
