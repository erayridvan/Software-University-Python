area_to_greening = float(input())
money_for_greening = area_to_greening*7.61
discount = 0.18*money_for_greening
total_money_for_greening=money_for_greening-discount
print(f"The final price is: {total_money_for_greening:.2f} lv.")
print(f"The discount is: {discount:.2f} lv.")