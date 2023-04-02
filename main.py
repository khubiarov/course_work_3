import json
from utils import sort_func
from utils import executed_data


def file_open():
    '''открывает файл , переделывает в формат пайтоновского словаря в списке, цикл выводит данные из executed_data'''
    with open('operations.json', 'rt', encoding='utf-8') as file:
        content = file.read()

        content = sort_func(json.loads(content))

    for i in range(5):
        print(executed_data(content[i]))

print('\n')

file_open()



