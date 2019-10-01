age = float(input())
symbol = input()

if age >= 16:
    if symbol == 'f':
        print("Ms.")
    else:
        print("Mr.")
elif age < 16:
    if symbol == 'f':
        print("Miss")
    else:
        print("Master")
