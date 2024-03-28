from setuptools import setup, find_packages

setup(
    name='tiny-torch-utils',
    version='0.1',
    packages=find_packages(),
    description='A brief description of what the package does',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Chainathan',
    install_requires=[
    'torch',
    'matplotlib',
    'numpy',
    'fastcore',
    'fastprogress',
    'torcheval',
    ],
    python_requires='>=3.6',
)
