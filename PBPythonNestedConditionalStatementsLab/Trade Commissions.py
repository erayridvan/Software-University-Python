import sys

city_name = input()
sales = float(input())
commision = 0;


if city_name == 'Sofia':
    if sales <= 500:
        commision = 5
    elif sales <= 1000:
        commision = 7
    elif sales <= 10000:
        commision = 8
    elif sales > 10000:
        commision = 12

elif city_name == 'Varna':
    if sales <= 500:
        commision = 4.5
    elif sales <= 1000:
        commision = 7.5
    elif sales <= 10000:
        commision = 10
    elif sales > 10000:
        commision = 13

elif city_name == 'Plovdiv':
    if sales <= 500:
        commision = 5.5
    elif sales <= 1000:
        commision = 8
    elif sales <= 10000:
        commision = 12
    elif sales > 10000:
        commision = 14.5

total_money = commision * sales / 100

if commision<=0:
    print('error')
elif total_money<=0:
    print('error')
else:
    print(f'{total_money:.2f}')
