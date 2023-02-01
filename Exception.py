# try:
#     print("나누기 전용 계산기")
#     nums = []
#     nums.append(int(input("첫번째숫자")))
#     nums.append(int(input("두번째숫자")))
#     nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}" .format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러 잘못된값")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알수없는에러")
#     print(err)


# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg


# try:
#     print("한자리숫자나누기")
#     num1 = int(input("첫번째숫자"))
#     num2 = int(input("두번째숫자"))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}" .format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된값입력 한자리숫자만입력")
# except BigNumberError as err:
#     print("에러가발생하였습니다 한자리숫자만입력")
#     print(err)
# finally:
#     print("계산기를 이용해주세요")

class SoldOutError(Exception):
    pass


chicken = 10
waiting = 1

while (True):
    try:
        print("[남은 치킨 : {0}" .format(chicken))
        order = int(input("치킨 몇마리 주문하시겠습니까"))
        if order > chicken:
            print("재료가 부족합니다")
        elif order <= 0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1} 마리 주문이 되었습니다"
                  .format(waiting, order))
            waiting += 1
            chicken -= order
        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다")
    except SoldOutError:
        print("재고가 소진되어 더이상 주문 받지 않습니다")
        break
