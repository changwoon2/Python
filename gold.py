print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))
# 참 / 거짓 
print(5 > 10)
print(5 < 10)
print(not True)
print(not False)

# 애완동물 소개해주세요 변수
name ="강아지"
animal ="연탄이"
age = 4
hobby ="산책"
is_adult = age >= 3

print("우리집 " + animal + " 이름은 " + name + "예요")
print(name + "는" + str(age) + " 살이며, "+ hobby + "을 아주 좋아해요")
print(name + "는 어른일까요? " + str (is_adult))

from random import *

print(random())
print(random() * 10)
print(int(random() * 10))
print(int(random() * 10) + 1)

print(randrange(1,46))
print(randint(1,45))

date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월" + str(date) + " 선정되었습니다.")