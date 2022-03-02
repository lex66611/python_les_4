def zp():
    try:
        time = float(input('Выработка (ч): '))
        salary = int(input('Ставка ($): '))
        bonus = int(input('Премия ($): '))
        res = time * salary + bonus
        print(f'заработная плата сотрудника  {res}')
    except ValueError:
        return print('Неверные данные')
zp()
# завершено