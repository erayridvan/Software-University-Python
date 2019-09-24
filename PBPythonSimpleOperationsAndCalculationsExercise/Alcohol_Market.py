price_of_wiskey = float(input())
quantity_of_beer = float(input())
quantity_of_wine = float(input())
quantity_of_rakiya = float(input())
quantity_of_wiskey = float(input())

price_of_rakiya = price_of_wiskey / 2
price_of_wine = price_of_rakiya-(0.4 * price_of_rakiya)
price_of_beer = price_of_rakiya-(0.8 * price_of_rakiya)

total_money_for_rakiya = quantity_of_rakiya * price_of_rakiya
total_money_for_wine = quantity_of_wine * price_of_wine
total_money_for_beer = quantity_of_beer * price_of_beer
total_money_for_wiskey = quantity_of_wiskey * price_of_wiskey

total_sum = total_money_for_rakiya + total_money_for_wine + total_money_for_beer + total_money_for_wiskey

print(f'{total_sum:.2f}')