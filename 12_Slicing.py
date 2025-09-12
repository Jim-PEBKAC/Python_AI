# 초기 리스트
arr = ['Life', 'is', 'too', 'short']
print('[초기]    ', arr)  # ['Life', 'is', 'too', 'short']

# --- 슬라이싱 결과 확인 ---      → [a:b] a이상 b미만
area = arr[0:2]  # 인덱스 0~1 (2는 미포함) => ['Life','is']
print('arr[0:2]  ', area)

area = arr[1:3]  # 인덱스 1~2 (3은 미포함) => ['is','too']
print('arr[1:3]  ', area)

area = arr[:2]   # 인덱스 0~1 => ['Life','is']
print('arr[:2]   ', area)

area = arr[2:]   # 인덱스 2부터 끝 => ['too','short']
print('arr[2:]   ', area)

# --- 슬라이스 대입---
arr = ['Life', 'is', 'too', 'short']  # 다시 초기화
arr[1:3] = ['A', 'B', 'C']  # 인덱스 1~2('is','too')를 세 개로 대체 → 길이 증가
print('[대입1 후]', arr)  # ['Life','A','B','C','short']

arr[2:3] = ['가', '나', '다']  # 인덱스 2('B')를 세 개로 대체 → 길이 증가
print('[대입2 후]', arr)  # ['Life','A','가','나','다','C','short']

arr[2:2] = ['가', '나', '다']  # 인덱스 2('B')를 세 개로 대체 → 길이 증가
print('[대입3 후]', arr) # ['Life', 'A', '가', '나', '다', '가', '나', '다', 'C', 'short']
# 대체할 수 있는 범위 내 원소가 없으니까 그냥 그 위치에 있는 걸 밀고 끼워라.



#리스트끼리 연산
a=[1,2,3,4,5]
b=['a','b','c','d']
print(a+b)
print(a*3)