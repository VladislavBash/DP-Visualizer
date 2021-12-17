def tabl(array: list):
    """Находит максимальную сумму чисел, расположенных на клетках таблицы, по которой можно двигаться либо вниз, либо вправо.

    Ключевые аргументы:
    array -- двумерный массив, соедражий числа, которые расположены на клетках
    """
    m = 0
    n = len(array)
    for u in array:
        m = max(m, len(u))
    for y in range(len(array)):
        if len(array[y]) < m:
            for r in range(m-len(array[y])):
                array[y].append(0)
    for j in range(1,n):
        for i in range(1,m):
            array[j][i] += max(array[j-1][i], array[j][i-1])
    try:
        return array[0][0] + array[-1][-1]
    except:
        return None