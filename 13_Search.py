# 검색 → 특정한 자료에서 원하는 값을 찾는 것
from operator import truediv
from os import remove
from re import search

a=[3,4,1,2,5,6,7,'G','A','G',3]

#위에서 원하는 값에서 원하는 Index 찾기
# 2라는 값은 몇 번째에 위치해있나?

print(f'2는 어디?: {a.index(2)}')
print(f'G는 어디?: {a.index('G')}') # 현재 G는 두 개지만 처음 위치만 알려준다.

# 8번째 이후부터 G를 찾아라
print(f'G는 어디?: {a.index('G',8)}')

# 값이 없으면 에러(예외)를 발생시킨다.
# print(a.index('H')) 실행 시, 발생 → ValueError: 'H' is not in list

b=[3,4,1,2,3,4,5,6,6,7,3,2,3,3,5,1,5] # 모든 3을 찾아라.
# print(f'첫 번째 3: {b.index(3)}')
# print(f'두 번째 3: {b.index(3,1)}')
# print(f'세 번째 3: {b.index(3,5)}')
# print(f'네 번째 3: {b.index(3,11)}')
# print(f'다섯 번째 3: {b.index(3,13)}')
idx = 0 # 0부터 하는 이유는 개발 환경에서 0 = 1을 의미하기 때문 [초기값 설정]


# while True: # 참이면 계속해라
#     idx = b.index(3,idx) # 
#     print(f'3의 값은 {idx}번째에 있다') 
#     idx += 1

for n in b: # for in을 이용하면 list에 있는 값을 순서대로 하나씩 뽑는다.
    if n ==3:
        print(f'3이 있는 인덱스:{idx}')
    idx += 1

print(f'a:{a}')
a.remove(3)
print(f'a:{a}')

# pop() = append의 반대 개념
# pop은 맨 뒷줄 원소부터 제거한다.

val=a.pop()
print(f'빼낸 값: {val} / a:{a}')
val=a.pop()
print(f'빼낸 값: {val} / a:{a}')

# 리스트 확장(더하기와 비슷한 개념)
print(a)
a.extend(b)
print(a)

# count(val) 특정한 값이 해당 리스트에 몇 개가 있는지 확인
print(a.count(3)) # a안에 3이 몇 개냐
print(a.count(0)) # a안에 0이 몇 개냐 → 없는 값 0 반환됌

# a 안에 있는 모든 3을 지워라.
a=[3,4,1,2,5,6,7,'G','A','G',3]

# for n in a:
#     if n ==3:
#         a.remove(3)
# print(a)

while True:
    a.remove(3)
    if a.count(3) ==0:
        break
print(a)
