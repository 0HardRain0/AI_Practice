# parameter 없음, 반환값 없음
def a_calculateRectangleArea():
    print(5 * 7)


# parameter 있음, 반환값 없음
def b_calculateRectangleArea(x, y):
    print(x * y)


# parameter 없음, 반환값 있음
def c_calculateRectangleArea():
    return 5 * 7


# parameter 있음, 반환값 있음
def d_calculateRectangleArea(x, y):
    return x * y

print(d_calculateRectangleArea(5,7))