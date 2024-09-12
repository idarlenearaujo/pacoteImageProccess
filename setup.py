from setuptools import setup, find_packages


with open('README.md', 'r') as f:
    page_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='image_processing',
    version='0.0.1',
    author='idarlene',
    description='Alguns filtros de imagem',
    long_description=page_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'image_processing=image_processing.enhance:main'
            ],
    },
)
