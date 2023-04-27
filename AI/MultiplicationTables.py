# 구구단

def multipli(data):
    for i in range(1, 10):
        print(f"{data} X {i} = {data*i}")

print("구구단 몇단을 계산할까요? ")
data = int(input())
multipli(data)
