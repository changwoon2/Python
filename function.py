def open_account():
    print("새로운 계좌가 생성")


def deposit(balance, money):
    print("입금이 완료되었습니다 잔액은 {0} 원입니다." .format(balance + money))
    return balance + money


def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다 잔액은 {0} 원입니다." .format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다." .format(balance))
        return balance


def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission


balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다." .format(commission, balance))


def profile(name, age=17, main_lang="java"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"
          .format(name, age, main_lang))


profile("html")
profile("css")


def profile(name, age, main_lang):
    print(name, age, main_lang)


profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")


def profile(name, age, *language):
    print("이름 : {0}\나이 : {1}\t".format(name, age), end="")
    for lang in language:
        print(lang, end="")
        print()


profile("김태호", 20, "파이선", "자바", "c", "c++", "c#")
profile("김종국", 27, "코틀린", "뷰", "", "", "")

gun = 10


def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}" .format(gun))


def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}" .format(gun))
    return gun


print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))


def std_weight(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21


height = 175
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
