x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

lenght = abs(x1 - x2)
witdh = abs(y1 - y2)

area = lenght * witdh
perimeter = 2 * lenght + 2 * witdh

print(f'{area:.2f}')
print(f'{perimeter:.2f}')
