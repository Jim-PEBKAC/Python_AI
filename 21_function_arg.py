# 인자값으로 아무것도 안들어왔을 때 에러를 뜨지 않게하기 위해 기본값 설정 가능
def plus(num=0):
    result = num + 5
    return result

print(plus(5))  # 프린트 값 10
print(plus())


# 인자값(기본값)의 종류를 튜플(수정불가 List 형태)로만 받겠다 /별(*)표시를 앞에 붙이면
def tuple_args(*numbers):
    print(numbers)
    total = 0
    for num in numbers:
        total += num
    return total
print(tuple_args(1,2,3,4,5))