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
# CONDIÇÕES INICIAIS - PERIÉLIO
# ==========================================

# Distância de Mercúrio ao Sol no periélio
r_perielio = a_real * (1 - e_real)

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
# PERÍODO TEÓRICO - 3ª LEI DE KEPLER
# ==========================================

periodo_teorico = (
    2
    * np.pi
    * np.sqrt(
        a_real**3 / MU_SOL
    )
)

# Converter de segundos para dias
periodo_teorico_dias = (
    periodo_teorico
    / (24 * 60 * 60)
)

# ==========================================
# CONFIGURAÇÃO DA SIMULAÇÃO
# ==========================================

# Passo de tempo: 1 hora
dt = 60 * 60

# Mercúrio leva aproximadamente 88 dias
# para completar uma órbita.
# Usamos 100 dias para garantir a detecção.
tempo_total = (
    100 * 24 * 60 * 60
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

    # Distância Mercúrio-Sol
    r = np.linalg.norm(
        posicao
    )

    # Aceleração gravitacional
    aceleracao = (
        -MU_SOL
        * posicao
        / r**3
    )

    # ======================================
    # EULER-CROMER
    # ======================================

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

    # Mercúrio começa no eixo x positivo.
    #
    # Após uma volta completa, cruza
    # novamente o eixo x positivo,
    # passando de y negativo para y positivo.

    if (
        posicao[1] < 0
        and nova_posicao[1] >= 0
        and nova_posicao[0] > 0
    ):

        # Interpolação para estimar
        # com maior precisão o instante
        # em que ocorreu o cruzamento.

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
# DIFERENÇA ENTRE OS PERÍODOS
# ==========================================

diferenca_segundos = abs(
    periodo_simulado
    - periodo_teorico
)

diferenca_horas = (
    diferenca_segundos
    / 3600
)

# ==========================================
# ERRO PERCENTUAL
# ==========================================

erro_percentual = (
    diferenca_segundos
    / periodo_teorico
    * 100
)

# ==========================================
# MOSTRAR RESULTADOS
# ==========================================

print()

print("=" * 65)

print(
    "3ª LEI DE KEPLER - MERCÚRIO"
)

print("=" * 65)

print()

print("VALORES DE REFERÊNCIA:")

print()

print(
    f"Semieixo maior: "
    f"{a_real:.3e} m"
)

print(
    f"Excentricidade: "
    f"{e_real:.8f}"
)

print()

print("RESULTADOS:")

print()

print(
    f"Período teórico: "
    f"{periodo_teorico_dias:.6f} dias"
)

print(
    f"Período simulado: "
    f"{periodo_simulado_dias:.6f} dias"
)

print(
    f"Diferença: "
    f"{diferenca_horas:.6f} horas"
)

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
    "3ª Lei de Kepler - Mercúrio\n"
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
    "terceira_lei_mercurio.png",
    dpi=300,
    bbox_inches="tight"
)

# ==========================================
# EXIBIR
# ==========================================

plt.show()
