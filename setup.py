from setuptools import setup, find_packages

setup(
    name='Naver Series module',
    version='1.0.0 Alpha',

    author='EGGnmad',
    author_email='viewnono1219@gmail.com',

    packages=find_packages(),

    requires=['requests', 'beautifulsoup4']
)