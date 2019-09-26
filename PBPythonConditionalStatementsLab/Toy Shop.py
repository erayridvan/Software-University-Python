value_of_trip = float(input())
number_of_puzzles = int(input())
number_of_dools = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

total_money_earn = (number_of_puzzles * 2.60) + (number_of_dools * 3) + (number_of_bears * 4.10) + (
        number_of_minions * 8.20) + (number_of_trucks * 2)

number_of_toys = number_of_puzzles + number_of_dools + number_of_bears + number_of_minions + number_of_trucks

if number_of_toys >= 50:
    total_money_earn = total_money_earn - (total_money_earn * 0.25)

total_money_earn = total_money_earn - (total_money_earn * 0.10)

if total_money_earn >= value_of_trip:
    left_money = total_money_earn - value_of_trip
    print(f'Yes! {left_money:.2f} lv left.')
else:
    needed_money = abs(total_money_earn - value_of_trip)
    print(f'Not enough money! {needed_money:.2f} lv needed.')
