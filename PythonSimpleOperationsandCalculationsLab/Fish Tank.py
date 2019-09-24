lenght = float(input())
witdh = float(input())
height = float(input())
procent_occupied_part = float(input())

capacity_of_auquarium = lenght*witdh*height
total_liters = capacity_of_auquarium*0.001
litres_available = total_liters*(1-(procent_occupied_part*0.01))
print(f"{litres_available:.3f}")