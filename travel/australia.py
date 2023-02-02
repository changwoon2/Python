class AustraliaPackage:
    def detail(self):
        print("[호주 패키지 3박 5일] 방콕, 파타야 여행 100만원")

if __name__ == "__main__":
    print("호주 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
    trip_to = AustraliaPackage()
    trip_to.detail()
else:
    print("호주 외부에서 모듈 호출")