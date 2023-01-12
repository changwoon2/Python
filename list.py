# 자료구조
subway = [10,20,30]
print(subway)

subway = ["유재석","조세호","박명수"]
print(subway)

print(subway.index("조세호"))

subway.append("하하")
print(subway)

subway.insert(1, "정형돈")
print(subway)

print(subway.pop())
print(subway)

subway.append("유재석")
print(subway)
print(subway.count("유재석"))

num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

num_list.clear()
print(num_list)

num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]

num_list.extend(mix_list)
print(num_list)

cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
print(cabinet.get(5))
print(cabinet.get(5,"사용 가능"))
print("hi")
print(3 in cabinet)
print(5 in cabinet)

cabinet = {"A-3":"유재석","B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세종"
print(cabinet)

del cabinet["A-3"]
print(cabinet)

print(cabinet.keys())

print(cabinet.values())

print(cabinet.items())

cabinet.clear()
print(cabinet)

menu = ("돈까스","치즈까스")
print(menu[0])
print(menu[1])

name = "김종국"
age = 20
hobby = "헬스"
print(name,age,hobby)

my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석","박명수"])

print(java & python)
print(java.intersection(python))

print(java | python)
print(java.union(python))

print(java - python)
print(java.difference(python))

python.add("김태호")
print(python)

java.remove("김태호")
print(java)

menu = {"커피","우유","주스"}
print(menu, type(menu))
menu = list(menu)
print(menu, type(menu))
menu = tuple(menu)
print(menu, type(menu))
menu= set(menu)
print(menu, type(menu))

from random import *
users = range(1,21)
users = list(users)

print(users)
shuffle(users)
print(users)

winners = sample(users,4)

print("당첨자발표")
print("치킨당첨자 : {0}".format(winners[0]))
print("커피당첨자 : {0}".format(winners[1:]))
print("축하합니다")