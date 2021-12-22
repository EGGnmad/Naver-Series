from setuptools import setup, find_packages

setup(
    name='Naver Series module',
    version='1.0.0 Alpha',
    description='Naver Series module',

    author='EGGnmad',
    author_email='viewnono1219@gmail.com',
    url='https://github.com/EGGnmad/NaverSeries',

    packages=find_packages(),

    requires=['requests', 'beautifulsoup4']
)