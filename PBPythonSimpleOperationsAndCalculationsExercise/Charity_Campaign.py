number_of_days = int(input())
number_of_cake_makers = int(input())
number_of_cakes = int(input())
number_of_goff = int(input())
number_of_pancakes = int(input())

cakes = number_of_cakes*45
goffs = number_of_goff*5.80
pancakes = number_of_pancakes*3.20

sum = (cakes+goffs+pancakes)*number_of_cake_makers
total_sum = sum*number_of_days
left_money = total_sum-((1/8)*total_sum)

print(f'{left_money:.2f}')