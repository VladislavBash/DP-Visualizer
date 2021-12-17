from browser import document, svg, timer, alert, bind, html
height = 2
len = 3
red_k = 6
green_k = 1
blue_k = 6
i = 0
j = 0
b = 0
def Visualization_count(posx=0, posy=0, height=0, len=0):
    """Визуализирует алгоритм, где на вход подаётся двумерный массив.

Ключевые аргументы:
posx -- позиция первого 'rect' по оси x (по умолчанию 0)
posy -- позиция первого 'rect' по оси y (по умолчанию 0)
height -- кол-во 'rect' в столбце (по умолчанию 0)
len -- кол-во 'rect' в строке (по умолчанию 0)
"""
    posx += 100
    posy += 100
    red_k = 6
    green_k = 2
    blue_k = 3
    document['panel'] <= svg.text('elem 1', x=80, y=80)
    for j in range(height):
        for i in range(len):
            col = "rgb" + str((250-i*red_k-i*red_k, 242-i*green_k-i*green_k, 93-i*blue_k-i*blue_k))
            rect = svg.rect(id=j*len+i, x=posx+60*i, y=posy+60*j, height="50", width="50", fill=col, stroke="black", stroke_width="2")
            document['panel'] <= rect
    document['panel'] <= svg.text('elem 2', x=posx+60*i+60, y=posy+60*j+30)
def Visualization_str(posx, posy, len):
    """Визуализирует алгоритм, где на вход подаётся одномерный массив.

Ключевые аргументы:
posx -- позиция первого 'rect' по оси x (по умолчанию 0)
posy -- позиция первого 'rect' по оси y (по умолчанию 0)
len -- кол-во 'rect' в строке (по умолчанию 0)
"""
    posx += 100
    posy += 100
    red_k = 1
    green_k = 4
    blue_k = 3
    document['panel'] <= svg.text('elem 1', x=80, y=80)
    for i in range(len):
        col = "rgb" + str((250-i*red_k**2-i*red_k**2, 242-i*green_k**2-i*green_k**2, 93-i*blue_k**2-i*blue_k**2))
        rect = svg.rect(id=j*len+i, x=posx+60*i, y=posy+60*j, height="50", width="50", fill=col, stroke="black", stroke_width="2")
        document['panel'] <= rect
    document['panel'] <= svg.text('elem 2', x=posx+60*i+60, y=posy+60*j+30)
def config():
    """Заполняет поле анализа функции"""
    document['coding'] <= txt
sel1 = document['prog']
sel2 = document['appr']
txt = document['in'].value
def show_selected_1(ev):
    """После выбора значения из списка активирует функциюы.

Ключевые аргументы:
ev -- нужен, чтобы работал .bind
"""
    for option in sel1:
         if option.selected:
             if option.id == 'counting':
                 document['in'].value = "Massive: [5, 3, 1, 2]"
                 txt = document['in'].value
                 txt = txt[9:]
                 Visualization_count(0, 0, 5, 5)
             elif option.id == 'ball':
                 document['in'].value = "Massive: [5, 3, 1, 2]; Step1: 2; Step2: 3;"
                 txt = document['in'].value
                 texxt = ''
                 for p in txt:
                     if p == ';':
                         break
                     else: texxt += p
                 txt = texxt[9:]
                 step1 = txt[-12]
                 step2 = txt[-2]
                 Visualization_str(0, 0, 4)
             elif option.id == 'fib':
                 document['in'].value = "Number: [5]"
                 txt = document['in'].value
                 txt = txt[-2]
                 Visualization_str(0, 0, int(txt))
document['prog'].bind("change", show_selected_1)
def prnty(ev):
    """Визуально выделяет 'rect'.

Ключевые аргументы:
ev -- нужен, чтобы работал .bind
"""
    alert('asdas')
document["2"].bind("mouseenter", prnty)
