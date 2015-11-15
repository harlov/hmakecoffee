import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='hmakecoffee', #Название пакета
    version='1.0.0', #версия
    packages=find_packages(), # входящие в состав модуля пакеты - отдаем на откуп хелпера find_packages
    include_package_data=True,
    license='MTI License', #Указываем выбранную лицензию
    description='test funny python packet', #краткое описание пакета
    long_description=README, #полное описание пакета - копируем, из файла README.md
    url='https://github.com/harlov/hmakecoffee', # домашняя страница пакета - пока оставим адрес репозитория.
    download_url = 'https://github.com/harlov/hmakecoffee/tarball/1.0.0', # адрес для скачивания пакета
    author='Nikita Harlov', 
    author_email='nikita@harlov.com',
    classifiers=[ 
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Education'
    ],

    #для удобства использования , забиндим вызов сервиса на комманду hmakecoffee-cli
    entry_points={'console_scripts': [
        'hmakecoffee-cli = hmakecoffee.__main__:main'
        ],
    },
)