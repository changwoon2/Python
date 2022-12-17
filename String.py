# 문자열
sentence = "나는 소년입니다."
print(sentence)
sentence1 = "파이썬강의."
print(sentence1)
sentence3 = """
나는소년이고,
파이썬은쉬워요
"""
print(sentence3)

jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])
print("별 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 (뒤에부터): " + jumin[-7:])

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n")
print(index)
index = python.index("n" , index + 1)
print(index)

print(python.find("Java"))
print('hi')
print(python.count("n"))

print("나는 %d살입니다." % 20)
print("나는 %s을좋아해요." % "파이썬")
print("apple %c시작해요." % "A")
print("나는 %s시작 %s끝" % ("파란", "빨간"))

print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))


print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))

age = 20
color = "주황"
print(f"나는{age}살이며,{color}색을좋아해요.")

print("백문이 붙여일견\n백견이 불여일타")
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")

print("C:/Users/changwoon/AppData/Local/Microsoft/WindowsApps>")

print("Red Apple\rPine")

print("Redd\bApple")

print("Red\tApple")

url = "http://youtube.com"
my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다." .format(url, password))