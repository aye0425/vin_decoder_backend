from importlib.metadata import entry_points
from setuptools import setup, find_packages

long_description = open('README.md').read()

with open('requirements.txt') as f:
  requirements = f.read().splitlines()

setup(
  name='vin_decoder_backend',
  version='1.0.0',
  install_requires=requirements,
  python_requires = '>=3.8.13'
  description='vin decoder backend server',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author='Andy Ye',
  author_email='awye0425@gmail.com',
  packages=find_packages(),
  url = 'https://github.com/',
  license=license,
  entry_points = {'console_scripts' = ['decode_vin = python -m app.main']},
)