# 화씨 변화기

def fahrenheit(temp):
    temp = ((9/5) * temp) + 32
    return temp


print("본 프로그램은 섭씨를 화씨로 변환해주는 프로그램입니다.")
temp = float(input("변환하고 싶은 섭씨 온도를 입력해 주세요:"))

# 입력이 string이므로 숫자 입력일 경우 int나 float형으로 넣었음
print(f"섭씨온도 : {temp:.2f}")
print(f"화씨온도 : {fahrenheit(temp):.2f}")

# print("화씨온도 :  %.2f" % (fahrenheit(temp))) 내가 생각했던것