import sys
print("java", "javascript", "python", sep=",", end="?")
print("무엇이 더 재미있나?")

print("java", "python", file=sys.stdout)
print("java", "python", file=sys.stderr)

scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    # print(subject,score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

for num in range(1, 10):
    print("대기번호 : " + str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 : ")
# print("입력하신 값은" + answer + "입니다.")
answer = 10
print(type(answer))

print("{0: >10}".format(500))
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
print("{0:_<+10}".format(500))
print("{0:,}".format(1000000))
print("{0:+,}".format(1000000))
print("{0:+,}".format(-1000000))
print("{0:^<+30,}".format(1000000))
print("{0:f}".format(5/3))
print("{0:.2f}".format(5/3))

# score_file = open("score.txt", "w", encoding="utf-8")
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf-8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf-8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

score_file = open("score.txt", "r", encoding="utf-8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")

    score_file.close()

# import pickle
# profile_file = open("profile.pickle","wb")
# profile = {"이름":"박명수","나이":50,"취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile,profile_file)
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

# with open("study.txt","w", encoding="utf-8") as study_file:
#     study_file.write("파이선기초공부")

with open("study.txt","r", encoding="utf-8") as study_file:
    print(study_file.read())

for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding="utf-8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")