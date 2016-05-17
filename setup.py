from setuptools import setup, find_packages

setup(
    name = 'ct-rest',
    version = '0.1',
    keywords = ('django', 'ctcloud', 'rest'),
    description = 'a rest utils for ctcloud using Django',
    license = 'MIT License',
    install_requires = ['Django>=1.8'],

    author = 'Wang Yonggang',
    author_email = 'i@ysgh.net',
    
    packages = find_packages(),
    platforms = 'any',
)