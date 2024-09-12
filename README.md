# image_processing

## Descrição

Este pacote oferece uma série de filtros de imagem que permitem melhorar a qualidade das imagens de diversas formas. As funcionalidades incluem melhorias de luminosidade, contraste, saturação, redução de ruído, nitidez e correção de cor. Ideal para fotógrafos, designers e desenvolvedores que precisam de uma ferramenta eficiente para processamento de imagens.

## Funcionalidades

### Módulo *processing*:

-   **improve_lighting**: Ajusta a luminosidade da imagem utilizando o método CLAHE (Contrast Limited Adaptive Histogram Equalization), que melhora os detalhes em áreas escuras sem saturar as áreas claras.

```python
from image_processing.processing.enhance import improve_lighting

improve_lighting('caminho/para/imagem.jpg', 'caminho/para/imagem_melhorada.jpg')
```

-   **improve_contrast**: Aumenta o contraste da imagem de forma natural, ajustando os valores de brilho e contraste para realçar os detalhes.

```python
from image_processing.processing.enhance import improve_contrast

improve_contrast('caminho/para/imagem.jpg', 'caminho/para/imagem_melhorada.jpg')
```

-   **improve_saturation**: Aumenta a saturação das cores na imagem, tornando-as mais vibrantes e vivas.


```python
from image_processing.processing.enhance import improve_saturation

improve_saturation('caminho/para/imagem.jpg', 'caminho/para/imagem_melhorada.jpg')
```

-   **reduce_noise**: Aplica um filtro de desfoque gaussiano para reduzir o ruído na imagem, resultando em uma aparência mais suave.


```python
from image_processing.processing.enhance import reduce_noise

reduce_noise('caminho/para/imagem.jpg', 'caminho/para/imagem_melhorada.jpg')
```

-   **sharpen_image**: Aplica um filtro que realça os contornos e detalhes da imagem, tornando-as mais nítidas.


```python
from image_processing.processing.enhance import sharpen_image

sharpen_image('caminho/para/imagem.jpg', 'caminho/para/imagem_melhorada.jpg')
```

-   **correct_color**: Converte a imagem para preto e branco, útil para criar efeitos artísticos ou preparar imagens para processamento adicional.


```python
from image_processing.processing.enhance import correct_color

correct_color('caminho/para/imagem.jpg', 'caminho/para/imagem_melhorada.jpg')
```
    
### Módulo *utils*:
        
-   **load_image**: É feito o carregamento da imagem para um caminho especificado.

```python
from image_processing.utils.io import load_image

image = load_image('caminho/para/imagem.jpg')
```

-   **save_image**: Onde é salvo a nova imagem em um caminho especificado.

```python
from image_processing.utils.io import save_image

save_image(image, 'caminho/para/imagem_salva.jpg')

```

## Estrutura do projeto

A estrutura do projeto é organizada da seguinte forma:

```
image_processing/
├── processing/ 
│ ├── init.py 
│ ├── enhance.py 
├── utils/ 
│ ├── init.py 
│ ├── io.py 
├── tests/
│ ├── img
│ │ ├──img.JPEG
│ ├── test_enhance.py
│ ├── test_io.py  
├── init.py 
├── setup.py 
├── README.md 
├── requirements.txt
```

## Dependências

As dependências estão listadas no arquivo `requirements.txt` e incluem:

-   `opencv-python`
-   `numpy`

Para instalar as dependências, execute:

```bash
pip install -r requirements.txt
```

## Instalação

Para instalar o pacote, você pode usar o pip:


```bash
pip install image_processing
```

## Uso

```python
from image_processing.processing.enhance import improve_lighting, improve_contrast, improve_saturation, reduce_noise, sharpen_image, correct_color
```

ou

```python
import image_processing.processing.enhance
```

## Contribuição

Se você quiser contribuir para o desenvolvimento deste pacote, siga estas etapas:

1.  Faça um fork do repositório
2.  Crie uma nova branch (```git checkout -b feature/nova-feature```)
3.  Faça commit das suas mudanças (```git commit -am 'Adiciona nova feature x'```)
4.  Faça push para a branch (```git push origin feature/nova-feature```)
5.  Abra um Pull Request


## Autor

Idarlene Araujo
