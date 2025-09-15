# 함수선언(define)

def toaster(bread):
    print(f'{bread}가 구워지고 있다.')
    return f'구워진{bread}' # 프린트랑 다르게 실제 결과값을 내는 거임 프린트는 요청한 온전한 그대로를 냄

# 함수 사용
dish=toaster(' 소보로')
print(dish)