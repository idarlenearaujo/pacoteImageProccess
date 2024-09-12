from image_processing.utils import load_image, save_image
import unittest
import os
import numpy as np


class TestIO(unittest.TestCase):
    '''Testes para as funções de entrada e saída de imagem'''

    @classmethod
    def setUpClass(cls):
        '''Configuração inicial para todos os testes'''
        cls.image_path = 'tests/img/img.jpeg'
        cls.output_path = 'tests/img/test_output.jpeg'

    def test_load_image_success(self):
        '''Teste para carregar a imagem existente'''
        image = load_image(self.image_path)
        self.assertIsNotNone(image)
        self.assertIsInstance(image, np.ndarray)

    def test_save_image_success(self):
        '''Teste para salvar a imagem corretamente'''
        image = load_image(self.image_path)
        save_image(image, self.output_path)
        self.assertTrue(os.path.exists(self.output_path))

    def test_save_image_failure(self):
        '''Teste para salvar um objeto que não é uma imagem'''
        with self.assertRaises(TypeError):
            save_image('not_an_image', self.output_path)

    @classmethod
    def tearDownClass(cls):
        '''Limpeza após os testes'''
        if os.path.exists(cls.output_path):
            os.remove(cls.output_path)


if __name__ == '__main__':
    unittest.main()
