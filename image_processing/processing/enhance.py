from image_processing.utils.io import load_image, save_image
import cv2
import numpy as np


def verifica_image(image, image_path):
    '''Função que verifica se a imagem existe em tal caminho indicado'''
    if image is None:
        raise ValueError(f'Falha ao carregar a imagem de {image_path}')


def improve_lighting(image_path, output_path):
    '''Função que ajusta a luminosidade com o método CLAHE'''
    image = load_image(image_path)
    verifica_image(image, image_path)

    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl, a, b))
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    save_image(final, output_path)
    return final


def improve_contrast(image_path, output_path):
    '''Função que aumenta o contraste de forma natural com o opencv'''
    image = load_image(image_path)
    verifica_image(image, image_path)

    alpha = 1.2  # Reduzido para um ajuste mais natural
    beta = 10    # Ajuste leve no brilho
    adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    save_image(adjusted, output_path)
    return adjusted


def improve_saturation(image_path, output_path):
    '''Função que aumenta a saturação das cores das imagens com o opencv'''
    image = load_image(image_path)
    verifica_image(image, image_path)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv[..., 1] = hsv[..., 1] * 1.1  # Ajuste leve na saturação
    adjusted = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    save_image(adjusted, output_path)
    return adjusted


def reduce_noise(image_path, output_path):
    '''Função que aplica um filtro gaussiano com o opencv'''
    image = load_image(image_path)
    verifica_image(image, image_path)

    blurred = cv2.GaussianBlur(image, (3, 3), 0)
    save_image(blurred, output_path)
    return blurred


def sharpen_image(image_path, output_path):
    '''Função que aplica um realçador de contornos'''
    image = load_image(image_path)
    verifica_image(image, image_path)

    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened = cv2.filter2D(image, -1, kernel)
    save_image(sharpened, output_path)
    return sharpened


def correct_color(image_path, output_path):
    '''Função de estilizar imagem para preto e branco'''
    image = load_image(image_path)
    verifica_image(image, image_path)

    result = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    save_image(result, output_path)
    return result
