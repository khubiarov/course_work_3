from datetime import date


def sort_func(content):
    """Сортирует по дате в оьратном порядке"""
    executed = []
    for cell in content:
        if cell.get("state") == 'EXECUTED':
            executed.append(cell)
    executed.sort(key=lambda x: x.get('date'), reverse=True)
    return executed


def executed_data(executed):
    """формирует конечный вид для главного цикла, есть условия из-за
    оссобености устройства словаря, (есть пустые словарики) и вызывает choose_format для выбора оформления номера"""


    date_correct = date_correct_format(executed.get('date'))
    description = executed.get('description')
    source = executed.get('from')
    purpose = executed.get('to')
    summ = executed.get('operationAmount').get('amount')
    currency = executed.get('operationAmount').get('currency').get('name')
    if source is None:
        source = ''
        stripe = ""
    else:
        source = choose_format(source)
        stripe = ' -> '


    return f'{date_correct} {description}\n{source}{stripe}{choose_format(purpose)}\n{summ} {currency}\n'


def date_correct_format(date_before_refactor):
    '''меняет формат даты с пайтоновского на тот, который требуется в условиях'''
    check_time = date.fromisoformat(date_before_refactor[0:10])
    return f'{check_time.day}.{check_time.month}.{check_time.year}'


def choose_format(source):
    '''Выбирает формат номера карты или счета '''
    letters = []
    digit = []

    for letter in source:
        if letter.isalpha():
            letters.append(letter)
        elif letter.isdigit():

            digit.append(letter)

        else:
            letters.append(letter)
    #print(letters)

    if "".join(letters) == "Счет ":
        return f'{"".join(letters)}**{"".join(digit[-4:])}'
    else:
        return f'{"".join(letters)}{"".join(digit[0:4])} {"".join(digit[4:6])}** **** {"".join(digit[-4:])}'