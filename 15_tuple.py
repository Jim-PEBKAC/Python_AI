tu1 = (1,2,3)
tu2 = ('a','b','c')
tu3 = (1,2,('a','b'))

# 단순 불러오기
print(tu1[1])
# slicing
print(tu2[1:])
# 더하기
print(tu1+tu2)
# 곱하기
print(tu1*3)

# tuple ↔ list 전환
tu2list = list(tu2)
print(f'{tu2} → {tu2list}')  # 튜플을 리스트로

list2tu = tuple(tu2list)
print(f'{tu2list} → {list2tu}') # 리스트를 튜플로