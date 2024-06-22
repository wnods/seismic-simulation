from src.seisread import ler_dados_segy
from src.processingseis import preprocessar_dados
from src.simple_model_velocity import criar_modelo_velocidade, visualizar_modelo
from src.simulation import carregar_dados_segy, configurar_simulacao, realizar_simulacao
from src.view import visualizar_resultados

def main():
    arquivo_segy = "data/segy_ativa/3.SGY"

    # Ler e interpretar dados SEG-Y
    stream = ler_dados_segy(arquivo_segy)
    print(stream)

    # Pré-processar os dados
    stream_filtrado = preprocessar_dados(stream, freqmin=1.0, freqmax=20.0)

    # Criar e visualizar modelo de velocidade
    area = (0, 10000, 0, 10000)
    shape = (50, 50)
    velocidade = 1500.0
    modelo = criar_modelo_velocidade(area, shape, velocidade)
    visualizar_modelo(modelo)

    # Carregar dados SEG-Y e configurar a simulação
    dados_segy = carregar_dados_segy(arquivo_segy)
    solver = configurar_simulacao()

    # Realizar simulação e visualizar resultados
    wavefields = realizar_simulacao(solver)
    visualizar_resultados(wavefields)

if __name__ == "__main__":
    main()
