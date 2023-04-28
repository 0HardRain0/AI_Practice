def swap_value(x, y):
    temp = x
    x = y
    y = temp


# a 리스트의 전역 변수 값을 직접 변경
def swap_offset(offset_x, offset_y):
    temp = a[offset_x]
    a[offset_x] = a[offset_y]
    a[offset_y] = temp


# a 리스트 객체의 주소 값을 받아 값을 변경
def swap_reference(list, offset_x, offset_y):
    temp = list[offset_x]
    list[offset_x] = list[offset_y]
    list[offset_y] = temp


a = [1,2,3,4,5]
swap_value(a[1], a[2])
print(a)
swap_offset(1, 2)
print(a)
swap_reference(a, 1, 2)
print(a)