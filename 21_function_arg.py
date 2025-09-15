# 인자값으로 아무것도 안들어왔을 때 에러를 뜨지 않게하기 위해 기본값 설정 가능
def plus(num=0):
    result = num + 5
    return result

print(plus(5))  # 프린트 값 10
print(plus())