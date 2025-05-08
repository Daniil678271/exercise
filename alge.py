import math 
a = int(input("Введіть з клавіатури a"))
if a > 0:
    print(a**7 * math.sqrt(81 * a**2))
elif a < 0:
    print("Корнів немає")
else:
    print(a**7 * math.sqrt(81 * a**2))

x = float(input("Введіть число з клавіатури x"))
y = int(input("Введіть число з клавіатури y"))
if x <= 0 and y <= 0:
    print(0,36 * x**14 * y**10)
else:
    print("Коренів немає")
