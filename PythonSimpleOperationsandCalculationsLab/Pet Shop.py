number_of_dogs = int(input())
number_of_other_animals = int(input())
money_needed_fir_dogs = number_of_dogs*2.50
money_needed_for_rest_animals = number_of_other_animals*4.00
total_money = money_needed_fir_dogs+money_needed_for_rest_animals
print(f"{total_money:.2f} lv.")