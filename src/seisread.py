from obspy.io.segy.segy import _read_segy

def ler_dados_segy(caminho_arquivo):
    """
    Lê um arquivo SEG-Y e retorna o stream de dados.
    """
    stream = _read_segy(caminho_arquivo)
    return stream
