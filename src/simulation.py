import segyio
import pysit
from pysit.gallery import horizontal_reflector
from pysit import *

def carregar_dados_segy(caminho_arquivo):
    """
    Carrega dados SEG-Y usando segyio.
    """
    with segyio.open(caminho_arquivo, "r", ignore_geometry=True) as f:
        data = segyio.tools.cube(f)
    return data

def configurar_simulacao():
    """
    Configura a simulação usando PySIT.
    """
    domain, m = horizontal_reflector()
    shots = equispaced_acquisition(
        domain, RickerWavelet(25.0), sources=5, receivers=101, seed=10
    )
    solver = ConstantDensityAcousticWave(domain, m)
    solver.model_parameters = ModelParameters(domain, m)
    solver.data_model = shots
    return solver

def realizar_simulacao(solver):
    """
    Realiza a simulação e retorna os campos de onda.
    """
    wavefields = solver.compute_shotgathers()
    return wavefields
