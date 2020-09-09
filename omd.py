# Lukovsky Vsevolod

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    else:
        return step2_no_umbrella()


def step2_umbrella():
    print('Зонтик у утки. Полетели!')
    return 0

def step2_no_umbrella():
    print('Правильно, зачем нам зонтик. Выпьем?')
    options = {'да': True, 'нет': False}
    option=''
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        print('Могли бы остаться трезвым с зонтиком.')
        return 0
    else:
        print('Ваша цель неясна.')
        return 0


if __name__ == '__main__':
    step1()

