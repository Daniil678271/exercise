import math
a = 0.3
b = 900
c = 1/4
d = 64
S_1 = a * math.sqrt(b) - c * math.sqrt(64)
print(S_1)

a_1 = 8
b_1 = 20
c_1= 1/4
d_1 = 0.36
S_2 = a_1 * math.sqrt(b_1 * c_1) - math.sqrt(d_1)
print(S_2)

a_2 = 0.64
b_2 = 49
c_2 = 3**4
d_2 = 2**6
S_3 = math.sqrt(a_2 * b_2) - math.sqrt(c_2 * d_2)
print(S_3)
#реализовать дома try else finally
#2 Задание
x = math.sqrt(4)
print(x)

x_1 = math.sqrt(5)
print(x_1)

a_4 = 8
b_4 = 4
X=(a_4**2)/(b_4**2)
print(X)

#задание 4
a = 5
b = math.sqrt(3)
S = a/b
print(S)

a_1 = 3
b_1 = 2
S_1 = a_1/b_1 * math.sqrt(6)
print(S_1)

a_2 = 7
a_2 = a * math.sqrt(a)
S_2 = a_2/a_2
print(S_2)

a_3 = 5
b_3 = math.sqrt(6 - 1)
S_3 = a_3/b_3
print(S_3)
#задание 5
l = 5*math.sqrt(2)
d = 2 * math.sqrt(5)
if l > d:
    print("l > d")
elif l < d:
    print("l < d")
else:
    print("l = d")

s = 4 * math.sqrt(3/4)
z = 2 * math.sqrt(7/8)
if s > z:
    print("s > z")
elif s < z:
    print("s < z")
else:
    print("s = z")
