import numpy as np
from fatiando import mesher
from fatiando.vis import mpl

def criar_modelo_velocidade(area, shape, velocidade):
    """
    Cria um modelo de velocidade simples.
    """
    model = mesher.SquareMesh(area, shape)
    model.addprop('vp', np.full(shape, velocidade))
    return model

def visualizar_modelo(model):
    """
    Visualiza o modelo de velocidade.
    """
    mpl.figure()
    mpl.title("Modelo de Velocidade")
    mpl.squares(model, prop='vp', cmap='jet')
    mpl.colorbar()
    mpl.show()
