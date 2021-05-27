count = int(input("Введите количество билетов "))
age = 0
final_sum = 0
for i in range (count):
    age = int(input("Введите возраст "))
    if age >= 18:
        if age < 25:
            final_sum += 990
        else:
            final_sum += 1390
if count > 3:
    final_sum *=0.9

print(" итог: ",final_sum)	
