def print_max(x,y): # x,y 중에 누가 더 크냐
    '''
    입력된 x와 y 중 큰 값을 알려주는 함수 입니다.
    :param x: 인자값 1
    :param y: 인자값 2
    :return:
    '''
    print(f'{x}와{y} 중에...')
    if x > y:
        print(f'{x}가 더 큽니다.')
    else:
        print(f'{y}가 더 큽니다.')
print_max(5,10)

# 해당 함수에 대한 설명 출력
print(f'함수설명:{print_max.__doc__}')