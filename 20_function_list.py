#반환타입(결과값): O 매개변수(동전): O  자판기

def auto(coin): #
    return f'구매한 {coin}원짜리 음료수' # 프린트랑 다르게 실제 결과값을 내는 거임 프린트는 요청한 온전한 그대로를 냄

# 함수 사용
att=auto('1000')
print(att)

print('--------------------------------')

#반환타입(용지): O 매개변수(넣은 거 없음): X  번호표

def num():
    cou = 1
    print(f'{cou}번 번호표 입니다.')
    return f'{cou}번 번호표'
papper = num()
print(papper)

#반환타입(나온 거 없음): X 매개변수(동전): O  저금통

def pig(con):
    print(f'{con}원을 넣었습니다')

btt=pig(1000)
print(btt)

#반환타입(나온 거 없음): X 매개변수(넣은 거 없음): X  호출벨

def ring():
    print(f'호출벨이 울립니다.')

tou=ring()
print(tou)