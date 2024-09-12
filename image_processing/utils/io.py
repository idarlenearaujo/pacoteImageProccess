import cv2
import numpy as np


def load_image(image_path):
    """Carrega uma imagem a partir de um caminho especificado"""
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Imagem não encontrada: {image_path}")

    return image


def save_image(image, output_path):
    """Salva uma imagem no caminho especificado."""

    if not isinstance(image, np.ndarray):
        raise TypeError("A imagem a ser salva não é um array numpy.")

    success = cv2.imwrite(output_path, image)
    if not success:
        raise IOError(f'Falha ao salvar a imagem em {output_path}')

    return success
