# 연산자
print(1+1)
print(3-2)
print(5*2)
print(6/3)
print(2**3)
print(5%3)
print(10%3)
print(5//3)
print(10//3)
print(10>3)
print(4>=7)
print(10<3)
print(5<=5)
print(3==3)
print(4==2)
print(3+4==7)
print(1 != 3)
print(not (1 != 3))
print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))
print((3 > 0) or (3 > 5))
print((3 > 0) | (3 > 5))
print(5 > 4 > 3)
print(5 > 4 > 7)

print(2 + 3 * 4)
print((2 + 3) * 4)
number = 2 + 3 * 4
print(number)
number = number + 2
print(number)
number += 2
print(number)
number *= 2
print(number)
number /= 2
print(number)
number -= 2
print(number)

number %= 5
print(number)

print(abs(-5))
print(pow(4,2))
print(max(5,12))
print(min(5,12))
print(round(3.14))
print(round(4.99))

from math import *
print(floor(4.99))
print(ceil(3.14))
print(sqrt(16))

from random import *
print(random())
print(random()*10)
print(int(random()*10))
print(int(random()*10) + 1)
print(int(random()*45) + 1)
print(randrange(1, 45))
print(randint(1, 90))
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월" + str(date) + "일로 선정되었습니다.")