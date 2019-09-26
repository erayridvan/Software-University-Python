import math

type_of_figure = input()

if type_of_figure == 'square':
    side = float(input())
    area = side * side
    print(f'{area:.3f}')
elif type_of_figure == 'rectangle':
    first_side = float(input())
    second_side = float(input())
    area = first_side * second_side
    print(f'{area:.3f}')
elif type_of_figure == 'circle':
    radius = float(input())
    area = radius * radius * math.pi
    print(f'{area:.3f}')
elif type_of_figure == 'triangle':
    side = float(input())
    height = float(input())
    area = (side * height) / 2
    print(f'{area:.3f}')
