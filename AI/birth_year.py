# 태어난 년도를 계산하여 학력 구분 (만 나이 아님)

from datetime import datetime

def birth(year):
    age = int(datetime.today().year) - year + 1
    print(age) # 만 나이 아님 (확인용)
    if 20 <= age <= 26:
        print("대학생")

    elif 17 <= age < 20:
        print("고등학생")

# 숫자 <= 변수 and 변수 < 숫자 가 아닌 숫자 <= 변수 <= 숫자 로 표기가 가능 대신 and라 가능
# 대신 권장하지 않음
    elif 14 <= age < 17:
        print("중학생")

    elif 8 <= age < 14:
        print("초등학생")

    else:
        print("학생이 아닙니다.")


year = int(input("당신이 태어난 년도를 입력하세요"))
print(year)
birth(year)

