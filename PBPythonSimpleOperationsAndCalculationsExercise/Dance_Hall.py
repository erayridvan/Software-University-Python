import  math

lenght_of_hall = float(input())
width_of_hall = float(input())
side_of_wardrobe = float(input())

hall_area_santimeter = (lenght_of_hall*100)*(width_of_hall*100)
wardrobe_area = (side_of_wardrobe*100)*(side_of_wardrobe*100)
bench_area = hall_area_santimeter/10
free_space = hall_area_santimeter-wardrobe_area-bench_area
number_of_dancers = free_space/(40+7000)

print(f'{math.floor((number_of_dancers))}')