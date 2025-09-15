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
# 이 방식은 사용자가 인자값의 개수를 자유롭게 정해서 넣을 수 있다.
print(tuple_args(1,2,3,4,5))

# 별(**) 표시를 앞에 붙이면 매개변수를 딕셔너리 형태(키와 벨류)로 받겠다.
def dic_args(**dic):
    # 1. dic에서 값만 빼온다.
    # 2. 이 값들을 하나씩 더해 누적시킨다.
    # 3. 누적시킨 값을 밖으로 return 한다.
    values = dic.values()
    print(values)
    total = 0
    for i in values:
        total = total + i
    return total

#   밑에는 items에 대한 이해가 더 필요할 듯
#   for key, value in dic.items(): 
#   total += value  # total = total + value
#   return total

# 위 함수를 실행하면 입력된 값들의 합산이 반환된도록 하세요.
result = dic_args(kim=50,less=100, park=70,na=90)
print(result)

print('------------------')



