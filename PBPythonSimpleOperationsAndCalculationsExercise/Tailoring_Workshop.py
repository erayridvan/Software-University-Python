number_of_tables = int(input())
lenght_of_tables = float(input())
witdh_of_tables = float(input())

total_area_of_cloths = number_of_tables*(lenght_of_tables+2*0.30)*(witdh_of_tables+2*0.30)
total_area_of_quads = number_of_tables*(lenght_of_tables/2)*(lenght_of_tables/2)

price_in_dollars = total_area_of_cloths*7+total_area_of_quads*9
price_in_levas = price_in_dollars*1.85

print(f'{price_in_dollars:.2f} USD')
print(f'{price_in_levas:.2f} BGN')