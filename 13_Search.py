# 검색 → 특정한 자료에서 원하는 값을 찾는 것
from operator import truediv
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
idx = 0
# while True:
#     idx = b.index(3,idx)
#     print(f'3의 값은 {idx}번째에 있다')
#     idx += 1

for n in b: # for in을 이용하면 list에 있는 값을 순서대로 하나씩 뽑는다.
    if n ==3:
        print(f'3이 있는 인덱스:{idx}')
    idx += 1