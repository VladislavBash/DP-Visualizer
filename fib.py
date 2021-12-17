def fiban(n: int):
    """Находит число Фибоначчи под номером 'n'.

    Ключевые аргументы:
    n -- номер числа Фибоначчи
    """
    prev = 1
    current = 1
    if n <= 0:
        return None
    for i in range(n-2):
        buf = current
        current += prev
        prev = buf
    return current