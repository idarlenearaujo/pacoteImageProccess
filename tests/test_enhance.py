from image_processing.utils import load_image
import unittest
import image_processing.processing as img
import os


class TestEnhance(unittest.TestCase):

    ''' Teste para funções de melhoria de imagem '''

    @classmethod
    def setUp(cls):
        '''Configuração inicial para todos os testes.'''
        cls.image_path = 'tests/img/img.jpeg'
        cls.output_path = 'tests/img/img_melhorada.jpeg'
        cls.image = load_image(cls.image_path)
        assert cls.image is not None, "Falha ao carregar a imagem de teste."

    def test_improve_lighting(self):
        '''Teste para a função de melhoria de iluminação.'''
        result = img.improve_lighting(self.image_path, self.output_path)
        self.assertIsNotNone(result)
        self.assertTrue(os.path.exists(self.output_path))

    def test_improve_contrast(self):
        '''Teste para a função de melhoria de contraste.'''
        result = img.improve_contrast(self.image_path, self.output_path)
        self.assertIsNotNone(result)
        self.assertTrue(os.path.exists(self.output_path))

    def test_improve_noise(self):
        '''Teste para a função de redução de ruído.'''
        result = img.reduce_noise(self.image_path, self.output_path)
        self.assertIsNotNone(result)
        self.assertTrue(os.path.exists(self.output_path))

    def test_improve_saturation(self):
        '''Teste para a função de melhoria de saturação.'''
        result = img.improve_saturation(self.image_path, self.output_path)
        self.assertIsNotNone(result)
        self.assertTrue(os.path.exists(self.output_path))

    def test_improve_sharpen(self):
        '''Teste para a função de nitidez.'''
        result = img.sharpen_image(self.image_path, self.output_path)
        self.assertIsNotNone(result)
        self.assertTrue(os.path.exists(self.output_path))

    def test_improve_color(self):
        '''Teste para a função de correção de cor.'''
        result = img.correct_color(self.image_path, self.output_path)
        self.assertIsNotNone(result)
        self.assertTrue(os.path.exists(self.output_path))

    @classmethod
    def tearDown(cls):
        '''Limpeza após todos os testes.'''
        if os.path.exists(cls.output_path):
            os.remove(cls.output_path)


if __name__ == '__main__':
    unittest.main()
