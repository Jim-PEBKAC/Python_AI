from logging import exception

num_list = [1,2,3,1,2,3,1,2,3,1,2,3,4,5,6]

idx = 0

try:
    while True:
        idx=num_list.index(3,idx)
        print(f'3은 {idx} 인덱스에 있습니다. ')
        idx=idx+1
# 여기까지만 실행했을 경우, ValueError: 3 is not in list 발생
except ValueError as e:
    print(e) # 예외에 대한 대략적인 정보 출력
    print('더 이상 존재하지 않습니다.')
finally:
    print('=====끝=====')

