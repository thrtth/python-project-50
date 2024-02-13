### Hexlet tests and linter status:
[![Actions Status](https://github.com/thrtth/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/thrtth/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/040490f2dab482c31015/maintainability)](https://codeclimate.com/github/thrtth/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/040490f2dab482c31015/test_coverage)](https://codeclimate.com/github/thrtth/python-project-50/test_coverage)  


### Gendiff

Сравнивает два конфигурационных файла и показывает различия

### Requirements

python 3.10  
pytest 8.0.0  
pytest-cov 4.1.0  
PyYAML 6.0.1  

### Installation

make install  
make build  
make publish  
make package-install

### Run

Запуск из консоли: gendiff -f <format> <path to file 1> <path to file 2>  
format может быть stylish, plain или json (по умолчанию stylish)  
Принимаются файлы json и yaml  
Пример: gendiff -f plain file1.json file2.json

### Asciinema records:

Запуск функции generate_diff()  
[![asciicast](https://asciinema.org/a/HC2aNP0kKnQZ88okOknax9t23.svg)](https://asciinema.org/a/HC2aNP0kKnQZ88okOknax9t23)  
Запуск gendiff с плоскими файлами yaml и json  
[![asciicast](https://asciinema.org/a/NRwzAh29SpnoY4zTHcZrpJcvr.svg)](https://asciinema.org/a/NRwzAh29SpnoY4zTHcZrpJcvr)  
Запуск gendiff с файлами yaml и json  
[![asciicast](https://asciinema.org/a/D8Us7YM60JaX8oMolj9BU9cSs.svg)](https://asciinema.org/a/D8Us7YM60JaX8oMolj9BU9cSs)  
Запуск gendiff с файлами yaml и json в формате вывода plain  
[![asciicast](https://asciinema.org/a/TjuXoTgb8GY5wUiqYHNXCXpq5.svg)](https://asciinema.org/a/TjuXoTgb8GY5wUiqYHNXCXpq5)  
Запуск gendiff с файлами yaml и json в формате вывода json  
[![asciicast](https://asciinema.org/a/X8uKrTpzONHo2jZ3u7kTqNxwi.svg)](https://asciinema.org/a/X8uKrTpzONHo2jZ3u7kTqNxwi)  