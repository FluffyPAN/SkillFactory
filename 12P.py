per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите количество денег "))
v = list(per_cent.values())
v = list(map(lambda x: x* money*0.01, v))
print(v)
print(max(v))